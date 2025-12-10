# 名人名言資料庫範例
quotes_db = [
    {
        "quote": "It always seems impossible until it's done.",
        "author": "Nelson Mandela",
        "role": "前南非總統、反種族隔離運動領袖",
        "source": "演講，2001年",
        "tags": ["勇氣", "堅持", "改變"],
        "shortBio": "曼德拉因反種族隔離被監禁27年，出獄後領導南非民主轉型。",
        "suggestion": "當你覺得目標遙不可及時，分解成小步驟並持續行動。"
    },
    {
        "quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
        "role": "蘋果公司共同創辦人、企業家",
        "source": "史丹佛畢業演講，2005年",
        "tags": ["熱情", "工作", "創新"],
        "shortBio": "Jobs 創辦 Apple，帶動多次產業創新。",
        "suggestion": "找能讓你投入的方向，持久的熱情會放大你的成長。"
    }
]

# 根據 tag 配對名言

def get_quote_by_tag(tag):
    for item in quotes_db:
        if tag in item["tags"]:
            return item
    return None

# 範例用法
if __name__ == "__main__":
    print("歡迎來到心靈建議平台！請輸入你想詢問的主題（如：勇氣、熱情、工作），或輸入 exit 離開。")
    while True:
        user_tag = input("請輸入主題：").strip()
        if user_tag.lower() == "exit":
            print("感謝使用，祝福你！")
            break
        result = get_quote_by_tag(user_tag)
        if result:
            print(f"\n『{result['quote']}』")
            print(f"— {result['author']}（{result['role']}）")
            print(result['shortBio'])
            print("建議：" + result['suggestion'] + "\n")
        else:
            print("很抱歉，目前沒有相關主題的名言。請嘗試其他主題。\n")
