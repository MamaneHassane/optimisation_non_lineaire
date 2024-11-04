import numpy as np

# Retourner une matrice
def matrice(*vecteurs):
    return np.array(vecteurs)

# Calculer la transposée d'une matrice
def transposee(matrice):
    return matrice.T

# Calculer l'inverse d'une matrice
def inverse(matrice):
    return np.linalg.inv(matrice)

# Tester les fonctions
if __name__ == "__main__":
    A = matrice([1,2,-2],[3,7,8])
    print(A)