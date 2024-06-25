##Desenvolvido por:
#Felipe Lorusso,        felipelorusso@alunos.utfpr.edu.br
#Murilo F. Muniz,       murilo.2022@alunos.utfpr.edu.br

import os
import sys

def abrirarquivo():
    file = "input.txt"
    with open(file, 'r', encoding='utf8') as f:
        lines = f.readline().strip()
    
    paginas = list(lines)
    return(paginas)

##def printAcesso(s, )

def algoritmoLRU(paginas, n, capacidade):
    s = set()
    indices = {}

    page_foults = 0
    pf = False

    for i in range(n):
        pf = False
        if len(s) < capacidade:

            if paginas[i] not in s:
                s.add(paginas[i])

                page_foults += 1
                pf = True

            indices[paginas[i]] = i

        else:
            if paginas[i] not in s:
                lru = float('inf')

                for pagina in s:
                    if indices[pagina] < lru:
                        lru = indices[pagina]
                        valor = pagina
                
                s.remove(valor)

                s.add(paginas[i])

                page_foults += 1
                pf = True
            indices[paginas[i]] = i

        if pf == True:
            print(f"{i}:\t{paginas[i]} | {s}\tPAGE FOULT")
        else:
            print(f"{i}:\t{paginas[i]} | {s}\t\t")
    
    print(f"\ntotal page foults: {page_foults}")
        
    return page_foults


def main():
    
    paginas = abrirarquivo()
    #print(paginas)
    qtd_paginas = len(paginas)
    
    print("RAM 3 pg\n")
    print("TEMPO\tPG\tRAM\t\tPG_F")
    nmro_pg_foults_3 = algoritmoLRU(paginas, qtd_paginas, 3)
    print("\nRAM 4 pg\n")
    print("TEMPO\tPG\tRAM\t\tPG_F")
    nmro_pg_foults_4 = algoritmoLRU(paginas, qtd_paginas, 4)

    print(f"\n\nRESULTADOS:\n\tRAM 3 Slots: {nmro_pg_foults_3} page foults\n\tRAM 4 Slots: {nmro_pg_foults_4} page foults")


if __name__ == "__main__":
    main()

