from pico2d import *
import math

open_canvas()

# 이미지 로드
grass = load_image('grass.png')
character = load_image('character.png')

# 캔버스 기초 세팅
clear_canvas_now()
grass.draw_now(400, 30)
character.draw_now(400, 90)
delay(1)

# 캐릭터 위치 갱신
def character_setting(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.05)

# 삼각형 그리기
def run_triangle():
    print('TRIANGLE')

    # 삼각형의 세 꼭지점 좌표, 중간, 우측, 위
    # 리스트로 좌표 묶기
    points = [(400, 90), (600, 90), (400, 290)]

    for i in range(3):
        start_x, start_y = points[i]
        end_x, end_y = points[(i + 1) % 3]
        
        for j in range(0, 100, 5):
            x = start_x + (end_x - start_x) * (j / 100)
            y = start_y + (end_y - start_y) * (j / 100)
            character_setting(x, y)
            
# 원 그리기
def run_circle():
    print('CIRCLE')
    cx, cy, r = 400, 300, 200
   
    for deg in range(90 , 450, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        character_setting(x, y)


while True:
    run_triangle()
    run_circle()

close_canvas()
