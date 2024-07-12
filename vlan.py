vlan = int(input("Ingrese el número de VLAN (1-4096): "))

if 1 <= vlan <= 1005:
    print(f"La VLAN {vlan} corresponde al rango normal.")
elif 1006 <= vlan <= 4096:
    print(f"La VLAN {vlan} corresponde al rango extendido.")
else:
    print("Número de VLAN inválido. Debe estar entre 1 y 4096.")
