# from student import Student

from student import init


def main():
    st1 = Student()
    st2 = Student()
    print(vars(st1))
    print(vars(st2))

    # init(st1, "Alex", 20, 10)
    # init(st2, "Mike", 20, 10)
    # init(st3, "Kate", 20, 10)

    st1.name = "Alex"
    st2.name = "Anna"
    st1.mark = 10
    st2.mark = 7
    st1.age= 20
    st2.age = 18

    # print(st1.name)
    # print(getattr(st1, "name"))
    # print(st1.__getattribute__("name"))

    # del st1.name
    # delattr(st1, 'mark')
    # st1.__delattr__("age")

    setattr(st1, "name", "Andrei")
    st1.__setattr__("name", "Olga")

    st1.init()



    print(vars(st1))
    print(st1.__dict__)
    print(dir(st1))
    print(help(st1))


if __name__ == "__main__":
    main()

