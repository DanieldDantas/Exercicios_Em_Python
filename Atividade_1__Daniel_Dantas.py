alunos = []
alunos.append({'nome': 'Aluno 01', 'curso': 'Ciências da Computação', 'AV1':8 })
alunos.append({'nome': 'Aluno 02', 'curso': 'Sistemas de Informação', 'AV1':7 })
alunos.append({'nome': 'Aluno 03', 'curso': 'Sistemas de Informação', 'AV1':6 })
alunos.append({'nome': 'Aluno 04', 'curso': 'Sistemas de Informação', 'AV1':6 })
alunos.append({'nome': 'Aluno 05', 'curso': 'Sistemas de Informação', 'AV1':6 })
notas = []

cc=[]
ads = []
si = []

[cc.append(aluno['AV1']) for aluno in alunos if aluno['curso'] == 'Ciência da computação']
notas = []

for aluno in alunos:
  notas.append(aluno['AV1'])

print('A MAIOR nota é.....:', max(cc))
print('A MENOR nota é.....:', min(cc))
print('A MÉDIA das notas é:', round(sum(cc)/len(cc),2))

