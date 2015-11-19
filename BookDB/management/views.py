# from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import Author, Book

# Create your views here.

def showHomepage(req):
	if req.POST:
		post = req.POST
		name = post["name"]
		try:
			authorid = Author.objects.get(Name = name).AuthorID
			book_list = Book.objects.filter(AuthorID = int(authorid))
			c = RequestContext(req, {"book_list":book_list},)
		except:
			c = RequestContext(req, {"book_list":Book.objects.all()},)
		return render_to_response("index.html", c)
	else:
		c = RequestContext(req, {"book_list":[]},)
		return render_to_response("index.html", c)

def showHomepage_rdir(req):
	return HttpResponseRedirect("/management/")

def viewInfoPage(req):
	if req.GET:
		isbn = int(req.GET.get("isbn", None))
		try:
			book = Book.objects.get(ISBN = isbn)
			author = Author.objects.get(AuthorID = book.AuthorID)
		except:
			return HttpResponseRedirect("/management/")
		c = RequestContext(req, {"book":book, "author":author},)
		return render_to_response("info.html", c)
	else:
		return HttpResponseRedirect("/management/")

def addBook(req):
	author_list = Author.objects.all()
	count = author_list.count()
	if req.POST:
		post = req.POST
		new_book = Book(ISBN = int(post["isbn"]),\
			Title = post["title"],\
			AuthorID = count,\
			Publisher = post["publisher"],\
			PublishDate = int(post["publishdate"]),\
			Price = int(post["price"]))
		if post["authorid"] == 'N':
			new_author = Author(AuthorID = count,\
				Name = post["name"],\
				Age = int(post["age"]),\
				Country = post["country"])
			new_book.save()
			new_author.save()
		else:
			new_book.AuthorID = int(post["authorid"])
			new_book.save()
		return HttpResponseRedirect("/add_book/")
	c = RequestContext(req, {"author_list":author_list},)
	return render_to_response("add.html", c)

def delete(req):
	isbn = int(req.GET.get("isbn", None))
	book_to_delete = Book.objects.get(ISBN = isbn)
	book_to_delete.delete()
	return HttpResponseRedirect(req.META.get('HTTP_REFERER', '/'))