"""食材宅配コンパス - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "食材宅配コンパス"
BLOG_DESCRIPTION = "オイシックス・らでぃっしゅぼーや・大地を守る会・パルシステム・コープデリ等を徹底比較。味・コスパ・配送・安全性を主婦目線で本音レビュー。"
BLOG_URL = "https://musclelove-777.github.io/shokuzai-compass/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/shokuzai-compass"

TARGET_CATEGORIES = [
    "食材宅配サービス比較",
    "ミールキット・時短料理",
    "オーガニック・無農薬",
    "離乳食・子育て向け",
    "高齢者向け宅配食",
    "送料・配送エリア",
    "おすすめレシピ",
    "解約・乗り換え",
]

THEME = {
    "primary": "#588157",
    "accent": "#a3b18a",
    "gradient_start": "#588157",
    "gradient_end": "#dad7cd",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
