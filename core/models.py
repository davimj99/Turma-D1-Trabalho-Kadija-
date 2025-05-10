from django.db import models

# Crie seus modelos aqui 

class Produto(models.Model):   
    nome = models.CharField ('Nome', max_length=100)
    preco = models.DecimalField ('Preço' , decimal_places=2 , max_digits=8)
    estoque = models.IntegerField ('Quantidade em Estoque')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100) 
       
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
class Pagamento(models.Model):
    TIPO_PAGAMENTO = [
        ('crédito', 'Crédito'),
        ('débito', 'Débito'),
        ('pix', 'PIX'),
        ('dinheiro', 'Dinheiro'),
    ]

    nome = models.CharField('Nome do Pagador', max_length=100)
    tipo = models.CharField('Tipo de Pagamento', max_length=20, choices=TIPO_PAGAMENTO)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField('Data do Pagamento', auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.tipo} - R${self.valor}'
    
class Pedido(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('cancelado', 'Cancelado'),
    ])

    def __str__(self):
        return f'Pedido #{self.id}  {self.cliente.nome}'


