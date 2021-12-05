class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


m1 = Matrix([[-2, 0, 4], [1, 1, 1], [0, 1, 2], [2, 1, 1]])
m2 = Matrix([[-3, 2, 1], [3, 2, 1], [7, 2, -2], [2, 2, -7]])
print(m1.__add__(m2))
