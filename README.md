# 🦁 VR-ALIGN – Portable VR-Based BSV (Binocular Vision) Measurement Tool

VR-ALIGN is a Virtual Reality project that aims to provide a **cost-effective and portable solution** for measuring **Binocular Single Vision (BSV)** — an important part of eye checkups that traditionally requires bulky and expensive equipment.

This project enables BSV testing at **free eye camps** and **remote locations**, leveraging simple VR headsets and a real-time control interface.

---

## 🧠 Problem Statement

Current instruments for BSV measurement are:
- ❌ Expensive  
- ❌ Bulky  
- ❌ Difficult to transport to field camps

---

## 💡 Our Solution

In ACEi:
- Patients view **two slides in VR** – one with a 🦁 lion and the other with a 🦁‍⬛ cage.
- These are shown at the patient’s **actual Interpupillary Distance (IPD)**.
- In normal vision, both images **merge into one** (lion appears inside the cage).
- If there is eye misalignment, the images will appear separated.
- The tester can then **move the images toward each other in real time** using a control panel.
- The distance at which the patient perceives a merged image is recorded to **calculate eye misalignment**.

---

## ⚙️ Tech Stack

- 🐍 **Python**
- 🔥 **Flask** – for backend routes and APIs
- 📡 **Socket.IO** – for real-time image control between devices
- 🥽 **VR interface** – accessible via mobile phone browser

---

## 🚀 Getting Started

### 1. Clone the repository
     ```bash
     git clone https://github.com/KAVYAJAIN410/ACEi.git
     cd ACEi

###2. Set up a virtual environment
     
     
      python3 -m venv env

      source env/bin/activate #MAC

      .\env\Scripts\activate   #WINDOWS


###3. Install dependencies
           
            
      pip install -r requirements.txt

###4.Run the Flask server

      python app.py
      
##🌐Application Routes
Route	  Description
/	      Controller interface (used by the operator on laptop)
/vr	    VR interface (to be opened on mobile inside VR headset)
      
🧪 Demo Use Case
👁 A patient wears a basic VR headset and looks at the /vr route on their phone.
💻 The operator uses their laptop to go to / and move images until the patient confirms the lion is inside the cage.
📏 The measured displacement is used to compute ocular misalignment.

MIT License © 2025 Kavya Jain
    
