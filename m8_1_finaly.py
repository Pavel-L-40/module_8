# Try Except Else Finaly

def add_everything_up(a, b):
    try:
        a + b
    except TypeError as exc:
        print(exc.args)
        a = str(a)
        b = str(b)
    except SyntaxError as exc:
        print(exc.args)
        a = str(a)
        b = str(b)
    else:
        print("it's ok")
    finally:
        return (a + b)

print()
print(add_everything_up(123.456, ' строка'), '\n')
print(add_everything_up('яблоко ', 4215), '\n')
print(add_everything_up(123.456, 7))
