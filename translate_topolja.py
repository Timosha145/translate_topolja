from module1 import *

rus=[]
eng=[]
rus=loef('rus.txt',rus)
print(rus)
eng=loef('eng.txt',eng)
print(eng)

print("--------------------------------------Добро пожаловаться в Python Translate!--------------------------------------------")
while True:
    language=input("С какого на какой язык вы хотите выполнить перевод?\nДобавить новое слово - Y\nУвидеть список слов - N\nПросто перевести - T\nНашел ошибку - V\nПроговорить слово - R\nТест на знание слов - Z\nЗакончить - E\nВыбери вариант: ")
    print()
    if language.upper()=="Y":
        rus=newWord("rus.txt", input("Новое слово: "))
        eng=newWord("eng.txt", input("Перевод слова: "))
    elif language.upper()=="N":
        print(rus)
        print(eng)
    elif language.upper()=="T":
        translate(rus,eng)

    elif language.upper()=="V":
        error(rus,"rus.txt", eng,"eng.txt")

    elif language.upper()=="R":
        lang=input("На каком языке проговорить?: ")
        word=input("Слово: ")
        heli(word,lang)
    elif language.upper()=="R":
        lang=input("На каком языке проговорить?: ")
        word=input("Слово: ")
        heli(word,lang)
    elif language.upper()=="Z":
        test(rus, eng)
    elif language.upper()=="E":
        print('Head Aega!')
        break