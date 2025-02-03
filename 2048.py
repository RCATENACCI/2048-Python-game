import numpy
import matplotlib.pyplot as plt
import time
def creer_jeu(dim):
    return numpy.zeros((dim, dim), dtype=int)

def position_libre(jeu):
    pos = []
    for i in range(jeu.shape[0]):
        for j in range(jeu.shape[1]):
            if jeu[i, j] == 0:
                pos.append((i, j))
    return pos

def nombre_aleatoire(jeu):
    pos = position_libre(jeu)
    if pos!=[]:
        nb = numpy.random.randint(0, 2) * 2 + 2
        i = numpy.random.randint(0, len(pos))
        p = pos[i]
        jeu[p] = nb

def perdu(jeu):
    n=len(position_libre(jeu))
    if n==0:
        return False
    else:
        return True

def perdu2(j):
    if len(position_libre(j))!=0:
        return True
    if len(position_libre(j))==0:
        for i in range(1,len(j)-1):
            for k in range(1,len(j)-1):
                if j[i,k]==j[i,k-1] or j[i,k]==j[i,k+1] or j[i,k]==j[i-1,k] or j[i,k]==j[i+1,k]:
                    return True
        for i in range(1,len(j)):
            if j[0,i]==j[0,i-1] or j[-1,i]==j[-1,i-1] or j[i,0]==j[i-1,0] or j[i,-1]==j[i-1,-1]:
                return True
    return False

def agg(t):
    nn=[a for a in t if a!=0]
    i=len(nn)-1
    while i>0:
        if nn[i]!=0 and nn[i]==nn[i-1]:
            nn[i-1]+=nn[i-1]
            nn[i]=0
            i-=2
        else:
            i-=1
    while len(nn)!=len(t):
        nn.append(0)
    return(nn)


def joueuncoup(t,d):
    for i in range(len(t)):
        if d==0:#haut
            t[:,i]=agg(t[:,i])
        elif d==1 :#droite
            t[i,::-1]=agg(t[i,::-1])
        elif d==2:#bas
            t[::-1,i]=agg(t[::-1,i])
        elif d==3:#gauche
            t[i,:]=agg(t[i,:])
    return t


def score(jeu):
    return(jeu.max())

def direction(jeu):
    d=numpy.random.randint(0,4)
    return(d)

def partie(dim):
    j=creer_jeu(dim)
    while perdu2(j)==True:
        joueuncoup(j,direction(j))
        nombre_aleatoire(j)
    return (j, score(j))


def direction2(jeu):
    v=0
    h=0
    for i in range(len(jeu)):
        for j in range(len(jeu)):
            if i != 0 and j != 0:
                if jeu[i,j]==jeu[i-1,j] :
                    v+=1
                if jeu[i,j]==jeu[i,j-1]:
                    h+=1
            elif i==0 and j!=0 :
                if jeu[i,j]==jeu[i,j-1]:
                    h+=1
            elif i!=0 and j==0 :
                if jeu[i,j]==jeu[i-1,j] :
                    v+=1
    if v <= h :
        return (1+ 2*numpy.random.randint(0,1))

    else:
        return (2*numpy.random.randint(0,1))



def partie2(dim):
    j=creer_jeu(dim)
    while perdu2(j)==True:
        joueuncoup(j,direction2(j))
        nombre_aleatoire2(j)
    return (j, score(j))


def nombre_aleatoire2(jeu):
    pos = position_libre(jeu)
    if pos!=[]:
        b=numpy.random.binomial(1,0.1)
        nb=0
        if b==0:
            nb=2
        else:
            nb=4
        i = numpy.random.randint(0, len(pos))
        p = pos[i]
        jeu[p] = nb



print(j)
##
def meilleure_direction(jeu):
    v=0
    h=0
    for i in range(len(jeu)):
        for j in range(len(jeu)):
            if i != 0 and j != 0:
                if jeu[i,j]==jeu[i-1,j] :
                    v+=1
                if jeu[i,j]==jeu[i,j-1]:
                    h+=1
            elif i==0 and j!=0 :
                if jeu[i,j]==jeu[i,j-1]:
                    h+=1
            elif i!=0 and j==0 :
                if jeu[i,j]==jeu[i-1,j] :
                    v+=1
    if v<=h:
        return([1,h])
    else:
        return([0,v])

def meilleure_direction2(jeu):
    v=0
    h=0
    for i in range(len(jeu)):
        for j in range(len(jeu)):
            if i != 0 and j != 0:
                if jeu[i,j]==jeu[i-1,j] :
                    v+=jeu[i,j]
                if jeu[i,j]==jeu[i,j-1]:
                    h+=jeu[i,j]
            elif i==0 and j!=0 :
                if jeu[i,j]==jeu[i,j-1]:
                    h+=jeu[i,j]
            elif i!=0 and j==0 :
                if jeu[i,j]==jeu[i-1,j] :
                    v+=jeu[i,j]
    if v<=h:
        return([1,h])
    else:
        return([0,v])



def direction_ant1(jeu):
    pj1=jeu.copy()
    pj2=jeu.copy()
    d=0
    if meilleure_direction(jeu)[0]==0 :
        m=meilleure_direction(joueuncoup(pj1,0))[1]
        n=meilleure_direction(joueuncoup(pj2,2))[1]
        if n>=m :
            d=2
        else:
            d=0
    else:
        m=meilleure_direction(joueuncoup(pj1,1))[1]
        n=meilleure_direction(joueuncoup(pj2,3))[1]
        if n>=m :
            d=3
        else:
            d=1
    return(d)

def direction_ant2(jeu):
    pj1=jeu.copy()
    pj2=jeu.copy()
    d=0
    if meilleure_direction(jeu)[0]==0 :
        m=meilleure_direction2(joueuncoup(pj1,0))[1]
        n=meilleure_direction2(joueuncoup(pj2,2))[1]
        if n>=m :
            d=2
        else:
            d=0
    else:
        m=meilleure_direction2(joueuncoup(pj1,1))[1]
        n=meilleure_direction2(joueuncoup(pj2,3))[1]
        if n>=m :
            d=3
        else:
            d=1
    return(d)


def partie3(dim):
    j=creer_jeu(dim)
    while perdu2(j)==True:
        joueuncoup(j,direction_ant1(j))
        nombre_aleatoire2(j)
    return (j, score(j))


def partie4(dim):
    j=creer_jeu(dim)
    while perdu2(j)==True:
        joueuncoup(j,direction_ant2(j))
        nombre_aleatoire2(j)
    return (j, score(j))




print(partie4(4))

#def technique(jeu):






