import requests
from pathlib import Path

# 설정할 핸들(아이디) 입력
SOLVEDAC_HANDLE = "juwon0718"   # 본인의 백준 핸들로 변경
CODEFORCES_HANDLE = "knowin_kyeong" # 본인의 코드포스 핸들로 변경

# 저장할 디렉토리 설정
OUT_DIR = Path("../badges")
OUT_DIR.mkdir(parents=True, exist_ok=True)
HEADERS = {"User-Agent": "Mozilla/5.0"}

def download_svg(url: str, filename: str):
    print(f"Fetching {filename}...")
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        
        out_path = OUT_DIR / filename
        out_path.write_text(response.text, encoding="utf-8")
        print(f"Saved: {out_path.resolve()}")
    except Exception as e:
        print(f"Failed to fetch {filename}: {e}")

def main():
    # 1. Solved.ac 뱃지 (mazassumnida API 활용)
    solvedac_url = f"http://mazassumnida.wtf/api/v2/generate_badge?boj={SOLVEDAC_HANDLE}"
    download_svg(solvedac_url, "solvedac.svg")

    # 2. Codeforces 뱃지 (codeforces-readme-stats API 활용)
    codeforces_url = f"https://codeforces-readme-stats.vercel.app/api/card?username={CODEFORCES_HANDLE}&force_username=true&disable_animations=true"
    download_svg(codeforces_url, "codeforces.svg")

if __name__ == "__main__":
    main()