import os
import sys
import zipfile
import tarfile

itens= []
nome= ''
					
def mover(origem, final):
	cf= os.path.abspath(final)
	cn= os.path.join(cf, origem)
	os.rename(origem, cn)

if sys.argv[1]:
	if len(sys.argv) > 2:
		nome= sys.argv[-1]
		sys.argv.pop()
		partes= os.path.splitext(nome)
		if not os.path.exists(nome):
			print('O arquivo compremido nao existe, criando.')
			for item in sys.argv[1:]:
				if os.path.exists(item):
					print(f'[ {item} ] => existe.')
					itens.append(item)
			else:
				print(f'[ {item} ] => nao existe.')
			print(f'{itens} indo para [ {nome} ] .')
			match partes[1]:
				case '.zip':
					with zipfile.ZipFile(nome, 'w') as zipf:
						for item in itens:
							zipf.write(item)
					print(f'Criado com sucesso, total de itens: {len(itens)} .')
				case '.tar':
					with tarfile.open(nome, 'w') as tarf:
						for item in itens:
							tarf.add(item)
					print(f'Criado com sucesso, total de itens: {len(itens)}')
				case _: print('Sem suporte, criacao encerrada.')
		else: print('O arquivo ja existe.')
	elif len(sys.argv) == 2:#para criar apenas um arquivo compremido vazio
		nome= sys.argv[1]
		if not os.path.exists(nome):
			partes= os.path.splitext(nome)
			match partes[1]:
				case '.zip':
					z= zipfile.ZipFile(nome, 'w')
					print('Arquivo criado.')
				case '.tar':
					t= tarfile.open(nome, 'w')
					print('Arquivo criado.')
				case _: print('Sem suporte para criacao')
		else:
			print('O arquivo ja existe.')
else: print('Voce deve informar pelo menos o nome do novo arquivo compremido.')