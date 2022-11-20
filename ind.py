#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def first_n(type = 0):
    print("Введите стороны фигуры: ")
    a = int(input())
    b = int(input())

    print("Вы знаете, какая фигура нужна?\n" + "введите y или n")
    agr = str(input())
    if agr == "y":
        print("Треугольник или квадрат?\n" + "Введите 0, если треугольник и 1, если квадрат...")
        type = int(input())        
    else:
        print("...")
        
    def second_n(a, b):
        
        if type == 0:
            return(0.5 * a * b)
        else:
            return(a * b)
    return second_n(a, b)


if __name__ == '__main__':
    
    y = first_n()
    print(y)


