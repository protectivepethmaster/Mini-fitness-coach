# 🏋️‍♂️ Mini Fitness Coach

**Mini Fitness Coach**  
เป็นเว็บแอปพลิเคชันแนว **Functional Programming** สำหรับช่วยผู้ใช้วางแผนและติดตามการออกกำลังกาย โดยใช้ **ExerciseDB API** เพื่อแนะนำท่าออกกำลังกาย พร้อมระบบบันทึกการฝึก วิเคราะห์แนวโน้มรายสัปดาห์ และผู้ช่วยอัจฉริยะ (AI Assistant)

---

## 🚀 คุณสมบัติ (Features)

### 💪 การออกกำลังกาย (Workout Tracking)
- ดึงข้อมูลท่าออกกำลังกายจาก **ExerciseDB API** ตามกลุ่มกล้ามเนื้อ  
- บันทึกจำนวนเซตและครั้งต่อเซต  
- แสดงสถิติรายวันและรายสัปดาห์  

### 🧠 ผู้ช่วยอัจฉริยะ (AI Assistant)
- วิเคราะห์พฤติกรรมการฝึกของผู้ใช้  
- แนะนำกล้ามเนื้อที่ควรฝึกเพิ่มเติมเพื่อความสมดุล  
- (เพิ่มเติม) ใช้ **OpenAI API** เพื่อคำแนะนำเชิงเหตุผล  

### 📊 แดชบอร์ด (Dashboard)
- สรุปผลการออกกำลังกายทั้งหมด  
- แสดงกราฟสถิติรายสัปดาห์ (จำนวนครั้ง/กล้ามเนื้อที่ฝึก)  
- วิเคราะห์แนวโน้มพัฒนาในรูปแบบเข้าใจง่าย  

### ⚙️ ระบบจัดเก็บข้อมูล (Persistence)
- ใช้ฐานข้อมูล **SQLite** สำหรับเก็บข้อมูลการฝึก  
- โครงสร้างโมดูลแยกชัดเจน และสามารถขยายเป็น MySQL ได้  

---

## 🧩 โครงสร้างโปรเจกต์ (Project Structure)

```
mini_fitness_coach/
│
├── app/
│   ├── main.py              # จุดเริ่มต้นโปรแกรม
│   ├── exercise_api.py      # ดึงข้อมูลจาก ExerciseDB API
│   ├── db.py                # จัดการฐานข้อมูล SQLite
│   ├── analyzer.py          # วิเคราะห์ข้อมูลและแนวโน้ม
│   ├── ai_assistant.py      # ผู้ช่วย AI สำหรับให้คำแนะนำ
│   ├── gui.py               # Streamlit UI
│   └── __init__.py
│
├── data/
│   └── workouts.db
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── tests/
│   └── test_db.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the project
```bash
git clone https://github.com/YOURUSERNAME/mini_fitness_coach.git
cd mini_fitness_coach
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit app
```bash
streamlit run app/main.py
```

เปิดเว็บเบราว์เซอร์ไปที่ 👉 [http://localhost:8501](http://localhost:8501)

---

## 📦 Dependencies

| Library | Description |
|----------|-------------|
| `requests` | ดึงข้อมูลจาก ExerciseDB API |
| `streamlit` | สร้าง Web UI |
| `matplotlib` | แสดงกราฟ |
| `sqlite3` | จัดการฐานข้อมูล |
| `dotenv` | โหลดตัวแปร API Key |
| `openai` *(optional)* | ใช้สำหรับ AI Assistant |

---

## 🧠 Concept

> “Train smart, not just hard.”

แนวคิดของโปรเจกต์คือการใช้ AI เป็น “ผู้ช่วย” ไม่ใช่ผู้แทน — ช่วยผู้ใช้วางแผนการฝึกที่มีประสิทธิภาพมากขึ้น และส่งเสริมการคิดเชิงระบบในยุคที่ AI เป็นเครื่องมือสำคัญของโปรแกรมเมอร์

---

## 📜 Example Workflow

1. ผู้ใช้เลือกกล้ามเนื้อที่ต้องการฝึก  
2. ระบบแนะนำท่าออกกำลังกายจาก **ExerciseDB**  
3. ผู้ใช้บันทึกข้อมูลการฝึก (sets/reps)  
4. ระบบแสดงสรุปผลและกราฟรายสัปดาห์  
5. AI Assistant ให้คำแนะนำเพิ่มเติมตามพฤติกรรมการฝึก  

---

## 👨‍💻 Developers

**Mini Fitness Coach Team – College of Computing**

| ชื่อ | บทบาท |
|------|--------|
| นายภูมิรัฐ สุขเอนกนันท์ | Project Manager / CI-CD Integrator |
| [ชื่อสมาชิกที่ 2] | Core Developer / Automated Tester |

---

## 📜 License

Distributed under the **MIT License**  
ใช้เพื่อการศึกษาและสามารถพัฒนาต่อยอดได้อย่างอิส
