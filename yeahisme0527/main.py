from transformers import pipeline

def main():
    print("=== YehEun's Korean Sentiment Program ===")

    # 한국어 전용 감정 분석 모델
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
        raw_label = result["label"]   # LABEL_0 / LABEL_1 / LABEL_2
        score = result["score"]

        # 🔻 여기서 3단계를 2단계(부정/긍정)로 강제 변환
        if raw_label == "LABEL_0":
            final_label = "부정 😡"
        else:  # LABEL_1, LABEL_2 모두 긍정으로 처리
            final_label = "긍정 🙂"

        print(f"모델 원래 라벨: {raw_label}")
        print(f"최종 판단(2단계): {final_label} (확신도: {score:.4f})")
        print("-" * 40)

if __name__ == "__main__":
    main()
