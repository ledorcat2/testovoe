# Задание 1: Функция для получения уникальных элементов из списка
def unique_elements(input_list):
    return list(set(input_list))

# Задание 2: Функция для получения списка простых чисел в заданном диапазоне
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(minimum, maximum):
    primes = []
    for num in range(minimum, maximum + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Задание 3: Класс Point
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    
    def get_coordinates(self):
        return (self.x, self.y)
    
    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Задание 4: Программа для сортировки списка строк по длине
def sort_strings_by_length(strings):
    return sorted(strings, key=lambda x: (len(x), x))

# Пример использования функций и класса
if __name__ == "__main__":
    # Задание 1
    list1 = [1, 2, 3, 4, 3, 2, 1]
    print("Уникальные элементы:", unique_elements(list1))
    
    # Задание 2
    print("Простые числа от 10 до 30:", prime_numbers(10, 30))
    
    # Задание 3
    point1 = Point(1, 2)
    point2 = Point(4, 6)
    print("Расстояние между точками:", point1.distance_to(point2))
    
    # Задание 4
    strings = ["apple", "banana", "pear", "grapefruit", "kiwi"]
    print("Список строк по длине:", sort_strings_by_length(strings))
