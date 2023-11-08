# 1
def slovnik(language, word):

    my_dictionary = {'cz': ['já', 'slovo', 'rok', 'červený', 'krasný'], 
                    'eng': ['I', 'word', 'year', 'red', 'beautiful'], 
                    'it': ['io', 'parola', 'anno', 'rosso', 'bello']}
    
    idx = my_dictionary.get(language).index(word) 
    
    res = [key + ': ' + value[idx] for key, value in my_dictionary.items() if key != language]
    
    return '; '.join(res)

#print(slovnik('eng', 'beautiful'))

# 2
def poradnik_na_feldu(people):
    people = list(i for i in people.split(','))
    
    while True:
        person, operation = input('Zadejte osobu: '), input('Co bych měl udělat? ')
        
        if operation == 'insert':
            people.append(person)
            print('Tady máš:', *people, sep=' ') 
        
        elif operation == 'delete':
            if person in people:
                people.remove(person)
                print('Tady máš:', *people, sep=' ') 
            else:
                print('Taková osoba není. Zkus znova.')
        
        elif operation == 'rank':
            print('Pořadí osoby je', people.index(person) + 1)
        
        #elif operation == 'stop':
            #break
        else:
            print('Nevím, co chceš. Zkus znova.')
        
#poradnik_na_feldu('osoba1,osoba2,osoba3')

# 3
from random import randint

def pocitadlo():
    res, counter = set(), 0
    while len(res) < 6:
        res.add(randint(1, 6))
        counter += 1
    return counter

#print(pocitadlo())

# 4
def seznam_cisel(numbers):
    numbers = tuple(int(i) for i in numbers.split())
    
    while True:
        operation = input('Co bych měl udělat? ')
        if operation == 'insert':
            numbers += tuple(input('Zadej čislo: '))
            print(numbers)
        elif operation == 'count':
            print(len(numbers))
        #elif operation == 'stop':
            #break

seznam_cisel('1 2 3 4 5 6 7')

