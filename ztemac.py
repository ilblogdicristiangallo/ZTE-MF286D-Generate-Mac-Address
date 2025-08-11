import random

def genera_mac_zte(mac_default, posizioni_da_modificare=[9, 10, 12, 13]):
    """
    Genera un nuovo MAC address basato su un MAC di default per ZTE MF286D,
    modificando solo alcune cifre negli ultimi due byte.
    
    :param mac_default: Il MAC address di base (es. "D4:72:26:60:E0:98")
    :param posizioni_da_modificare: Indici dei caratteri da modificare (inclusi i ':')
    :return: Un nuovo MAC address con alcune cifre modificate
    """
    mac_lista = list(mac_default)  # Converte il MAC in lista per modificarlo
    
    for i in posizioni_da_modificare:
        if mac_lista[i] != ":":  # Evita di modificare i ':'
            mac_lista[i] = random.choice("0123456789ABCDEF")

    return "".join(mac_lista)  # Ricompone il MAC

# MAC address di default per ZTE MF286D
mac_default = "D4:72:26:60:E0:98"

# Genera un nuovo MAC modificato e lo stampa
print(genera_mac_zte(mac_default))
