import csv
import random
#from playsound import playsound


#抽選するリストが入ったCSVファイル（各クラスごとに列のリストをcsvのファイル）を抽選する
#令和4年度 父母の会 次年度役員抽選プログラム　
#
#################
#プロンプトにて下記のファイルを実行
# $python lotty.py
#読み込みたいCSVファイルを指定して、抽選をしたい数（当選者1名＋補欠数名の数）を入力する
#enter　キーを押して抽選する
################

#ファイルの置いてあるところを指定する。デフォルトは、lotty.pyの同じディレクトリ（プログラムと同じ場所の方がわかりやすい）
csvfile_path = './'

#抽選するリストの入ったCSVのファイル名の入力
print('')
print('抽選するファイル名を入力してください。')
print('「sakura.csv」など')
print('上記ファイルの抽選対象者リストが入ったファイル名の')
print('入力をお願いします。')
csvfile_name = csvfile_path + input()
print('')
print('ファイル置いてあるファイルは下記')
print(csvfile_name)
print('')

#ファイルから列に入っている抽選候補者のリストの取り出す
def read_csv(csvfile_name):
  #csvfileを開く
  csvfile = open(csvfile_name)
  #開いたcsvファイルで、readerオブジェクトを生成する
  csvreader = csv.reader(csvfile)

  #出席番号で抽選する場合には、「lottynumber_list」
  #名前での抽選の場合には、「lottyname_list」の’#’を外す。
  #出席番号を入れる入れる抽選リスト
  #lottynumber_list = []
  #名前を入れる抽選リスト
  lottyname_list = []

  #csvが入ったreaderオブジェクトから一つ一つ抽出する
  for row in csvreader:
    #ヘッダー行は、読み込まない
    if csvreader.line_num == 1:
      continue
    #出席番号と名前のどちらかの「#」を外す
    #rowの一番最初の左の行を出席番号を読み込む。出席番号抽選の場合にはこちらを外す
    #lottynumber_list.append(row[0])
    #クラスの名前のデータを読み込む。名前抽選の場合にはこちらを外す。
    lottyname_list.append(row[1])

  csvfile.close()
  #出席番号抽選の場合にはこちらの「#」を外す。
  #return lottynumber_list
  #名前抽選の場合にはこちらの「#」を外す。
  return lottyname_list

#読み込んだ候補者リストから抽選
if __name__ == '__main__':
  result = read_csv(csvfile_name)
  #確認
  print('読み込んだリストの確認')
  print(result)
  print('')
  print('---------------------------------------')
  print('----          結果発表！！          ----')
  print('---------------------------------------')

  #resultに入れた候補者抽選リストから、random関数で抽選する
  print('抽選する人数を入力してください')
  result_list = random.sample(result, int(input()))
  #結果発表！！！(当選順位を添え字の数字と値で出力)
  print('結果発表！！！上から当選の順位です')
  num = int(0)
  print('')

  #ドラムロールの音を出す
  #playsound.playsound('./tinpany_roll.mp3')
  #playsound('./tinpany_roll.mp3')
  for i, member in enumerate(result_list):
    if i == 0:
      print('当選者：' + member)
      print('以降、予備当選候補者（順位順）')
      continue
    print(i,':', member)
