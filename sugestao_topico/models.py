from django.db import models


class SugestaoTopico(models.Model):
    titulo = models.CharField(max_length=70)
    resumo_topico = models.TextField()
    nome_autor = models.CharField(max_length=50)
    contato_autor = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo
