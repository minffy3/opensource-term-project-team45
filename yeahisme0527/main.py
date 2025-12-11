from transformers import pipeline

def main():
    print("=== YehEun's Korean Sentiment Program ===")

    classifier = pipeline(
        "sentiment-analysis",
        model="WhitePeak/bert-base-cased-Korean-sentiment"
    )

    print("✅ 모델 로딩 완료! 이제 문장을 입력해 보세요.\n")

    while True:
        text = input("문장을 입력하세요 (종료: exit): ")
        if text.lower() == "exit":
            print("프로그램을 종료합니다.")
            break

        result = classifier(text)[0]
        label_id = result['label']    # LABEL_0 / LABEL_1 / LABEL_2
        score = result['score']

        label_map = {
            "LABEL_0": "부정 😡",
            "LABEL_1": "중립 😐",
            "LABEL_2": "긍정 🙂",
        }
        pretty_label = label_map.get(label_id, label_id)

        print(f"결과: {pretty_label} (확신도: {score:.4f})")
        print("-" * 40)

if __name__ == "__main__":
    main()

