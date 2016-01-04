import sys

import declaracao_de_orientacao
import encaminhamento_de_estagio
import justificativa_de_falta 
import memo
import cancelamento_de_matricula_em_disciplina

op = 4

while op != 0:
	
	print "0 - para sair"
	print "1 - declaracao de orientacao"
	print "2 - memorando"
	print "3 - justificativa de falta\n"

	op = input("Informe a opcao:\n")

	if op == 0:
		
		print "Voce saiu !\n"
		break		
			
	elif op == 1:
		
		declaracao_de_orientacao.cli()

	elif op == 2:
		
		memo.cli()

	elif op == 3:
	
		justificativa_de_falta.cli()

	else:

		print "Opcao invalida, tente 0, 1, 2 ou 3 !"
