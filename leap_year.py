# leap year
def check_year(year):
    if year % 400 == 0:
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False
def input_data():
    while True:
        try:
            year = int(input("Nhập một năm bất kỳ đi nhé: "))
            return year
            break
        except Exception:
            print("Dữ liệu nhập vào phải là số nguyên, không phải số thập phân hoặc chuỗi")
            print()

if __name__ == '__main__':
    year = input_data()
    if check_year(year):
        print("Năm {} là năm nhuận!!!".format(year))
    else:
        print("Năm {} không phải là năm nhuận!!!".format(year))
