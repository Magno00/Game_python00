# Andamento do ciclista

# Entrada de dados
s_km=input("qual a distância?")
s_h=input("quanto tempo?")
km=int(s_km)
h=int(s_h)

# Calculo da velocidade
velocidade = km/h

# Saída de dados
print("velocidade:", velocidade)
if velocidade > 40:
    print("ciclista rápido")
elif velocidade > 10 or velocidade <=40:
    print("moderado")
elif velocidade <= 10:
    print("ciclista lento ")
