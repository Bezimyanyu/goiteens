def determine_quadrant(x, y):
    if y > 0:
        if x > 0:
            return "Точка знаходиться у першій чверті."
        elif x < 0:
            return "Точка знаходиться у другій чверті."
        else:
            return "Точка знаходиться на осі Y."
    elif y < 0:
        if x > 0:
            return "Точка знаходиться у четвертій чверті."
        elif x < 0:
            return "Точка знаходиться у третій чверті."
        else:
            return "Точка знаходиться на осі Y."
    else:
        if x != 0:
            return "Точка знаходиться на осі X."
        else:
            return "Точка знаходиться у початку координат."

def exam_result(surname, points):
    if points > 80:
        return f"Студент {surname} здав іспит."
    else:
        return f"Студент {surname} не склав іспит."

surname = input("Введіть прізвище студента: ")
points = int(input("Введіть кількість балів: "))

print(exam_result(surname, points))
