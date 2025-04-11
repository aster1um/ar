class Stack:
    def __init__(self, size=10):  # Исправлено: __init__
        if size <= 0:
            raise ValueError("Размер стека должен быть положительным")
        self.size = size
        self.stack = [None] * size
        self.top_index = -1  # Индекс вершины стека

    def push(self, value):
        """Добавляет элемент в стек.  Выводит сообщение об ошибке при переполнении."""
        if self.top_index == self.size - 1:
            print("Ошибка: Стек переполнен")
            return  # Ничего не возвращаем в случае переполнения
        self.top_index += 1
        self.stack[self.top_index] = value


    def pop(self):
        """Удаляет и возвращает верхний элемент. Бросает исключение, если стек пуст."""
        if self.is_empty():
            raise IndexError("Стек пуст")
        value = self.stack[self.top_index]
        self.top_index -= 1
        return value

    def top(self):
        """Возвращает верхний элемент без удаления. Бросает исключение, если стек пуст."""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.stack[self.top_index]

    def is_empty(self):
        """Проверяет, пуст ли стек."""
        return self.top_index == -1

    def __str__(self): #Исправлено: __str__
        """Строковое представление стека (только элементы, без None)."""
        if self.is_empty():
            return "[]"
        return str(self.stack[:self.top_index + 1])


# Пример использования:
if __name__ == "__main__":
    stack = Stack(3)

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)  # [10, 20, 30]

    stack.push(40) # Ошибка: Стек переполнен

    print(stack.pop())  # 30
    print(stack.pop())  # 20
    print(stack.pop())  # 10

    try:
        stack.pop()  # Ошибка: Стек пуст
    except IndexError as e:
        print(f"Ошибка: {e}")

