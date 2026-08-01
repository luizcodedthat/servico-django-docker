from django.shortcuts import render
import random

def catalogo_produtos(request):
    produtos = [
        {"nome": "Cadeira Gamer", "preco": "R$ 899,90"},
        {"nome": "Fone Bluetooth", "preco": "R$ 199,90"},
        {"nome": "Teclado Mecânico", "preco": "R$ 349,90"},
        {"nome": "Mouse sem Fio", "preco": "R$ 89,90"},
        {"nome": "Monitor 24\"", "preco": "R$ 749,90"},
        {"nome": "Webcam Full HD", "preco": "R$ 159,90"},
    ]

    for produto in produtos:
        seed = random.randint(1, 1000)
        produto["imagem"] = f"https://picsum.photos/seed/{seed}/400/300"

    return render(request, "catalogo.html", {"produtos": produtos})