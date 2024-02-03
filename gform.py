import requests
import random
form_url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSfHBUQtcm-BkLmNlWppXEoXdxrjgUvUM1fv6oetwrWJH8ulXw/formResponse'


def callGform():
    value = ['มากที่สุด (5)', 'มาก (4)', 'ปานกลาง (3)']
    # value = ['มากที่สุด (5)', 'มาก (4)', 'ปานกลาง (3)', 'น้อย (2)']
    # value = ['มากที่สุด (5)', 'มาก (4)', 'ปานกลาง (3)',
    #          'น้อย (2)', 'น้อยที่สุด (1)']
    suggestions = ['ไม่มีจร้า', '', '', '', '', 'ไม่มี', 'นาน ๆ ใช้ครั้ง ไม่ค่อยสะดวก',
                   'ดีมาก', 'ตอบโจทย์', '', '', '', '', '', '', '', '',]
    # suggestions = [
    #     " จัดระบบให้มีการติดตามผลและรายงานเพื่อให้ผู้ใช้สามารถทราบสถานะและผลลัพธ์ของระบบได้ในเวลาทันที.",
    #     "พัฒนาความสามารถในการเชื่อมต่อกับอุปกรณ์อื่นๆ เพื่อเพิ่มประสิทธิภาพและความสามารถของระบบ.",
    #     "ใช้เทคโนโลยีการเรียนรู้เพื่อทำนายแนวโน้มและสามารถทำเรียนรู้จากข้อมูลทั้งหมด.",
    #     "สนับสนุนการใช้งานผ่านอินเทอร์เน็ตเพื่อให้ผู้ใช้สามารถควบคุมและตรวจสอบระบบได้ทุกที่ทุกเวลา.",
    #     "พัฒนาการบริหารจัดการที่มีภาพรวมและทั้งครอบคลุมทุกรายละเอียดของการใช้งาน.",
    #     "ระบบควรสามารถจัดการข้อมูลที่เกี่ยวข้องกับตำแหน่งที่ตั้งของอุปกรณ์ใน Smart Farm.",
    #     "ส่งเสริมการบูรณาการทางเกษตรและการใช้เทคโนโลยีเพื่อสร้างระบบที่ยั่งยืน.",
    #     "พัฒนาระบบให้มีประสิทธิภาพในการจัดการและให้น้ำตามความต้องการของพืช.",
    #     "ให้ข้อมูลและคำแนะนำเกี่ยวกับการจัดการกับสภาพอากาศที่ส่งผลต่อการเกษตร.",
    #     "สนับสนุนความสามารถในการทำนายและตรวจวัดอุณหภูมิดิน.",
    #     "พัฒนาระบบในการติดตามและแจ้งเตือนเกี่ยวกับคุณภาพดิน.",
    #     "นำเสนอข้อมูลที่สามารถนำไปใช้ในการตลาดผลผลิต.",
    #     "การสนับสนุนโมเดลการทำเลี้ยงสัตว์: สนับสนุนการใช้เทคโนโลยีในการทำเลี้ยงสัตว์.",
    #     "พัฒนาระบบที่สามารถควบคุมและให้ปุ๋ยตามความต้องการของพืช.",
    #     "สนับสนุนการรวมระบบกับโปรแกรมและระบบที่ใช้ในฟาร์ม.",
    #     "พัฒนาระบบที่สามารถรองรับการเพาะเมล็ดและติดตามขั้นตอนต่างๆ.",
    #     "พัฒนาระบบที่สามารถใช้งานได้ผ่านมือถือเพื่อความสะดวกและเข้าถึงง่าย.",
    #     "การส่งเสริมความยั่งยืน",
    #     'ไม่มีจร้า', '', '', '', '', 'ไม่มี', 'นาน ๆ ใช้ครั้ง ไม่ค่อยสะดวก',
    #     'ดีมาก', 'ตอบโจทย์', '', '', '', '', '', '', '', '',
    # ]
    payload = {
        "entry.1598024020": random.choice(value),
        "entry.511057586": random.choice(value),
        "entry.820219989": random.choice(value),
        "entry.1536888005": random.choice(value),
        "entry.1081501010": random.choice(value),
        "entry.1016627210": random.choice(value),
        "entry.1606843533": random.choice(value),
        "entry.1711328391": random.choice(value),
        "entry.2042848464": random.choice(value),
        "entry.1989784115": random.choice(value),
        "entry.1743732877": random.choice(value),
        "entry.2043491057": random.choice(value),
        "entry.426623522": random.choice(value),
        "entry.148559807": random.choice(value),
        "entry.131493263": random.choice(value),
        "entry.1656012255": random.choice(value),
        "entry.761453629": random.choice(value),
        "entry.1973681773": random.choice(value),
        "entry.1219662185": random.choice(value),
        "entry.1196421183": random.choice(value),
        "entry.1747755167": random.choice(value),
        "entry.2096137980": random.choice(value),
        "entry.1155374026": random.choice(value),
        "entry.204445977": random.choice(value),
        "entry.1892499685": random.choice(value),
        "entry.2076101627": random.choice(value),
        "entry.176467582": random.choice(suggestions),
    }
    if __name__ == '__main__':
        res = requests.post(form_url, payload)
        if res.status_code == 200:
            return True
        elif res.status_code == 400:
            print('Check your payload')
            return False
        elif res.status_code == 404:
            print('Check your form_url')
            return False
    return False


# จำนวนแบบประเมินที่ต้องการให้ทำ
number = 100
for x in range(number):
    callGform()
