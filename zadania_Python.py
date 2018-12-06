# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH

def code_generator(first_code, last_code):
    first_code = int(''.join(first_code.split('-')))
    last_code = int(''.join(last_code.split('-')))

    for i in range(first_code, last_code + 1):
        first = i // 1000
        last = i % 1000
        print('{:2}-{:003}'.format(first, last))

if __name__ == '__main__':
    first_code = '79-900'
    last_code = '80-155'
    code_generator(first_code, last_code)

# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE

def miss_elem(elements, n):
    missing_list = []
    for i in range(1, n + 1):
        if i not in elements:
            missing_list.append(i)
    return missing_list

if __name__ == '__main__':
    list = [2, 3, 7, 4, 9]
    n = 10
    print(miss_elem(list, n))


# ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.

import decimal

def list_digits(beginn, end):
    beginn = decimal.Decimal(beginn)
    end = decimal.Decimal(end)
    while beginn < end:
        print(beginn)
        beginn += decimal.Decimal(0.5)
    return beginn

print(list_digits(2, 5.5))