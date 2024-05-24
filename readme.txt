wget https://www.python.org/ftp/python/3.10.5/python-3.10.5-macosx10.9.pkg
sudo installer -pkg python-3.10.5-macosx10.9.pkg -target /

# pipコマンドで必要なパッケージをインストール
pip3 install selenium
pip3 install pytest
pip3 install pytest-html
pip3 install webdriver_manager
pip3 install chromedriver_autoinstaller
pip3 install chromedriver_binary
pip3 install pillow

・スクリーンショットの撮影
以下のような感じでコマンドで、screenshot.pyがあるディレクトリで実行する。
Python3 screenshot.py --url="サイトURL" --slug="スクショが保存されるディレクトリ名" --mode="2"


※オプション引数「--mode」 は0がPCモード、1がタブレットモード、2がスマホモードで、切り替えられる。設定しない場合はデフォルトで0になっている。
※現在はスクショが保存されるディレクトリはscreenshot.pyと同じ階層になっている。修正必要があればselenium_screenshot.pyを弄ること。