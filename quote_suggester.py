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
    },
    {
        "quote": "知之者不如好之者，好之者不如樂之者。",
        "author": "孔子",
        "role": "春秋時期思想家、儒家創始人",
        "source": "《論語·雍也》",
        "tags": ["學習", "熱情", "成長"],
        "shortBio": "孔子提倡仁愛、禮儀，影響東亞文化數千年。",
        "suggestion": "學習時保持興趣與快樂，能讓你持續進步。"
    },
    {
        "quote": "Life is like riding a bicycle. To keep your balance you must keep moving.",
        "author": "Albert Einstein",
        "role": "理論物理學家、相對論創立者",
        "source": "信件，1930年",
        "tags": ["生活", "堅持", "改變"],
        "shortBio": "愛因斯坦提出相對論，改變現代物理學。",
        "suggestion": "遇到困難時，持續前進就能找到平衡。"
    },
    {
        "quote": "We may encounter many defeats but we must not be defeated.",
        "author": "Maya Angelou",
        "role": "美國詩人、作家、民權運動者",
        "source": "演講，1991年",
        "tags": ["堅持", "逆境", "勇氣"],
        "shortBio": "安傑盧以詩歌和自傳鼓舞無數人，倡導平權。",
        "suggestion": "失敗是成長的一部分，不要因此放棄。"
    },
    {
        "quote": "To thine own self be true.",
        "author": "William Shakespeare",
        "role": "英國劇作家、詩人",
        "source": "《哈姆雷特》",
        "tags": ["誠實", "自我", "人生"],
        "shortBio": "莎士比亞創作多部經典劇作，影響世界文學。",
        "suggestion": "做自己，誠實面對內心，才能活得自在。"
    },
    {
        "quote": "One never notices what has been done; one can only see what remains to be done.",
        "author": "Marie Curie",
        "role": "物理學家、化學家，諾貝爾獎得主",
        "source": "自傳，1923年",
        "tags": ["科學", "努力", "謙虛"],
        "shortBio": "居禮夫人發現鐳和釙，是首位獲兩次諾貝爾獎女性。",
        "suggestion": "保持謙虛，持續努力，成就自然累積。"
    },
    {
        "quote": "The greater danger for most of us lies not in setting our aim too high and falling short; but in setting our aim too low, and achieving our mark.",
        "author": "Michelangelo",
        "role": "文藝復興時期藝術家、雕塑家",
        "source": "書信，1510年",
        "tags": ["目標", "夢想", "成長"],
        "shortBio": "米開朗基羅創作大衛像、西斯汀教堂壁畫。",
        "suggestion": "勇敢設定高目標，挑戰自我才能突破。"
    },
    {
        "quote": "Let us make our future now, and let us make our dreams tomorrow's reality.",
        "author": "Malala Yousafzai",
        "role": "巴基斯坦人權運動者、諾貝爾和平獎得主",
        "source": "演講，2013年",
        "tags": ["夢想", "未來", "勇氣"],
        "shortBio": "馬拉拉為女性教育發聲，年僅17歲獲諾貝爾和平獎。",
        "suggestion": "勇敢追夢，行動才能改變未來。"
    },
    {
        "quote": "The only true wisdom is in knowing you know nothing.",
        "author": "Socrates",
        "role": "古希臘哲學家",
        "source": "柏拉圖《阿波羅吉亞》記載",
        "tags": ["謙虛", "智慧", "學習"],
        "shortBio": "蘇格拉底以問答法啟發思考，被譽為西方哲學之父。",
        "suggestion": "保持謙虛，勇於提問，才能真正學習。"
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
範例
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

