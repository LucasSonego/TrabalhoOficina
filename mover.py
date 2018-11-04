#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Mover personagem '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (700, 700)
tela = criar_tela_base(LARGURA, ALTURA)

'''Imagens'''
MAPA = carregar_imagem('./Imagens/mapa.png')
PERSONAGEM = carregar_imagem('./Imagens/fantasma.png')
PASSARALHO = carregar_imagem('./Imagens/passaralho.png')
TIRO = carregar_imagem('./Imagens/naosei.png')

#Criar/carregar imagens:
IMG_PERSONAGEM = carregar_imagem("Imagens/fantasma.png")
IMG_PERSONAGEM = definir_dimensoes(IMG_PERSONAGEM, 60, 80)

MAPA = definir_dimensoes(MAPA,LARGURA,ALTURA)
PERSONAGEM = definir_dimensoes(PERSONAGEM,55,80)
PASSARALHO = definir_dimensoes(PASSARALHO,80,80)
TIRO = definir_dimensoes(TIRO,60,14)

LIMITE_ESQUERDO = 0 + largura_imagem(PERSONAGEM) // 2
LIMITE_DIREITO = LARGURA - (largura_imagem(PERSONAGEM) // 2)
LIMITE_CIMA = 0 + altura_imagem(PERSONAGEM) // 2
LIMITE_BAIXO = ALTURA - (altura_imagem(PERSONAGEM) // 2)


VEL_PERSONAGEM = 5
'''==================='''
'''# Definições de dados: '''

Personagem = definir_estrutura("Personagem", "x, y, dx, dy")
''' Personagem pode ser formado por: Personagem(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[LIMITE_CIMA, LIMITE_BAIXO], Int, Int 
Rep. a posicao do eixo x e y e as velocidades do personagem
'''

'''===================='''
''' Funções: '''

'''
tock: Personagem -> Personagem
Produz o próximo Personagem'''

def mover_perso(per):
    posicao_x = per.x + per.dx
    posicao_y = per.y + per.dy
    if posicao_x > LIMITE_DIREITO or posicao_x < LIMITE_ESQUERDO:
        return Personagem(per.x, per.y, per.dx, per.dy)
    if posicao_y < LIMITE_CIMA or posicao_y > LIMITE_BAIXO:
        return Personagem(per.x, per.y, per.dx, per.dy)
    return Personagem(posicao_x, posicao_y, per.dx, per.dy)

'''
desenha: Personagem -> Imagem
Desenha...'''

def desenha(per):
    colocar_imagem(MAPA,tela,LARGURA//2,ALTURA//2)
    colocar_imagem(TIRO, tela, 400, 200)
    colocar_imagem(PASSARALHO, tela, 600, 200)
    colocar_imagem(PERSONAGEM, tela, per.x, per.y)


'''
trata_tecla: Personagem, Tecla -> Personagem
Conforme aperta as teclas de movimento muda o dx e dy do personagem'''

def trata_tecla(per, tecla):
    if tecla == pg.K_w:
        return Personagem(per.x, per.y, 0, -VEL_PERSONAGEM)
    if tecla == pg.K_a:
        return Personagem(per.x, per.y, -VEL_PERSONAGEM, 0)
    if tecla == pg.K_s:
        return Personagem(per.x, per.y, 0, VEL_PERSONAGEM)
    if tecla == pg.K_d:
        return Personagem(per.x, per.y, VEL_PERSONAGEM, 0)
    return per

'''
trata_tecla: Personagem, Tecla -> Personagem
Conforme aperta as teclas de movimento muda o dx e dy do personagem'''

def trata_solta(per,tecla):
    if tecla == pg.K_w:
        return Personagem(per.x, per.y, per.dx, 0)
    if tecla == pg.K_a:
        return Personagem(per.x, per.y, 0, per.dy)
    if tecla == pg.K_s:
        return Personagem(per.x, per.y, per.dx, 0)
    if tecla == pg.K_d:
        return Personagem(per.x, per.y, 0, per.dy)
    return per



''' ================= '''
''' Main (Big Bang):
'''

''' EstadoMundo -> EstadoMundo '''
''' inicie o mundo com ... '''
def main(inic):
    big_bang(inic, tela=tela, frequencia=50, a_cada_tick=mover_perso,desenhar=desenha, quando_tecla=trata_tecla,quando_solta_tecla=trata_solta, modo_debug=True)

main(Personagem(100, 100, 0, 0))

