class Cellula:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cellula(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells <= other.cells:
            print("Raznost > 0")
            raise ValueError
        return Cellula(self.cells - other.cells)

    def __mul__(self, other):
        return Cellula(self.cells * other.cells)

    def __truediv__(self, other):
        return Cellula(round(self.cells / other.cells))

    def make_order(self, row):
        ordered = ['*' * row for _ in range(self.cells // row)]
        ordered.append('*' * (self.cells % row))
        return f'\n'.join(ordered)


if __name__ == '__main__':
    e1 = Cellula(27)
    e2 = Cellula(20)
    e3 = e1 + e2
    try:
        e4 = e3 - Cellula(100)
    except ValueError as e:
        e4 = e3 - Cellula(10)
    finally:
        print(f'e4.cells={e4.cells}')
    e5 = e3 * e4
    e6 = e5 / e1
    print(f'e1:7: cells({e1.cells})\n{e1.make_order(7)}')
    print(f'e2:7: cells({e2.cells})\n{e2.make_order(7)}')
    print(f'e3:7: cells({e3.cells})\n{e3.make_order(7)}')
    print(f'e4:7: cells({e4.cells})\n{e4.make_order(7)}')
    print(f'e5:70: cells({e5.cells})\n{e5.make_order(70)}')
    print(f'e6:7: cells({e6.cells})\n{e6.make_order(7)}')
