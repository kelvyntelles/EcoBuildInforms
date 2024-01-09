from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("introducaoFibrasVegetais", views.introducao_fibras_vegetais, name='introducao_fibras_vegetais'),
    path("tiposFibras", views.tipos_fibras, name='tipos_fibras'),
    path("aplicabilidadeConstrucaoCivil", views.aplicabilidade_contrucao_civil, name='aplicabilidade_contrucao_civil'),
    path("importanciaAmbiental", views.importancia_ambiental, name='importancia_ambiental'),
    path("contatos", views.contatos, name='contatos'),
    path("sugestaoTopico", views.sugestao_topico, name='sugestao_topico'),
    path("salvarSugestaoTopico", views.salvar_sugestao_topico, name='salvar_sugestao_topico'),
    path("sugestaoTopicoCriada", views.salvar_sugestao_topico, name='salvar_sugestao_topico'),
]





