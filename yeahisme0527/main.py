
def greet(name: str) -> str:
    """
    사용자의 이름을 입력받아 인사 문구를 생성하는 함수.
    """
    return f"Hello, {name}! Welcome to Yeh Eun's Open Source Project 🎉"


def main():
    print("=== YehEun's Greeting Program ===")
    user_name = input("이름을 입력하세요: ")
    message = greet(user_name)
    print(message)


if __name__ == "__main__":
    main()

