import streamlit as st
from datetime import datetime

# 16개 MBTI별 여행지 추천 데이터 (이유 + 이미지 포함)
mbti_recommendations = {
    "ISTJ": [
        {"place": "교토, 일본", "reason": "전통과 질서를 중시하는 ISTJ에게 고요한 사찰과 정원이 잘 어울려요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Kinkaku-ji_the_Golden_Pavilion_in_Kyoto%2C_Japan.jpg"},
        {"place": "하이델베르크, 독일", "reason": "고전적인 분위기와 역사적인 유산이 많은 도시입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/f/f4/Heidelberg_Castle_from_Philosophenweg.jpg"},
        {"place": "타이베이, 대만", "reason": "깔끔하고 정돈된 도시 분위기가 ISTJ에게 안정감을 줘요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/7/72/Taipei_skyline.jpg"}
    ],
    "ISFJ": [
        {"place": "브뤼헤, 벨기에", "reason": "조용하고 아기자기한 도시로 따뜻한 감성을 가진 ISFJ에게 적합해요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Bruges_Belgium_Canals.jpg"},
        {"place": "프라하, 체코", "reason": "아름다운 고성들과 클래식한 분위기가 잘 어울리는 도시예요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/3/37/Prague_Castle_and_Charles_Bridge.jpg"},
        {"place": "제주도, 한국", "reason": "가족 중심적이고 조용한 휴식을 원하는 ISFJ에게 제격이에요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Jeju_Seongsan_Ilchulbong.jpg"}
    ],
    "INFJ": [
        {"place": "피렌체, 이탈리아", "reason": "깊은 사색과 예술을 사랑하는 INFJ에게 감성을 자극하는 도시입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Firenze_-_Ponte_Vecchio_and_Arno_River.jpg"},
        {"place": "산토리니, 그리스", "reason": "평화로운 분위기와 아름다운 풍경이 내면을 채워줘요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/c/cb/Santorini_sunset_%2810034927844%29.jpg"},
        {"place": "하노이, 베트남", "reason": "조용하면서도 문화 깊은 도시로 INFJ에게 영감을 줘요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Temple_of_Literature_Hanoi.jpg"}
    ],
    "INTJ": [
        {"place": "레이크 디스트릭트, 영국", "reason": "혼자만의 시간을 즐기며 사색을 좋아하는 INTJ에게 완벽한 자연 속 휴식처입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/d/d1/Derwent_Water_from_Catbells.jpg"},
        {"place": "세도나, 미국", "reason": "조용한 자연 속에서 에너지를 재충전하고 싶은 INTJ에게 안성맞춤이에요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Sedona_Arizona.jpg"},
        {"place": "카파도키아, 터키", "reason": "비범한 풍경과 고요한 분위기는 깊은 사고를 즐기는 INTJ와 잘 어울려요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Cappadocia_balloon_ride.jpg"}
    ],
    "ISTP": [
        {"place": "요세미티, 미국", "reason": "액티비티와 자연을 동시에 즐길 수 있어 ISTP에게 제격이에요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/1/14/Yosemite_Tunnel_View.jpg"},
        {"place": "알프스, 스위스", "reason": "탐험을 좋아하는 ISTP에게 이상적인 도전의 공간입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/1/13/Zermatt_and_Matterhorn.jpg"},
        {"place": "뉴질랜드 남섬", "reason": "모험과 자유를 사랑하는 ISTP에게 완벽한 곳입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Lake_Tekapo_and_Church_of_the_Good_Shepherd.jpg"}
    ],
    "ISFP": [
        {"place": "발리, 인도네시아", "reason": "감성적이고 자연친화적인 ISFP에게 평화롭고 아름다운 바다가 어울려요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Bali_Indonesia_Temple.jpg"},
        {"place": "치앙마이, 태국", "reason": "잔잔하고 느긋한 분위기를 좋아하는 ISFP에게 딱 맞는 힐링 여행지입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Chiang_Mai_Montage.png"},
        {"place": "바르셀로나, 스페인", "reason": "예술과 개성을 사랑하는 ISFP에게 가우디의 도시 바르셀로나는 최고의 선택입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Sagrada_Familia_01.jpg"}
    ],
    "INFP": [
        {"place": "코펜하겐, 덴마크", "reason": "이상주의적인 INFP에게 따뜻하고 세련된 도시예요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Nyhavn_Copenhagen.jpg"},
        {"place": "에든버러, 스코틀랜드", "reason": "문학과 고요함이 조화를 이루는 도시로 INFP의 내면을 자극합니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Edinburgh_Castle_Scotland.jpg"},
        {"place": "우붓, 발리", "reason": "자연과 함께 명상과 내면의 여정을 좋아하는 INFP에게 딱이에요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Tegalalang_Rice_Terrace_Ubud_Bali.jpg"}
    ],
    "INTP": [
        {"place": "헬싱키, 핀란드", "reason": "논리적이고 조용한 INTP에게 잘 맞는 깨끗하고 차분한 도시입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Helsinki_Cathedral_and_Senate_Square.jpg"},
        {"place": "오슬로, 노르웨이", "reason": "지적 호기심을 자극하는 현대적이고 조용한 도시예요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/b/be/Oslo_opera_house.jpg"},
        {"place": "퀘벡시티, 캐나다", "reason": "유럽풍의 감성과 지적 자극이 공존하는 도시로 INTP에게 이상적입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Chateau_Frontenac_and_old_Quebec.jpg"}
    ],
    "ESTP": [
        {"place": "라스베이거스, 미국", "reason": "화려함과 즐거움을 추구하는 ESTP에게 완벽한 도시입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Vegas_Strip.jpg"},
        {"place": "도쿄, 일본", "reason": "끊임없이 변화하는 도시의 에너지가 ESTP의 활동성과 잘 맞아요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/1/13/Tokyo_Skyline.jpg"},
        {"place": "두바이, UAE", "reason": "최신 트렌드와 모험을 동시에 즐길 수 있어요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/5/55/Dubai_skyline_2020.jpg"}
    ],
    "ESFP": [
        {"place": "파리, 프랑스", "reason": "화려하고 감각적인 여행을 즐기는 ESFP에게 어울리는 도시입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Paris_Night.jpg"},
        {"place": "마이애미, 미국", "reason": "태양과 바다, 축제를 사랑하는 ESFP의 천국이죠.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Miami_Beach.jpg"},
        {"place": "시드니, 호주", "reason": "에너지 넘치는 도시와 해변이 공존하는 여행지예요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Sydney_Opera_House_-_Dec_2008.jpg"}
    ],
    "ENFP": [
        {"place": "암스테르담, 네덜란드", "reason": "자유로운 분위기와 예술이 살아 있는 도시로 ENFP에게 안성맞춤이에요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/6/65/Amsterdam_Canal_Ring_July_2011.jpg"},
        {"place": "리우데자네이루, 브라질", "reason": "열정 가득한 축제 도시로 ENFP의 에너지를 충전해요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Rio_de_Janeiro_-_Rafael_Defavari.jpg"},
        {"place": "멕시코시티, 멕시코", "reason": "다채로운 문화와 따뜻한 분위기를 즐기는 ENFP에게 최고의 여행지입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Mexico_City_Collage.png"}
    ],
    "ENTP": [
        {"place": "베를린, 독일", "reason": "새로움을 탐험하는 ENTP에게 역사와 현대가 공존하는 도시예요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Berlin_Brandenburger_Tor_Nacht.jpg"},
        {"place": "홍콩", "reason": "빠르게 변하는 도시의 역동성이 ENTP와 잘 맞습니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Hong_Kong_Skyline_Restitch_-_Dec_2007.jpg"},
        {"place": "시애틀, 미국", "reason": "기술과 문화가 조화롭게 어우러진 도시입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Seattle_Skyline.jpg"}
    ],
    "ESTJ": [
        {"place": "워싱턴 D.C., 미국", "reason": "논리적이고 체계적인 ESTJ에게 정치와 역사의 중심지인 이 도시가 잘 어울려요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/e/e6/US_Capitol_west_side.JPG"},
        {"place": "싱가포르", "reason": "질서 있고 효율적인 도시 환경이 ESTJ의 성향에 잘 맞습니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Singapore_Skyline_at_Night.jpg"},
        {"place": "도쿄, 일본", "reason": "시간 관리와 질서를 중시하는 ESTJ에게 적합한 도시입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/1/13/Tokyo_Skyline.jpg"}
    ],
    "ESFJ": [
        {"place": "로마, 이탈리아", "reason": "사교적이고 따뜻한 ESFJ에게 역사가 살아 있는 낭만적인 도시입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Colosseum_in_Rome%2C_Italy_-_April_2007.jpg"},
        {"place": "세부, 필리핀", "reason": "정 많은 ESFJ에게 활기차고 친근한 해변 도시입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/1/19/Mactan_beach_Cebu.jpg"},
        {"place": "푸꾸옥, 베트남", "reason": "따뜻한 사람들과 평화로운 자연이 있는 조용한 휴양지예요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/7/75/Phu_Quoc_Beach.jpg"}
    ],
    "ENFJ": [
        {"place": "부다페스트, 헝가리", "reason": "이해심 많고 따뜻한 ENFJ에게 감성적이고 역사 깊은 도시입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Budapest_Chain_Bridge.jpg"},
        {"place": "부에노스아이레스, 아르헨티나", "reason": "열정과 인간관계를 중시하는 ENFJ에게 매력적인 도시입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Buenos_Aires_obelisco_daytime.jpg"},
        {"place": "서울, 한국", "reason": "다채로운 문화와 인간 중심적인 환경이 ENFJ와 잘 맞아요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Seoul_Skyline_Night.jpg"}
    ],
    "ENTJ": [
        {"place": "런던, 영국", "reason": "리더십 강한 ENTJ에게 글로벌 중심지로서의 가치가 있는 도시입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/f/f3/London_Eye_Twilight_April_2006.jpg"},
        {"place": "뉴욕, 미국", "reason": "도전적이고 야망 있는 ENTJ에게 최고의 기회를 제공하는 도시입니다.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Manhattan_skyline_from_Weehawken%2C_NJ.jpg"},
        {"place": "상하이, 중국", "reason": "급성장하는 도시의 에너지가 ENTJ의 추진력과 잘 맞아요.",
         "image": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Shanghai_Skyline.jpg"}
    ]
}
