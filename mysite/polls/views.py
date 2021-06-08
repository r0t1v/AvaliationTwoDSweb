from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def index(request):
	if request.method == 'POST':
		mensagem = "Comentário Registrado\n"
		mensagem += "Nome: "+request.POST['nome']+"\n"
		mensagem += "Email: "+request.POST['email']+"\n"
		mensagem += "Mensagem: "+request.POST['mensagem']+"\n"
		send_mail(
			'Seu comentário em 127.0.0.1:8000 foi registrado com sucesso!',
			mensagem,
			'from@example.com',
			[''],
			fail_silently=False,
			)
	context = {
		'title': "CodeSimple"
	}
	return render(request, "polls/index.html", context)

def about(request):
	if request.method == 'POST':
		mensagem = "Comentário Registrado\n"
		mensagem += "Nome: "+request.POST['nome']+"\n"
		mensagem += "Email: "+request.POST['email']+"\n"
		mensagem += "Mensagem: "+request.POST['mensagem']+"\n"
		send_mail(
			'Seu comentário em 127.0.0.1:8000 foi registrado com sucesso!',
			mensagem,
			'from@example.com',
			[''],
			fail_silently=False,
			)
	context = {
		'title': "Sobre"
	}
	return render(request, "polls/about.html", context)

def pag1(request):
	if request.method == 'POST':
		mensagem = "Comentário Registrado\n"
		mensagem += "Nome: "+request.POST['nome']+"\n"
		mensagem += "Email: "+request.POST['email']+"\n"
		mensagem += "Mensagem: "+request.POST['mensagem']+"\n"
		send_mail(
			'Seu comentário em 127.0.0.1:8000 foi registrado com sucesso!',
			mensagem,
			'from@example.com',
			[''],
			fail_silently=False,
			)
	context = {
		'title': "Noticia 1"
	}
	return render(request, "polls/pag1.html", context)

def pag2(request):
	if request.method == 'POST':
		mensagem = "Comentário Registrado\n"
		mensagem += "Nome: "+request.POST['nome']+"\n"
		mensagem += "Email: "+request.POST['email']+"\n"
		mensagem += "Mensagem: "+request.POST['mensagem']+"\n"
		send_mail(
			'Seu comentário em 127.0.0.1:8000 foi registrado com sucesso!',
			mensagem,
			'from@example.com',
			['wanderson.helo@gmail.com'],
			fail_silently=False,
			)
	context = {
		'title': "Noticia 2"
	}
	return render(request, "polls/pag2.html", context)