#Autor: André Luiz Fernandes dos Santos
#Contato: andresantosbr@gmail.com
#Data: 23/04/2019

#Este script foi desenvolvido em Python 3.7.3, sua finalidade é pegar uma lista de domínios e subdomínios
#

import tldextract

#lê arquivo com as ACLs
file_acl_desorganizada = open("arquivo.txt", "r")
lista_subdominios = file_acl_desorganizada.readlines()

lista_dominios = []

#mantém apenas os domíniosde uma URL ou subdomínio
for item in lista_subdominios:
	lista_dominios.append(tldextract.extract(item.rstrip()).registered_domain)

#remove redundâncias
lista_dominios = list(dict.fromkeys(lista_dominios))

#escreve num arquivo a nova lista de ACLs
with open('acl_organizada.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(lista_dominios))

file_acl_desorganizada.close()