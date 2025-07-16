import streamlit as st
from datetime import datetime

# 여행지 정보: 추천 이유 + 이미지 URL 포함
mbti_recommendations = {
    "ENFP": [
        {
            "place": "암스테르담, 네덜란드",
            "reason": "창의적이고 자유로운 ENFP에게 예술과 개방성이 넘치는 도시예요.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/6/65/Amsterdam_Canal_Ring_July_2011.jpg"
        },
        {
            "place": "리우데자네이루, 브라질",
            "reason": "열정 가득한 ENFP에게 축제와 자연이 가득한 도시가 잘 어울려요.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Rio_de_Janeiro_-_Rafael_Defavari.jpg"
        },
        {
            "place": "멕시코시티, 멕시코",
            "reason": "다채로운 문화와 따뜻한 분위기를 즐기는 ENFP에게 최고의 여행지입니다.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Mexico_City_Collage.png"
        }
    ],
    "INTJ": [
        {
            "place": "레이크 디스트릭트, 영국",
            "reason": "혼자만의 시간을 즐기며 사색을 좋아하는 INTJ에게 완벽한 자연 속 휴식처입니다.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/d/d1/Derwent_Water_from_Catbells.jpg"
        },
        {
            "place": "세도나, 미국",
            "reason": "조용한 자연 속에서 에너지를 재충전하고 싶은 INTJ에게 안성맞춤이에요.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Sedona_Arizona.jpg"
        },
        {
            "place": "카파도키아, 터키",
            "reason": "비범한 풍경과 고요한 분위기는 깊은 사고를 즐기는 INTJ와 잘 어울려요.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Cappadocia_balloon_ride.jpg"
        }
    ],
    "ISFP": [
        {
            "place": "발리, 인도네시아",
            "reason": "감성적이고 자연친화적인 ISFP에게 평화롭고 아름다운 바다가 어울려요.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Bali_Indonesia_Temple.jpg"
        },
        {
            "place": "치앙마이, 태국",
            "reason": "잔잔하고 느긋한 분위기를 좋아하는 ISFP에게 딱 맞는 힐링 여행지입니다.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Chiang_Mai_Montage.png"
        },
        {
            "place": "바르셀로나, 스페인",
            "reason": "예술과 개성을 사랑하는 ISFP에게 가우디의 도시 바르셀로나는 최고의 선택입니다.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Sagrada_Familia_01.jpg"
        }
    ]
}

# 스트림릿 기본 설정
st.set_page_config(page_title="MBTI 여행지 추천기", page_icon="✈️")

# 헤더
st.title("✈️ MBTI 여행지 추천기")
st.caption("당신의 성격에 꼭 맞는 여행지를 추천해드릴게요!")
st.markdown("---")

# MBTI 선택
mbti_list = list(mbti_recommendations.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요:", mbti_list)

# 버튼 클릭 시 추천 여행지 출력
if st.button("여행지 추천받기!"):
    st.subheader("🌟 추천 여행지 3곳")
    for idx, spot in enumerate(mbti_recommendations[selected_mbti], 1):
        st.markdown(f"### {idx}. {spot['place']}")
        st.image(spot['image'], use_column_width=True)
        st.markdown(f"**이유:** {spot['reason']}")
        st.markdown("---")
    st.success("멋진 여행이 되시길 바랍니다! 🧳")

else:
    st.info("MBTI를 선택하고 버튼을 눌러보세요 😊")

# 하단 현재 시간
st.markdown("---")
st.caption(f"⏰ 지금 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
