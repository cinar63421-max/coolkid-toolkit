import os
import subprocess
import time
import sys

def main_panel():
    PY_PATH = sys.executable
    BASE_DIR = os.path.join(os.path.expanduser("~"), "Coolkid_Tools")
    
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
        ============================================================
        |                COOLKID_V1 / TOOLKIT V7.0                 |
        |              ----------------------------                |
        |           OWNER: PATRON | STATUS: INTEL MODE             |
        ============================================================
        
        [1] SMS BOMBER (Saldırı)    [2] DDOS / FLOOD (Yıkım)
        [3] PHISHING (Avlanma)      [4] SHERLOCK (Hesap Bulucu)
        [5] HOLEHE (E-Posta İzleyici) [6] SLOWLORIS (DoS)
        [7] NMAP (Network Scan)     [8] WI-FI PASSWORD SHOW
        [9] INTELLIGENCE DASHBOARD (Özel İstihbarat)
        
        [Q] ==> TOOLKIT'DEN AYRIL
        ============================================================
        """)
        
        secim = input("Hedef kim, Patron? : ").lower()

        if secim == 'q': break

        # --- 9. ÖZEL İSTİHBARAT MODÜLÜ ---
        if secim == "9":
            print("\n--- COOLKID ÖZEL SORGUPANELİ ---")
            target_mail = input("Hedef E-Posta: ")
            
            # Holehe: E-postanın hangi sitelere (Instagram, Twitter, Banka vb.) kayıtlı olduğunu bulur
            tool_dir = os.path.join(BASE_DIR, "holehe")
            if not os.path.exists(tool_dir):
                print("[*] Holehe (İstihbarat Aracı) indiriliyor...")
                os.chdir(BASE_DIR)
                subprocess.run(["git", "clone", "https://github.com/megadose/holehe.git"])
                os.chdir(tool_dir)
                subprocess.run([PY_PATH, "setup.py", "install"])
            
            print(f"\n[*] {target_mail} için dijital ayak izi taranıyor...")
            # Holehe genelde doğrudan komut olarak çalışır ama kütüphane olarak da çağırılabilir
            subprocess.run(["holehe", target_mail])
            input("\n[!] Sorgu bitti. Enter'a bas...")

        # --- 4. SHERLOCK (GELİŞTİRİLMİŞ) ---
        elif secim == "4":
            username = input("\nAranacak Kullanıcı Adı: ")
            tool_dir = os.path.join(BASE_DIR, "sherlock")
            if not os.path.exists(tool_dir):
                os.chdir(BASE_DIR)
                subprocess.run(["git", "clone", "https://github.com/sherlock-project/sherlock.git"])
                os.chdir(tool_dir)
                subprocess.run([PY_PATH, "-m", "pip", "install", "-r", "requirements.txt"])
            
            os.chdir(tool_dir)
            print(f"[*] {username} internetin her köşesinde aranıyor...")
            subprocess.run([PY_PATH, "sherlock", username])
            input("\n[!] Arama bitti. Enter'a bas...")

        # --- DİĞER MODÜLLER (Önceki sürümlerden devam eder) ---
        # ... (DDoS ve SMS kısımlarını buraya eklemeyi unutma kanka)