TM = float(input("Informe o tempo de viagem em horas: "))
VM = float(input("Informe a velocidade média em km/h: "))
CM = float(input("Informe qual foi o consumo médio em litros: "))
PG = float(input("Informe o preço da gasolina em reais: "))

DP = round(TM * VM, 2)
GS = round(DP / CM, 2)
VL = round(GS * PG, 2)

print("Você percorreu uma distância de", DP, "km em sua viagem")
print("A quantidade de combustível gasta na viagem foi de", GS, "litros")
print("Você gastou R$", VL, "de gasolina em sua viagem")
