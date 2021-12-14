import pygame as pg
import math


class Cardioida:
    def __init__(self, app):
        self.app = app
        self.radius = 400
        self.num_lines = 200
        # Вывод на центр
        self.translate = self.app.screen.get_width() // 2, self.app.screen.get_height() // 2
        # Для цвета
        self.counter, self.inc = 0, 0.01

    # Плавная смена от 0 до 1 и обратно
    def get_color(self):
        self.counter += self.inc
        self.counter, self.inc = (self.counter, self.inc) if 0 < self.counter < 1 else (
            max(min(self.counter, 1), 0), -self.inc)

        return pg.Color("red").lerp("blue", self.counter)

    # Отрисовка кардиойды
    def draw(self):
        # Добавляем биение =)
        time = pg.time.get_ticks()
        self.radius = 350 + 50 * abs(math.sin(time * 0.004) - 0.5)

        # Постепенное формирование кардиойды
        factor = 1 + 0.0001 * time

        # Строим
        for i in range(self.num_lines):
            theta = (2 * math.pi / self.num_lines) * i
            x1 = int(self.radius * math.cos(theta)) + self.translate[0]
            y1 = int(self.radius * math.sin(theta)) + self.translate[1]

            # x2 = int(self.radius * math.cos(2 * theta)) + self.translate[0]
            # y2 = int(self.radius * math.sin(2 * theta)) + self.translate[1]

            x2 = int(self.radius * math.cos(factor * theta)) + self.translate[0]
            y2 = int(self.radius * math.sin(factor * theta)) + self.translate[1]

            # print(f"x1:{x1}\ny1:{y1}\nx2:{x2}\ny2:{y2}\n")

            # Линия соединения
            # pg.draw.aaline(self.app.screen, "blue", (x1, y1), (x2, y2))
            pg.draw.aaline(self.app.screen, self.get_color(), (x1, y1), (x2, y2))

class App:
    def __init__(self):
        # Создаётся поверхность отрисовки 
        self.screen = pg.display.set_mode([1600, 900])
        self.clock = pg.time.Clock()
        self.cardioida = Cardioida(self)

    # Обновление и закрашивание экрана
    def draw(self):
        self.screen.fill("black")
        self.cardioida.draw()
        pg.display.flip()

    # Запуск основного цикла
    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]


if __name__ == '__main__':
    app = App()
    app.run()