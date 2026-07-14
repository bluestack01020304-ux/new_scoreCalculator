
import gradio as gr
# 🌟 중요: app_main.py 파일에서 메인 버튼 레이아웃을 임포트합니다.
from mainUI import main_layout

# 임시 회원 데이터 (테스트용)
USER_IDS = ["admin", "a"]
USER_PWS = ["1234", "0"]

# 로그인 인증 및 화면 전환 함수
def login_handler(userid, userpw):
    userid = userid.strip()
    userpw = userpw.strip()
    
    for i in range(len(USER_IDS)):
        if userid == USER_IDS[i] and userpw == USER_PWS[i]:
            # 로그인 성공 시: 로그인 창 숨김(False), 메인 버튼 창 표시(True)
            return gr.update(visible=False), gr.update(visible=True), ""
            
    return gr.update(visible=True), gr.update(visible=False), "❌ 로그인 정보가 올바르지 않습니다."


with gr.Blocks() as LogIn:
    
    # [화면 1] 로그인 UI (처음에는 보임)
    with gr.Column(visible=True) as login_layout:
        gr.Markdown("# 로그인")
        
        userid = gr.Textbox(
            label="아이디(ID)", 
            placeholder="아이디를 입력해주세요."
        )
        userpw = gr.Textbox(
            label="비밀번호(PW)", 
            type="password", 
            placeholder="비밀번호를 입력해주세요."
        )
        
        login_btn = gr.Button("로그인", variant="primary")
        status_msg = gr.Markdown()

    # [화면 2] 메인 UI (처음에는 숨김)
    with gr.Column(visible=False) as main_container:
        # 🌟 app_main.py에서 가져온 메인 버튼 레이아웃을 이 자리에 그대로 렌더링합니다.
        main_layout.render()


    # 로그인 버튼 동작 연결
    login_btn.click(
        fn=login_handler,
        inputs=[userid, userpw],
        outputs=[login_layout, main_container, status_msg]
    )

# 앱 실행 (자동으로 인터넷 창 열림)
LogIn.launch(inbrowser=True)