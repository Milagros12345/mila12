from random import*
from time import*
from turtle import*
def seleccion(lista):
  for i in range(0,len(lista)-1):
    mini = i
    for j in range(i+1,len(lista)):
      if lista[j]<lista[mini]:
        mini=j
    
    if mini != i: 
        c=lista[i]
        lista[i]=lista[mini]
        lista[mini]=c
        dibujar(l0)
        sleep(0.2)
  return lista
def dibujar (l):
    hideturtle()
    tracer(0,0)
    clear ()
    x= -200
    for i in range(0,len(l)):
        penup()
        goto(x,0)
        pendown()
        goto(x,l[i])
        x+=5
    update()
def insertion(lista):
  for i in range(1,len(lista)):
    x=lista[i]
    j=i
    while j>0 and lista[j-1]>x:
      lista[j]=lista[j-1]
      dibujar(lista)
      j-=1
    lista[j]=x
    sleep(0.02)
  return lista
def burbuja(lista):
  n=len(lista)
  cambio=True
  while cambio:
    cambio=False
    for i in range(0,n-1):
      if lista[i]>lista[i+1]:
        c=lista[i]
        lista[i]=lista[i+1]
        lista[i+1]=c
        dibujar(lista)
        cambio=True
    n=n-1
    sleep(0.2)
     
  return lista
def particion(l,primero,ultimo):
    indexPivote=primero
    valorPivote=l[indexPivote]
    l[indexPivote],l[ultimo]=l[ultimo],l[indexPivote]
    index=primero
    for i in range(primero, ultimo):
        if l[i] < valorPivote:
            l[i],l[index]=l[index],l[i]
            index+=1
    l[index],l[ultimo]=l[ultimo],l[index]
    sleep(0.2)

    
    return index
def quicksort(l,inicio, fin):
  if fin > inicio:
    index = particion(l,inicio,fin)
    quicksort(l,inicio,index-1)
    quicksort(l,index+1,fin)
def ordenar(lista):
  quicksort(lista,0,len(lista)-1)
  dibujar(lista)
def OrdenxMezcla(L):
  if len(L) < 2:
    return L

  mitad=len(L)//2
  left = OrdenxMezcla(L[:mitad])
  right = OrdenxMezcla(L[mitad:])
  res=mezcla(left,right)
  dibujar(res)
  sleep(0.10)
    
  return res

def mezcla(l1,l2):
  l3 = []
  while len(l1)!=0 and len(l2)!=0:
    if l1[0]>l2[0]:
      l3.append(l2.pop(0))
    else:
      l3.append(l1.pop(0)) 
  return l3+ l1 + l2
l=[]
for i in range(0,100):
    l.append(i)
start_time = time()
OrdenxMezcla(l)
end_time = time() - start_time
print "demoro: ", end_time






