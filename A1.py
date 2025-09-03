#Implementera Insättningssortering (Insertionsort)
#Implementera Urvalssortering (Selectionsort)
#Implementera Linjärsökning (Linear search)
#Implementera Binärsökning (Binary search)
#Allt som går att göra iterativt kan man också göra rekursivt. Implementera sökalgoritmerna du gjort ovan som rekursiva varianter om du gjort dem som iterativa, och vice versa.

def linear_search(lst, element):
    for i in range (len(lst)):
        if i == element:
            return i
    return -1

def insertionsort(lst):
    '''
        Implementera en iterativ insertionsort.
    '''
    pass

def selectionsort(lst):
    '''
        Implementera en iterativ selectionsort.
    '''
    pass

def binary_search(lst, element):
    '''
        Implementera en iterativ binärsökning.
    '''
    pass

def binary_search_recursive(lst, element):
    '''
        Implementera en rekursiv binärsökning.
        Gör detta m.h.a. en hjälpfunktion som hanterar och utför rekursionen.
    '''
    pass

def insertionsort_with_binary_search(lst):
    '''
        Implementera en iterativ insertionsort där du söker efter rätt plats att lägga in elementet m.h.a. binärsökning.
    '''
    pass

def linear_search_recursive(lst, element):
    '''
        Implementera en rekursiv linjärsökning.
        Gör detta m.h.a. en hjälpfunktion som hanterar och utför rekursionen.
    '''
    pass 

if __name__ == "__main__":
    lst= [1,2,3,4,5]
    x = linear_search(lst,3)
    print(x)

