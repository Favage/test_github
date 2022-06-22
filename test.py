def count(n):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst


if __name__ == "__main__":
    n = int(input("Enter n: "))
    result = count(n)
    for x in result:
        print(x, end="\n")
