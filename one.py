import logging
import datetime
import argparse


def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Треугольник равносторонний"
        elif a == b or b == c or a == c:
            return "Треугольник равнобедренный"
        else:
            return "Треугольник разносторонний"
    else:
        return "Такого треугольника не существует"


if __name__ == "__main__":
    logging.basicConfig(filename='project.log.', filemode='a',
                        encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.warning('Внимание! Запуск кода')
    Triangle = argparse.ArgumentParser(description="Введение сторон треугольника")

    Triangle.add_argument('-a', metavar='a', type=int, help='введите первую сторону треугольника', default=0)
    Triangle.add_argument('-b', metavar='b', type=int, help='введите вторую сторону треугольника', default=0)
    Triangle.add_argument('-c', metavar='c', type=int, help='введите третью сторону треугольника', default=0)

    args = Triangle.parse_args()
    logger.info(f'{datetime.datetime.now()}: Результат работы кода с параметрами {args.a}, {args.b}, {args.c} - '
                f'{triangle(args.a, args.b, args.c)}')
