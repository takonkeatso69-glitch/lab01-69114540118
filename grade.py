def average(scores):
    if not scores:
        return 0
    return round(sum(scores) / len(scores), 2)


def to_grade(score):
    if score < 0 or score > 100:
        raise ValueError("คะแนนต้องอยู่ในช่วง 0 - 100")
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def is_pass(score):
    return score >= 50


if __name__ == "__main__":
    scores = [85, 78, 71]
    avg = average(scores)

    print(f"คะแนนเฉลี่ย: {avg}")
    print(f"เกรด: {to_grade(avg)}")
    print(f"ผลสอบ: {'ผ่าน' if is_pass(avg) else 'ไม่ผ่าน'}")