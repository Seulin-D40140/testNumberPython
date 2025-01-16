#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def numbers(n):
    if n < 0:
        if n % 2 ==0:
            return "pair and negativ number"
        else:
            return "unpair and negativ number"
    elif n > 0 :
        if n % 2 ==0:
            return "pair and positive number"
        else:
            return "unpair and positive number"
    else:
        return "number is zero"


if __name__ == '__main__':
    args = sys.argv[1:]
    if args:
        try:
            for num in args:
                integerCast = int(num)
                result = numbers(integerCast)
                print(f"Le nombre {num} est {result}.")
        except ValueError:
            print("ceci n'est pas correcte ressayer ! ")
    else:
        try:
            nb = int(input("Entrer un nombre entier positif : "))
            fact_nb = numbers(nb)
            print(f"Le nombre {nb} est {fact_nb}.")
        except ValueError:
            print("ceci n'est pas correcte ressayer ! ")