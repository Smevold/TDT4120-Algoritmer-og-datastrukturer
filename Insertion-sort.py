import numpy as np

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i] # Lagrer verdien midlertidig

        j = i - 1 # Vil sjekke alle verdier til venstre for i
        while (j >= 0 and array[j] > key): 
            array[j+1] = array[j] # Flytter verdien ved j ett hakk til høyre
            j -= 1 

        array[j+1] = key # Setter tilbake den midlertidige verdien



def main():
    arr = np.array([7, 2, 3, 9, 0, 2, 5])

    insertion_sort(arr)

    print(arr)

main()

"""
Insertion sort er bra for små lister, men dårligere for lengre lister.
O(n²)
"""