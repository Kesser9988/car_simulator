class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = 0
        self.active = False
        self.km = 0

    def info(self):
        full_name = f"{self.brand} {self.model} {self.year}"
        print(full_name)
        print(f"Пробег машины - {self.probeg} км")

    def start(self):
        if not self.active:
            self.active = True
            print("Машина заведена!")
        else:
            print("Машина уже заведена!!")

    def drive(self):
        if self.active:
            if self.km > 0:
                self.probeg += self.km
                print(f"Машина проехала {self.km} км, пробег равен - {self.probeg} км.")
            else:
                print("Машина заведена, но не двигалась!")
        else:
            print("Машина заглушена!")

    def stop(self):
        if self.active:
            print("Машина заглушена!")
            self.active = False
            print(f"Машина проехала {self.km} км, пробег равен - {self.probeg} км.")
        else:
            print("Машина была заглушена и никуда не двигалась!")
            print(f"Пробег равен {self.probeg} км")


my_car = Car("Omoda", "C5", 2024)
while True:
    deystvie = ['1 — Завести', '2 — Указать расстояние', '3 — Поехать', '4 — Остановить', '5 — Показать информацию', '6 — Выйти']
    print("Выберете действие:")
    for x in deystvie:
        print(x)
    print()
    otvet = int(input("Выш выбор: "))     
    print()
    if otvet == 6:
        print("Программа симуляции завершена!")
        break
    elif otvet == 1:
        my_car.start()
        print()
    elif otvet == 2:
        if my_car.active:
            user_km = int(input("Укажите расстояние в киллометрах: "))
            my_car.km = user_km
            print()
        else:
            print("Машина заглушена, сначала необходимо завести машину!!!")
            print()
    elif otvet == 3:
        my_car.drive()
        print()
    elif otvet == 4:
        my_car.stop()
        print()
    elif otvet == 5:
        my_car.info()
    else:
        print("Нет такого варианта ответа!")