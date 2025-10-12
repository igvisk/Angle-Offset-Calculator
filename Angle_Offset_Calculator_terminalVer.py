#Angle Offset Calculator - Sirka otvoru pri danom uhle a dlzke

# Geometrický model:
# Vstupy: 
#   1. Dĺžka základnej priamky
#   2. Uhol sklonu druhej priamky (prednastavená hodnota 5°)
# Výstupy:
#   1. Vypočítaná dĺžka tretej priamky (kolmá na základnú) – dĺžka vznikajúceho otvoru

import math

#Function - terminal version/obsolete
def distance(length_cm, angle_degree):       
    # Prevod stupňov na radiány
    angle_rad = math.radians(angle_degree)
    # Vzdialenosť = dĺžka * tan(uhol)
    return length_cm * math.tan(angle_rad)


#terminal version /obsolete
# Príklady
print("8,8 cm pri 5°:", round(distance(8.8, 5), 2), "cm")      # → 0,77 cm

print("17 cm pri 5°:", round(distance(17, 5), 2), "cm")        # → 1.49 cm

# Zadaj vlastnu dlzku
length_cm = float(input("Zadaj dlzku priamky leziacej na 0°: "))
print(f"{length_cm} cm pri 5°, vychýlenie:", round(distance(length_cm, 5), 2), "cm")