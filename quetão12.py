carrosVendidos=float(input("Digite a quantidade de carros vendidos: "))
valorTotalVendas=float(input("Digite o valor total de vendas: "))
salarioFixo= float(input("Digite o salario fixo: "))
comissao=float(input("Digite o valor da comissão: "))
salarioFinal= salarioFixo + comissao*carrosVendidos + (5*valorTotalVendas)/100
print("O salario final será: " +str(salarioFinal))