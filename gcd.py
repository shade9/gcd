#Copyright 2014 Jonathan de la Rosa Gonzalez
import math
def gcd(a, b):
    if (a <= 0) or (b <= 0): 
        print "only positive numbers, please" 
        return 0
    if a > b: return gcd(a-b, b)
    elif a < b: return gcd(a, b-a);
    elif a == b: return a
    
print gcd(54, 24)
print gcd(24, 54)
print gcd(54, -24)
print gcd(0, 17)

factores = []
def factors(x):
    factores.append(x) #el mismo es su factor
    factores.append(1) #1 siempre es factor
    limite = int(math.sqrt(x)) #calculamos hasta aqui ya que en cierto momento el factor A toma un valor que antes era de B, y viceversa
    for f in range(limite, 1, -1): #limite > 1, es recorrido negativo, -1 es saltos negativos
        n = x/float(f)
        if n % 1 == 0: #si es entero
            factores.append(n)
            factores.append(int(x/n)) #tambien el denominador f es factor

factors(547) #adivine este numero primo, y aqui una curiosidad http://primes.utm.edu/curios/page.php/547.html
print sorted(factores)
