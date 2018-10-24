#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


def getLinks (url): #Como en el ejercicio anterior, la funcion obtiene los links de una URL
    req = requests.get(url)
    bs = BeautifulSoup(req.content, 'lxml')
    tempLinks = bs.find_all('a')
    links = []
    
    for link in tempLinks:
        try:
            if link.attrs['href'][:4] == 'http':
                links.append(link.attrs['href'])
        except:
            pass

    return links

def printLinks (url, i, n): # En este ejercicio hemos modificado la funcion para imprimir los links
                            # en el formato requerido
    links = getLinks(url)
    for link in links:
        print('  '*i + '--- ' + link)
        if i < n:
            try:
                printLinks(link, i+1, n) # Para imprimir los links en funcion de n usamos una funcion recursiva
            except:
                pass
        elif i >= n:
            pass



def main ():
    url = input('Introduzca una URL: ')
    try: # Con el try nos aseguramos que el se ha introducido un entero
        n = int(input('Introduzca el numero de iteraciones: '))
    except ValueError:
        print('No ha introducido un numero')
    try: # En este try nos aseguramos que la url es valida
        _checkurl = getLinks(url)
    except:
        print('La URL introducida no es valida, asegurese que el formato es \'http://........\'')
        return 0
    printLinks(url, 0, n)
    
    input('Pulse cualquier tecla para finalizar...')


if __name__ == '__main__':
    main()
