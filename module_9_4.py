first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda f, s: f == s, first, second)))


# ==================================================================================
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file_a = open(file_name, 'w', encoding='utf-8')
        for i in data_set:
            file_a.write(str(i) + '\n')
        file_a.close()

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# ==================================================================================
from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        result = choice(self.words)
        return result


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
