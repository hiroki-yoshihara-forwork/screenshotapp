import argparse
from selenium_screenshot import AutoWrite

def main():
    # コマンドライン引数のパース
    parser = argparse.ArgumentParser(description='Take screenshot of a webpage.')
    parser.add_argument('--url', type=str, help='URL of the webpage to take screenshot of', required=True)
    parser.add_argument('--slug', type=str, help='Slug for the screenshot', required=True)
    parser.add_argument('--mode', type=str, help='Slug for the screenshot', required=False)
    args = parser.parse_args()

    # AutoWriteクラスのインスタンス化とスクリーンショットの取得
    aw = AutoWrite(args.url, args.slug)

if __name__ == "__main__":
    main()