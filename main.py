class Samochod:
    def __init__(self, marka="Nieznana", model="Nieznana", rokprodukcji=0, przebieg=0):
        self.marka = marka
        self.model = model
        self.rokprodukcji = rokprodukcji
        self.przebieg = przebieg

    def __str__(self):
        return f"Samochod: Marka - {self.marka}, Model - {self.model}, Rok Produkcji - {self.rokprodukcji}, Przebieg - {self.przebieg} km"

samochod1 = Samochod()
samochod2 = Samochod("Toyota", "Corolla")
samochod3 = Samochod("Ford", "Focus", 2015)
samochod4 = Samochod("Honda", "Civic", 2018, 50000)

print(samochod1)
print(samochod2)
print(samochod3)
print(samochod4)
