# -*- coding: utf-8 -*-

import pickle
import pathlib


def load_animals(large_dataset=False):
    """

    :param bool large_dataset: Jeśli wartość to True zwraca 1E6 zwierząt, w
                               przeciwnym razie 1E5. Test będzie odbywał się
                               przy 1E6 zwierząt.

    :return: Lista zwierząt
    """
    file_name = 'animals-small.bin' if not large_dataset else 'animals.bin'
    file = pathlib.Path(__file__).parent / file_name
    with open(str(file), 'rb') as f:
        return pickle.load(f)


def filter_animals(animal_list):
    """
    Jesteś informatykiem w firmie Noe Shipping And Handling. Firma ta zajmuje
    się międzykontynentalnym przewozem zwierząt.

    Dostałeś listę zwierząt które są dostępne w pobliskim zoo do transportu.

    Mususz z tej listy wybrać listę zwierząt które zostaną spakowane na statek,

    Lista ta musi spełniać następujące warunki:

    * Docelowa lista zawiera obiekty reprezentujące zwierzęta (tak jak animal_list)
    * Z każdego gatunku zwierząt (z tej listy) musisz wybrać dokładnie dwa
      egzemplarze.
    * Jeden egzemplarz musi być samicą a drugi samcem.
    * Spośród samic i samców wybierasz te o najmniejszej masie.
    * Dane w liście są posortowane względem gatunku a następnie nazwy zwierzęcia

    Wymaganie dla osób aspirujących na ocenę 5:

    * Ilość pamięci zajmowanej przez program musi być stała względem
      ilości elementów w liście zwierząt.
    * Ilość pamięci może rosnąć liniowo z ilością gatunków.

    Nie podaje schematu obiektów w tej liście, musicie radzić sobie sami
    (można podejrzeć zawartość listy w interaktywnej sesji interpretera).

    Do załadowania danych z listy możesz użyć metody `load_animals`.

    :param animal_list:
    """
    animals_d = {}
    mass_units = {'g': 1, 'mg': 0.001, 'kg': 1000, 'Mg':1000000}
    for animal in animal_list:
        akey = animal['genus'],animal['sex']
        if akey not in animals_d:
            animals_d[akey] = animal
        animal_mass = animal['mass'][0]*mass_units[animal['mass'][1]]
        animal_mass_d = animals_d[akey]['mass'][0]*mass_units[animals_d[akey]['mass'][1]]
        if animal_mass < animal_mass_d:
            animals_d[akey] = animal
    
    return list(sorted(animals_d.values(), key=lambda x: (x['genus'], x['name'], -1 if x['sex'][0]=='m' else 1) ))
    


if __name__ == "__main__":
    animals = load_animals()
