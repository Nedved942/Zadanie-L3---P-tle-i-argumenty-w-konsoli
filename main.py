print("\n*** Pętle i argumenty w konsoli ***\n")

while True:
    elements_to_send = input("Podaj liczbę elementów do wysłania: ")
    try:
        elements_to_send = int(elements_to_send)
    except ValueError:
        print("Podana wartość musi być liczbą całkowitą.")
        continue
    if elements_to_send < 0:
        print("Podana wartość musi być liczbą dodatnią całkowitą.")
        continue
    break

weight_element = None
total_weight = 0
weight_single_package = 0
packages = 1
max_empty_weight = 0
number_max_empty_weight = 1

for number_element in range(elements_to_send):
    weight_element = input(f"Podaj wagę {number_element + 1}. elementu: ")
    try:
        weight_element = int(weight_element)
    except ValueError:
        print("Podana wartość musi być liczbą.")
        break

    if weight_element is None or weight_element == 0:
        packages = 0

    if weight_element < 1 or weight_element > 10:
        break

    total_weight = weight_element + total_weight
    # print("Suma wszystkich elementów:", total_weight)
    weight_single_package = weight_single_package + weight_element

    if weight_single_package > 20:
        empty_weight = 20 - (weight_single_package - weight_element)
        if empty_weight > max_empty_weight:
            max_empty_weight = empty_weight
            number_max_empty_weight = packages
        weight_single_package = weight_element
        packages += 1
    # print("Waga pojedynczej paczki:", weight_single_package)

empty_weight = 20 - weight_single_package
if empty_weight > max_empty_weight:
    max_empty_weight = empty_weight
    number_max_empty_weight = packages

print("*** PODSUMOWANIE ***")
print(f"Wysłana ilość paczek: {packages}.")
print(f"Wysłano {total_weight} kg.")
print(f"Suma pustych kilogramów: {packages * 20 - total_weight} kg.")
print(f"Najwięcej pustych kilogramów ma paczka: {number_max_empty_weight} "
      f"({max_empty_weight} kg).")
