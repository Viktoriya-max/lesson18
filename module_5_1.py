#Developer - не только разработчик
class House: #Реализовала класс House
    def __init__(self, name, number_of_floors):
        self.name = name # атрибут - имя
        self.number_of_floors = number_of_floors #атрибут - кол-во этажей

    def go_to(self,new_floor): #Метод go_to выводит значения от 1 до new_floor(включительно)
        n_f = int(new_floor)
        for i in range(1, n_f + 1):
            if n_f >= self.number_of_floors or n_f <= 1: #условие пи котором выводится "Такого этажа не существует"
                print('Такого этажа не существует')
                break
            else:
                print(i) #вывод этажей от 1 до new_floor включительно
h1 = House('Дом', 5)
h2 = House('Небоскреб', 38)
h1.go_to(10)
h2.go_to(37)