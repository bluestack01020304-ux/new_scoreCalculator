import gradio as gr

# main_login.py에서 불러와 사용할 화면 뼈대 정의
with gr.Blocks() as main_layout:
    
    # 상하 여백을 주어 버튼이 화면 중앙(수직)에 가깝게 위치하도록 구성
    gr.Markdown("<br><br><br>") 
    
    # gr.Row()를 사용하면 버튼이 가로로 나란히 균등하게 배치됩니다.
    with gr.Row():
        btn_go_input = gr.Button("📝 학생 점수 입력", variant="primary", size="lg")
        btn_go_view = gr.Button("📋 전체 학생 보기", variant="primary", size="lg")
        btn_go_ai = gr.Button("🤖 AI에게 질문하기", variant="primary", size="lg")
        
    gr.Markdown("<br><br><br>")