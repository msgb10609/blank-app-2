import streamlit as st

# 페이지 제목 설정
st.set_page_config(page_title="거리별 톨만 온도 계산기", layout="centered")
st.title("🌡️ 거리별 톨만 온도 계산기")

# 1. 톨만 온도 인지 여부 확인 (라디오 버튼)
answer = st.radio(
    "이것은 거리별 톨만 온도 계산기입니다. 혹시 톨만 온도가 뭔지 아시나요??",
    ("yes", "no"),
    index=0,  # 기본값 yes
)

# 2. 'no'를 선택했을 때 설명 출력
if answer == "no":
    st.markdown("---")
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
    st.info(
        "**이제 프로그램을 다시 실행하여 yes로 바꾼 후, 계산을 해볼까요??**"
    )

# 3. 'yes'를 선택했을 때 계산기 작동
else:
    # 슈바르츠실트 반지름 입력 (기본값 10, 권장 범위 10~30 표기)
    rs = st.number_input(
        "슈바르츠실트 반지름은(km)? (10~30 권장) :",
        min_value=1,
        value=10,
        step=1,
    )

    st.markdown("---")

    T_infinity = 2.73

    temperature = []
    distance = []

    # 기존 연산 로직 그대로 유지
    for r in range(rs + 1, rs + 22):
        T_tolman = ((1 - rs / r) ** (-0.5)) * T_infinity
        temperature.append(T_tolman)
        distance.append(r)

    # 21개의 결과 출력 및 뜨거운 정도 계산
    for i in range(21):
        st.write(
            f"**슈바르츠실트 반지름이 {rs}km 라면**, 블랙홀과의 거리가 **{distance[i]}km** 일 때, 톨만 온도는 **{temperature[i]:.2f}K** 입니다."
        )

        # 온도별 별점(●) 출력 로직 그대로 유지
        if temperature[i] > 6.5:
            st.error("뜨거운 정도 :  ●●●●●●●●●●!!!")
        elif 5.5 <= temperature[i] < 6.5:
            st.warning("뜨거운 정도 :  ●●●●●●●!!")
        elif 4.5 <= temperature[i] < 5.5:
            st.warning("뜨거운 정도 : ●●●●●!")
        elif 3.5 <= temperature[i] < 4.5:
            st.info("뜨거운 정도 : ●●●")
        else:
            st.success("뜨거운 정도 : ●")

    st.markdown("---")

    # 하단 결론 문구
    st.write(
        "방금 본 표에서 알 수 있듯이, 톨만 온도는 블랙홀과 가까운 곳, 즉 중력이 강할 수록 더 높게 나타난다는걸 알 수 있습니다.."
    )
    st.write(
        "추가적으로, 공식이 분모에 루트가 씌어진 형태를 하고 있기에, 거리가 가까워 질수록 온도가 기하급수적으로 올라간다는걸 알 수 있습니다."
    )