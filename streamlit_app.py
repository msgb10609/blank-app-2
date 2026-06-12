import streamlit as st

# 1. 페이지 기본 설정 및 우주 감성 테마(CSS) 주입
st.set_page_config(page_title="거리별 톨만 온도 계산기", layout="centered")

# 배경을 깊은 우주 느낌(짙은 네이비/블랙)으로 바꾸고, 텍스트와 구분선에 네온 효과를 줍니다.
st.markdown(
    """
    <style>
    /* 메인 배경색 및 기본 글자색 변경 */
    .stApp {
        background-color: #0B0F19;
        color: #E2E8F0;
    }
    /* 입력 위젯 라벨 글자색 변경 */
    label, .stRadio p {
        color: #6366F1 !important;
        font-weight: bold !important;
    }
    /* 구분선 스타일 변경 */
    hr {
        border: 0;
        height: 1px;
        background: linear-gradient(to right, #3B82F6, #8B5CF6, #EC4899);
        margin: 20px 0;
    }
    /* 텍스트 하이라이트 스타일 */
    .highlight {
        color: #F43F5E;
        font-weight: bold;
    }
    .neon-blue {
        color: #3B82F6;
        text-shadow: 0 0 5px #3B82F6;
    }
    .neon-purple {
        color: #A855F7;
        text-shadow: 0 0 5px #A855F7;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 타이틀 (이모지와 네온 효과)
st.markdown(
    "<h1 style='text-align: center; color: #8B5CF6; text-shadow: 0 0 10px #8B5CF6;'>🕳️ 거리별 톨만 온도 계산기</h1>",
    unsafe_allow_html=True,
)
st.write("---")

# 1. 톨만 온도 인지 여부 확인
answer = st.radio(
    "이것은 거리별 톨만 온도 계산기입니다. 혹시 톨만 온도가 뭔지 아시나요??",
    ("yes", "no"),
    index=0,
)

# 2. 'no'를 선택했을 때 설명 출력
if answer == "no":
    st.write("---")
    st.write("톨만 온도란, 아인슈타인의 특수 상대성 이론에서 생기는 현상으로,")
    st.write(
        "특수 상대성 이론에 따르면, 중력이 강한 곳은 시간이 느리게 흐릅니다."
    )
    st.write("온도라는 것은 그것을 이루는 물체의 에너지와 비례히는데,")
    st.write("시간이 느리게 흐른다면, 입자들의 에너지가 낮아지게 됩니다.")
    st.write("에너지가 낮아지면 그곳의 국소 온도가 감소하게 됩니다.")
    st.write(
        "중력이 강한곳과 약한곳의 온도가 다르므로 자연을 열평형을 맞추기 위해"
    )
    st.write("중력장이 강한 곳, 즉 온도가 낮은 곳의 온도를 올리게 됩니다.")
    st.write(
        "배경이 우주 배경복사 온도라면, 상승한 이 온도를 우리는 톨만 온도라고 부릅니다."
    )
    st.write(
        "추가적으로, 슈바르츠실트 반지름이라는 것은 블랙홀의 사건의 지평성 반지름입니다."
    )

    # 안내 문구를 카드 형태로 강조
    st.markdown(
        """
        <div style='background-color: #1E1B4B; padding: 15px; border-radius: 10px; border: 1px solid #6366F1; text-align: center;'>
            <span style='color: #F43F5E; font-weight: bold;'>💡 이제 프로그램을 다시 실행하여 yes로 바꾼 후, 계산을 해볼까요??</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# 3. 'yes'를 선택했을 때 계산기 작동
else:
    rs = st.number_input(
        "슈바르츠실트 반지름은(km)? (10~30 권장) :",
        min_value=1,
        value=10,
        step=1,
    )

    st.write("---")

    T_infinity = 2.73

    temperature = []
    distance = []

    for r in range(rs + 1, rs + 22):
        T_tolman = ((1 - rs / r) ** (-0.5)) * T_infinity
        temperature.append(T_tolman)
        distance.append(r)

    # 결과 출력창을 스크롤 박스나 깔끔한 카드로 묶어 시각화
    with st.container():
        for i in range(21):
            # 기본 텍스트에 하이라이팅 추가
            st.markdown(
                f"슈바르츠실트 반지름이 <span class='neon-purple'>{rs}km</span> 라면, 블랙홀과의 거리가 <span class='neon-blue'>{distance[i]}km</span> 일 때, 톨만 온도는 <span class='highlight'>{temperature[i]:.2f}K</span> 입니다.",
                unsafe_allow_html=True,
            )

            # 뜨거운 정도에 따라 커스텀 네온 바(Bar) 형태의 디자인 출력
            if temperature[i] > 6.5:
                st.markdown(
                    "<code style='color: #EF4444; background-color: #451A03; padding: 2px 8px; border-radius: 4px;'>뜨거운 정도 :  ●●●●●●●●●●!!!</code>",
                    unsafe_allow_html=True,
                )
            elif 5.5 <= temperature[i] < 6.5:
                st.markdown(
                    "<code style='color: #F97316; background-color: #431407; padding: 2px 8px; border-radius: 4px;'>뜨거운 정도 :  ●●●●●●●!!</code>",
                    unsafe_allow_html=True,
                )
            elif 4.5 <= temperature[i] < 5.5:
                st.markdown(
                    "<code style='color: #FBBF24; background-color: #382606; padding: 2px 8px; border-radius: 4px;'>뜨거운 정도 : ●●●●●!</code>",
                    unsafe_allow_html=True,
                )
            elif 3.5 <= temperature[i] < 4.5:
                st.markdown(
                    "<code style='color: #3B82F6; background-color: #172554; padding: 2px 8px; border-radius: 4px;'>뜨거운 정도 : ●●●</code>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    "<code style='color: #10B981; background-color: #064E3B; padding: 2px 8px; border-radius: 4px;'>뜨거운 정도 : ●</code>",
                    unsafe_allow_html=True,
                )
            st.write(" ")

    st.write("---")

    # 하단 결론 문구 (블랙홀 연구실 느낌의 박스로 감싸기)
    st.markdown(
        """
        <div style='background-color: #111827; padding: 20px; border-radius: 8px; border-left: 5px solid #8B5CF6;'>
            <p style='margin-bottom: 8px; color: #E2E8F0;'>📌 <b>분석 결과:</b></p>
            <p style='font-size: 0.95rem; color: #9CA3AF;'>방금 본 표에서 알 수 있듯이, 톨만 온도는 블랙홀과 가까운 곳, 즉 중력이 강할 수록 더 높게 나타난다는걸 알 수 있습니다.</p>
            <p style='font-size: 0.95rem; color: #9CA3AF; margin-bottom: 0;'>추가적으로, 공식이 분모에 루트가 씌어진 형태를 하고 있기에, 거리가 가까워 질수록 온도가 기하급수적으로 올라간다는걸 알 수 있습니다.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )