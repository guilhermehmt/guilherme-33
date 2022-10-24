documento = int(input('''Digite 1 para RG ou 2 para titulo''')
if documento == 1:
    numero = int(input("Digite o numero do RG"))
    if numero == 12345678:
        print("joão do carmo, Pode votar!")
    else:
    print("eleitor não encontrado.")
    
elif documento == 2:
   numero = int(input("Digite o Titulo do eleitor:"))
   if numero == 11122233344:
       print("João do Carmo pode votar!")
       
   else:
       print("Eleitor não encontrado.")
       
    
    
                   