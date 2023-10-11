#BUSCAR COMO GENERAR UN VECTOR DE PERMUTACIÓN EN PYTHOn
## de longitud completa
import itertools

if __name__ == '__main__':
    nums = [1, 2, 3]

    permutations = list(itertools.permutations(nums))
    print(permutations)
#Generar sucesivos r permutaciones de longitud
import itertools

if __name__ == '__main__':
    nums = [1, 2, 3]
    r = 2

    permutations = list(itertools.permutations(nums, r))
    print(permutations)