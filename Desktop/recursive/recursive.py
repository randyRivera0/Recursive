# Author Randy Adley Rivera Bermudez
def substring(string):
    return string[1:-1]


def palindromo(string):
    if string is None:
        return True
    n_len = len(string)
    if n_len>1:
        if string[0]==string[-1]:
            string = substring(string)
            return palindromo(string)
        else: 
            return False
    else:
        return True


def revertir(string):
    if len(string) > 1:
        return string[-1] + revertir(string[:-1])
    else: return string
    

def sumarDigitos(num):

    pass


string = input("Enter string: ")
print(palindromo(string)) 
print(revertir(string)) 
