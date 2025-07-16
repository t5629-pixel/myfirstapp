import streamlit as st
from datetime import datetime

# 🌍 MBTI별 여행지 추천 데이터
mbti_travel = {
    "ISTJ": ["교토, 일본", "하이델베르크, 독일", "타이베이, 대만"],
    "ISFJ": ["브뤼헤, 벨기에", "프라하, 체코", "제주도, 한국"],
    "INFJ": ["피렌체, 이탈리아", "산토리니, 그리스", "하노이, 베트남"],
    "INTJ": ["레이크 디스트릭트, 영국", "세도나, 미국", "카파도키아, 터키"],
    "ISTP": ["요세미티, 미국", "알프스, 스위스", "뉴질랜드 남섬"],
    "ISFP": ["발리, 인도네시아", "치앙마이, 태국", "바르셀로나, 스페인"],
    "INFP": ["코펜하겐, 덴마크", "에든버러, 스코틀랜드", "우붓, 발리"],
    "INTP": ["헬싱키, 핀란드", "오슬로, 노르웨이", "퀘벡시티, 캐나다"],
    "ESTP": ["라스베이거스, 미국", "도쿄, 일본", "두바이, UAE"],
    "ESFP": ["파리, 프랑스", "마이애미, 미국", "시드니, 호주"],
    "ENFP": ["암스테르담, 네덜란드", "리우데자네이루, 브라질", "멕시코시티, 멕시코"],
    "ENTP": ["베를린, 독일", "홍콩", "시애틀, 미국"],
    "ESTJ": ["워싱턴 D.C., 미국", "싱가포르", "도쿄, 일본"],
    "ESFJ": ["로마, 이탈리아", "세부, 필리핀", "푸꾸옥, 베트남"],
    "ENFJ": ["부다페스트, 헝가리", "부에노스아이레스, 아르헨티나", "서울, 한국"],
    "ENTJ": ["런던, 영국", "뉴욕, 미국", "상하이, 중국"],
}

# 🎨 앱 기본 설정
st.set_page_config(page_title="MBTI 여행지 추천기", page_icon="✈️")

# 🧡 헤더
st.title("✈️ MBTI 여행지 추천기")
st.caption("당신의 성격에 꼭 맞는 여행지를 추천해드릴게요!")
st.markdown("---")

# 📌 MBTI 선택
mbti_list = list(mbti_travel.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요:", mbti_list)

# 🚀 버튼 클릭 시 추천 여행지 표시
if st.button("여행지 추천받기!"):
    destinations = mbti_travel.get(selected_mbti, [])
    st.subheader("🌟 추천 여행지:")
    for idx, place in enumerate(destinations, 1):
        st.markdown(f"**{idx}. {place}**")
    st.success("즐거운 여행 되세요! 🧳")
else:
    st.info("MBTI를 선택한 후 버튼을 눌러보세요 😊")

# 🕒 하단에 현재 시간
st.markdown("---")
st.caption(f"⏰ 지금 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
