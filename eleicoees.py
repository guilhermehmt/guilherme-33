documento = int(input('''Digite 1 para RG ou 2 para titulo:'''))   
if documento == 1:
    rg = int(input("Digite o numero do RG:"))
    if rg == 12345678:
        print("joão do carmo, Pode votar!")
    else:
        print("eleitor não encontrado")
    
elif documento == 2:
   titulo = int(input("Digite o Titulo do eleitor:"))
   if titulo == 11122233344:
       print("João do Carmo pode votar!")
else:
    print("Eleitor não encontrado.")
    
candidatos = print('''
Candidaro 1 - Paulo Freire
Candidato 2 - Jean Piaget ''') 
voto = int(input('''Digite seu voto: 10 para Paulo Freire 
20 para Jean Piaget:'''))

if voto == 10:
    print("Paulo freire") 
    print("Candidato a presidente")

if voto == 20:
    print("Jean Piaget")
    print("candidato a presidente")
    
    
candidato1 = 0
candidato2 = 0

print('''Paulo freire 
Jean Piaget''')

voto = int(input("Digite seu voto:"))

if voto == 10:
   candidato1 =+ 1
    
if voto == 20:
   candidato2 =+ 1
   
print(f'A soma dos votos de Paulo Freire é de:{candidato1} A soma dos votos de Jean Piaget é de:{candidato2}' )