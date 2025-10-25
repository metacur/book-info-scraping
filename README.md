※各サイトにおいてスクレイピングが禁止されている場合は実行しないでください


# Overview
* 特定ワード（固有名詞、作家名、等）の関連書籍の情報を収集するスクレイピングのコードです。
* 国立国会図書館サーチ（NDL Search）でデータをを取得し、 タイトル・出版社・出版年を統合してcsv出力します。
* たとえばワードに人物名を設定した場合、その人物の書いた書籍と、その人物名が主題や副題に含まれる書籍が収集対象データとなります。


* プログラムの末尾あたりにワードを設定する箇所（変数名：person\_name）があります。
* max_pages を調整することで取得件数を増やせます


# Prerequisites
Python

# Requirements
pip install requests 
pip install beautifulsoup4
pip install lxml

