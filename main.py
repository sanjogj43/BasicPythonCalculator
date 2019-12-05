import re

print("Basic Calculator")
previous = 0
run = True


def perform_math():
    global run
    global previous

    if previous == 0:
        equation = input("Please enter equation:")
    else:
        equation = input(str(previous))

    if equation == "quit":
        run = False
    else:
        equation = re.sub("[a-zA-Z:''()]", "", equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        print(equation)


def main():
    while run:
        perform_math()


main()
