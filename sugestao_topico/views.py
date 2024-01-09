from django.shortcuts import render
from django.http import HttpResponse
from .models import SugestaoTopico


def home(request):
    return render(request, 'home.html')


def introducao_fibras_vegetais(request):
    return render(request, 'introducaoFibrasVegetais.html')


def tipos_fibras(request):
    return render(request, 'tiposFibras.html')


def aplicabilidade_contrucao_civil(request):
    return render(request, 'aplicabilidadeConstrucaoCivil.html')


def importancia_ambiental(request):
    return render(request, 'importanciaAmbiental.html')


def contatos(request):
    return render(request, 'contatos.html')


def sugestao_topico(request):
    return render(request, 'sugestaoTopico.html')


def salvar_sugestao_topico(request):
    titulo = request.POST.get("titulo")
    resumo = request.POST.get("resumo")
    nome = request.POST.get("nome")
    contato = request.POST.get("contato")

    if titulo == "" or resumo == "" or nome == "" or contato == "":
        erro = "Preencha todos os campos"
        return render(request, 'sugestaoTopico.html', {
            "erro": erro
        })

    SugestaoTopico.objects.create(
        titulo=titulo,
        resumo_topico=resumo,
        nome_autor=nome,
        contato_autor=contato
    )

    return render(request, 'sugestaoTopicoCriada.html')


def sugestao_topico_criada(request):
    return render(request, 'sugestaoTopicoCriada.html')






