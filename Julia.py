import pyautogui
import time
from datetime import datetime

lista = []
arq = open('authans.txt','r')
for linha in arq:
	linha = linha.rstrip()
	linha = linha.split()
	lista.append(linha)

valor = len(lista)
x = 1
while x != valor:
	y = 0
	#Empresa
	time.sleep(5)
	a = lista[x][y]
	pyautogui.typewrite(a)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	#Sucursal
	b = lista[x][y]
	pyautogui.typewrite(b)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	#Produto
	c = lista[x][y]
	pyautogui.typewrite(c)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	#Proposta
	d = lista[x][y]
	pyautogui.typewrite(d)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	y = y + 1
	#Operacao
	e = lista[x][y]
	pyautogui.typewrite(e)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	y = y + 1
	#Receb(Data Atual)
	f = datetime.today().strftime('%d%m%Y')
	pyautogui.typewrite(f)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	#TipoPessoa
	g = lista[x][y]
	pyautogui.typewrite(g)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	#CPF/CNPJ
	h = lista[x][y]
	pyautogui.typewrite(h)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	y = y + 1
	#Nome
	i = lista[x][y]
	pyautogui.typewrite(i)
	time.sleep(6)
	pyautogui.hotkey('enter')
	y = y + 1
	#RG
	j = '123456789'
	pyautogui.typewrite(j)
	time.sleep(6)
	pyautogui.hotkey('enter')
	#Orgão Emissor
	k = 'SSP'
	pyautogui.typewrite(k)
	time.sleep(6)
	pyautogui.hotkey('enter')
	#DtEmissão
	l = '01011990'
	pyautogui.typewrite(l)
	time.sleep(6)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.moveTo(573, 688)  #Teclado Virtual
	time.sleep(2)
	pyautogui.click(clicks=1, interval=0.5)
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	#Estipulante
	m = '001111998855228888'
	pyautogui.typewrite(m)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	#CodUnidade
	n = '1'
	pyautogui.typewrite(n)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.moveTo(608, 691)  #Teclado Virtual
	time.sleep(2)
	pyautogui.click(clicks=9, interval=0.5)
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.typewrite(n)
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(3)
	#CEP
	o = lista[x][y]
	pyautogui.typewrite(o)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	y = y + 1
	time.sleep(2)
	#Numero
	p = lista[x][y]
	pyautogui.typewrite(p)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	time.sleep(2)
	#Complemento
	q = lista[x][y]
	pyautogui.typewrite(q)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	y = y + 1
	'''
	r = 'S'
	pyautogui.typewrite(r)
	time.sleep(5)
	pyautogui.hotkey('enter')
	'''
	#Telefone
	s = lista[x][y]
	pyautogui.typewrite(s)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	time.sleep(3)
	#Data de Nascimento
	t = lista[x][y]
	pyautogui.typewrite(t)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	y = y + 1
	#Email
	u = lista[x][y]
	pyautogui.typewrite(u)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	#Telefone Celular
	pyautogui.typewrite(s)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.typewrite('S')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	#FinalVigencia
	v = lista[x][y]
	pyautogui.typewrite(v)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.moveTo(608, 691)  #Teclado Virtual
	time.sleep(2)
	pyautogui.click(clicks=2, interval=0.25)
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	y = y + 1
	#Forma de Pagamento
	pyautogui.typewrite('7')
	time.sleep(5)
	pyautogui.hotkey('enter')
	#Parcelas
	pyautogui.typewrite('01')
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	#Retirar o C
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.moveTo(1061, 633)  #Teclado Virtual delete
	time.sleep(2)
	pyautogui.click(clicks=1, interval=0.25) 
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.typewrite('S') 
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.moveTo(842, 518)  #Teclado Virtual
	time.sleep(2)
	pyautogui.click(clicks=1, interval=0.25)
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.moveTo(842, 518)  #Teclado Virtual
	time.sleep(2)
	pyautogui.click(clicks=1, interval=0.25)
	time.sleep(2)
	#Numero do Item
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.typewrite('1')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.typewrite('00')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.moveTo(608, 691)  #Teclado Virtual
	time.sleep(2)
	pyautogui.click(clicks=2, interval=0.25)
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	#Marca/Tipo
	w = lista[x][y]
	pyautogui.typewrite(w)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	y = y + 1
	#Fab/Modelo
	xx = lista[x][y]
	pyautogui.typewrite(xx)
	time.sleep(5)
	pyautogui.hotkey('enter')
	pyautogui.typewrite(xx)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	#Zero KM
	yy = lista[x][y]
	pyautogui.typewrite(yy)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	#Placa
	z = lista[x][y]
	pyautogui.typewrite(z)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	#UF
	aa = lista[x][y]
	pyautogui.typewrite(aa)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	#Renavam
	time.sleep(2)
	pyautogui.hotkey('enter')
	#Chassi
	bb = lista[x][y]
	pyautogui.typewrite(bb)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	#Combustivel
	cc = lista[x][y]
	pyautogui.typewrite(cc)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	y = y + 1
	#CEP circulação
	pyautogui.typewrite(o)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	#CEP pernoite
	pyautogui.typewrite(o)
	time.sleep(5)
	pyautogui.hotkey('enter')
	#Cobertura
	dd = lista[x][y]
	pyautogui.typewrite(dd)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	#Franquia
	ee = lista[x][y]
	pyautogui.typewrite(ee)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	#Protecao
	pyautogui.typewrite('057')	
	time.sleep(2)
	pyautogui.hotkey('enter')
	pyautogui.moveTo(653, 698)  #Teclado Virtual
	time.sleep(2)
	pyautogui.click(clicks=1, interval=0.25)
	time.sleep(2)
	y = y + 1
	pyautogui.typewrite('057')
	time.sleep(5)
	pyautogui.moveTo(619, 680)  #Teclado Virtual
	time.sleep(2)
	pyautogui.click(clicks=1, interval=0.25) 
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	#CIA Anterior
	ff = lista[x][y]
	pyautogui.typewrite(ff)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	#Apolice Anterior
	gg = lista[x][y]
	pyautogui.typewrite(gg)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.typewrite(gg)
	time.sleep(2)
	pyautogui.hotkey('enter')
	y = y + 1
	#CI Congenere
	hh = lista[x][y]
	pyautogui.typewrite(hh)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	#Com Perfil 
	ii = lista[x][y]
	pyautogui.typewrite(ii)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.moveTo(69, 476)  #Teclado Virtual
	time.sleep(2)
	pyautogui.click(clicks=1, interval=0.25) 
	time.sleep(2)
	pyautogui.typewrite('s')
	time.sleep(2)
	pyautogui.hotkey('enter')
	y = y + 1
	#Nome do Condutor
	jj = lista[x][y]
	pyautogui.typewrite(jj)
	time.sleep(5)
	pyautogui.hotkey('enter')
	y = y + 1
	#Dt Nascimento Condutor
	kk = lista[x][y]
	pyautogui.typewrite(kk)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(5)
	y = y + 1
	#Sexo 
	ll = lista[x][y]
	pyautogui.typewrite(ll, interval=0.5)
	time.sleep(8)
	pyautogui.hotkey('enter')
	time.sleep(3)
	pyautogui.hotkey('enter')
	y = y + 1
	#Estado Civil
	mm = lista[x][y]
	pyautogui.typewrite(mm, interval=0.25)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(3)
	pyautogui.hotkey('enter')
	y = y + 1
	#Tempo Habilitação
	nn = lista[x][y]
	pyautogui.typewrite(nn, interval=0.25)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(3)
	pyautogui.hotkey('enter')
	y = y + 1
	pyautogui.moveTo(72, 693)  #Teclado Virtual F5
	time.sleep(3)
	pyautogui.click(clicks=1, interval=0.25)
	pyautogui.moveTo(332, 469)  #Teclado Virtual F5
	time.sleep(3)
	pyautogui.click(clicks=1, interval=0.25)
	time.sleep(5)
	#Residente Dependente -- Parei aqui
	oo = lista[x][y]
	pyautogui.typewrite(oo, interval=0.25)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(3)
	pyautogui.hotkey('enter')
	#y = y + 1
	#Guarda Veiculo
	pp = lista[x][y]
	pyautogui.typewrite(pp, interval=0.25)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(3)
	pyautogui.hotkey('enter')
	y = y + 1
	#Utilização Veiculo
	qq = lista[x][y]
	pyautogui.typewrite(qq, interval=0.25)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(3)
	pyautogui.hotkey('enter')
	y = y + 1
	zz = lista[x][y]
	pyautogui.typewrite(zz, interval=0.25)
	time.sleep(5)
	pyautogui.hotkey('enter')
	time.sleep(3)
	pyautogui.hotkey('enter')
	y = y + 1
	#pyautogui.moveTo(72, 693)  #Teclado Virtual F5
	#time.sleep(2)
	#pyautogui.click(clicks=1, interval=0.25)
	#pyautogui.moveTo(332, 469)  #Teclado Virtual F5
	#time.sleep(2)
	#pyautogui.click(clicks=1, interval=0.25)
	time.sleep(2)
	pyautogui.moveTo(839, 535)  #Teclado Virtual F5
	time.sleep(2)
	pyautogui.click(clicks=2, interval=0.5)
	time.sleep(2)
	pyautogui.typewrite('1')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(4)
	#Cobertura Adicional
	rr = lista[x][y]
	pyautogui.typewrite(rr)
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.moveTo(617, 695)  #Teclado Virtual F5
	time.sleep(2)
	pyautogui.click(clicks=1, interval=0.5)
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(2)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.hotkey('enter')
	time.sleep(4)
	pyautogui.moveTo(73, 695)  #Teclado Virtual
	time.sleep(2)
	pyautogui.click(clicks=1, interval=0.25)
	time.sleep(2)
	pyautogui.moveTo(638, 486)  #Teclado Virtual
	time.sleep(2)
	pyautogui.click(clicks=1, interval=0.25)
	time.sleep(2)
	x = x + 1


 #Ultimo codigo para retornar o looping
#print(pyautogui.position())
#pyautogui.click(450,450);pyautogui.typewrite('graphicsnotes');pyautogui.press('enter')
