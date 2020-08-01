import calendar


class newsched():
    def trythis(self):
        print("try this")

    def __next__(self):
        print(1)


try:
    my_num = 5
    print(str(my_num))
except ZeroDivisionError as err:
    print(err)

file = open("notes.txt", "r")
# print(file.read())

for line in file.readlines():
    print(line)
file.close()

newsched().trythis()
newsched().__next__()