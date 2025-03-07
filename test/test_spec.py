import asyncio
import os
from app.agents.spec_agent import SpecRecommender  # SpecRecommender 클래스가 정의된 파일을 import

# 테스트용 사용자 입력 데이터
user_input = {
    "필수_스펙": {
        "성능": [
            "4K 해상도 지원", "8192 이상의 압력 감지 레벨", "펜 틸트 감지 기능",
            "최소 8GB RAM", "쿼드코어 프로세서"
        ],
        "하드웨어": [
            "최소 10인치 이상의 디스플레이", "색 정확도가 높은 IPS 또는 OLED 패널",
            "그래픽 작업을 위한 dedicated GPU 또는 강력한 integrated GPU"
        ],
        "기능": [
            "정밀한 펜 압력 감지", "틸트 인식 기능", "그래픽 디자인 소프트웨어와의 호환성"
        ]
    },
    "선호_스펙": {
        "성능": ["12인치 이상의 디스플레이", "16GB 이상의 RAM", "옥타코어 프로세서"],
        "하드웨어": ["OLED 디스플레이", "dedicated GPU"],
        "기능": ["무선 연결 기능", "터치 제스처 지원", "조절 가능한 스탠드"]
    },
    "제외_스펙": ["10인치 미만의 디스플레이", "4K 미만의 해상도", "8192 미만의 압력 감지 레벨"],
    "가격_범위": {
        "최소": {"value": 500000, "unit": "KRW"},
        "최대": {"value": 1200000, "unit": "KRW"}
    }
}

async def main():
    """SpecRecommender 실행"""
    recommender = SpecRecommender()
    recommendations = await recommender.generate_recommendations(user_input)

    print("\n🔹 **추천 제품 리스트** 🔹\n")
    for product in recommendations.get("추천 제품", []):
        print(f"📌 **제품명:** {product['제품명']}")
        print(f"💰 **가격:** {product['가격']} KRW")
        print(f"✅ **장점:** {product['추천 이유']['장점']}")
        print(f"❌ **단점:** {product['추천 이유']['단점']}")
        print("\n🎯 **핵심 사항:**")
        for spec in product["핵심 사항"]:
            print(f"  🔹 {spec['항목']}: {spec['사양']} ({spec['설명']})")
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    asyncio.run(main())
