number_input_a = int(input("정수 입력> "))
if string_input.isdigit():
    number_input_a = int(string_input)
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
    break
else:
    print("정수를 입력해주세요!")

list_input_a = ["52", "273", "32", "스파이", "103"]

list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass
    print("{} 내부에 있는 숫자는".format(list_input_a))
    print("{}입니다.".format(list_number))

number = [52, 273, 32, 103, 90, 10, 275]

print("# (2) 요소 내부에 없는 값 찾기")
number = 10000
ㅇㅂㅇ
    print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
ㅇㅂㅇ
    print("- 리스트 내뷍 없는 값입니다.") print()

def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되없습니다.")
        ㅇㅂㅇ.ㅇㅂㅇ()
        print("try 구문의 retern 키워드 뒤입니다")
    except:
        print("except 구문이 실행되었습니다.")
        retern
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")

test()

student = [
    { "name": "김가인", "korean": 87, "math": 90, "english": 88, "science": 86},
    { "name": "박시후", "korean": 92, "math": 78, "english": 95, "science": 86},
    { "name": "이선민", "korean": 90, "math": 86, "english": 92, "science": 90}
]

return student["korean"] + student["math"] + student["english"] + student["science"]
