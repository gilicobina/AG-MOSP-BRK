
# -*- Coding: UTF-8 -*-
#coding: utf-8
from Dado import Dados
from sys import argv
import numpy as np
from BRKGA import BRKGA
import glob	

#Tamanho da populacao
TAM_POP = 100
#Criterio de parada
MAX_GEN = 1000
#Taxa da populacao que estara na populacao elite
TX_ELITE = 0.6
#Taxa de cruzamento(Probabilidade de um filho herdar o gene do seu pai de elite)
TX_CROSS = 0.6
#Taxa de mutacao(Numero de mutantes criados)
TX_MUT = 0.13


'''
Para executar o programa, 'python nomedoarquivo.py nome_do_arquivo 0' para os que nao sao np e
'python nomedoarquivo.py nome_do_arquivo 1' para os que sao np
'''
#dados = Dados('../dados_atribuicao/'+argv[1], argv[2])
#dados = Dados('../dados_atribuicao/assign4.txt')
x = '/home/mateus/Documentos/algoritmos de otimizacao/MOSP/ChallengeInstances2005/trial/'
sol = '/home/mateus/Documentos/algoritmos de otimizacao/MOSP/ChallengeInstances2005/solucao/'
#dados = Dados('trial/'+argv[1])

listaArq = glob.glob(x+'*.txt')

for arq in listaArq:
	for i in range(10):
		print arq
		dados = Dados(arq)
		matriz = np.array(dados.matriz)
		

		atribuicao = BRKGA(dados, TAM_POP,MAX_GEN, TX_CROSS, TX_MUT, TX_ELITE)
		atribuicao.start()
		atribuicao.join()
		salve = arq.replace(x,'')
		salve = salve.replace('.txt','')

		with open(sol+salve+'_solu.csv','a') as z: 
			z.write(str(atribuicao.solucao))
			z.write('\n')
		z.close()
print('Solucao '+ str(atribuicao.solucao))


