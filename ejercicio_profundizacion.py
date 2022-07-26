#EJERCICIO DE PROFUNDIZACIÓN_M4: SQL_Introducción 


import sqlite3
import numpy as np
import matplotlib.pyplot as plt


def fetch():
    conn = sqlite3.connect('heart.db')
    c = conn.cursor()

    pulsos = c.execute('SELECT pulso FROM sensor').fetchall() 
    
    conn.close()

    return pulsos


def show(pulsos):
    figu = plt.figure()
    ax = figu.add_subplot()
    ax.plot(pulsos, color = 'darkcyan', label= r'$PPM$')
    ax.set_facecolor('whitesmoke')
    ax.set_title(r'Curva de ritmo cardíaco', size=18, x=0.5, y=1.02, color='darkred')
    ax.grid(ls ='-.')
    ax.set_xlabel(r'$t$')
    ax.set_ylabel(r'$Pulsaciones$')
    ax.legend()
    plt.show()


def estadistica(pulsos): 
    print(f'Resgitro mínimo de PPM: {np.min(np.array(pulsos))}\n')
    print(f'Registro máximo de PPM: {np.max(np.array(pulsos))}\n')

    print(f'Media aritmética de la muestra: {round(np.mean(np.array(pulsos)),2)}\n')
    print(f'Desvío stándard: {round(np.std(np.array(pulsos)),2)}\n')


def regiones(pulsos):
    med = np.mean(np.array(pulsos))
    destd = np.std(np.array(pulsos))

    x1=[]
    y1=[]
    x2=[]
    y2=[]
    x3=[]
    y3=[]


    for i in range(len(pulsos)):
        if pulsos[i] <= (med-destd):
            x1.append(i)
            y1.append(pulsos[i])

        elif pulsos[i] >= (med+destd):
            x2.append(i)
            y2.append(pulsos[i])

        else:
            x3.append(i)
            y3.append(pulsos[i])


    figu = plt.figure()
    ax = figu.add_subplot()
    ax.set_facecolor('snow')
    ax.set_title(r'Ritmo cardíaco', size=18, x=0.5, y=1.02, color='navy')
    ax.grid(ls ='--')
    ax.scatter(x1,y1,color='dimgray', marker='.', label= r'$\leq$ mean-std')
    ax.scatter(x2,y2,color='tomato', marker='.', label= r'$\geq$ mean+std')
    ax.scatter(x3,y3,color='cadetblue', marker='.', label= r'$normal$')
    ax.set_xlabel(r'$t$')
    ax.set_ylabel(r'$Pulsaciones$')

    ax.legend()
    plt.show()


if __name__=="__main__":
    # Leer la DB
    pulsos = fetch()

    # Data analytics
    show(pulsos)
    estadistica(pulsos)
    regiones(pulsos)