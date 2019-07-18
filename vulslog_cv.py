import json
import csv
import time
import sys
args = sys.argv 
json_place = '%s' % args[1] #第一引数はjsonファイルの場所
json_name = json_place.split("/")[-1].strip(".json") #jsonの名前を抽出
csv_name = '%s' % args[2] #第二引数はcsvを保存したい場所と名前
#csv_place = '%s' % args[2] #第二引数はcsvを保存したい場所
with  open(json_place, 'r') as f1: #jsonを開く
    log_json = json.load(f1)
    with open(csv_name, 'w', encoding="utf_8_sig") as f2 :
    #with open(csv_place +'/%s_%s.csv' % (json_name,time.strftime("%Y%m%d-%H%M%S"),), 'w', encoding="utf_8_sig") as f2 : #csvを[ファイル名]_[年月日]-[時刻].csvの形で生成
        writer = csv.writer(f2) #csvを開く
        vdatalist = dict(type="", cveID="", title ="",summary="", cvss2Score="", cvss2Vector="", cvss2Severity="",cvss3Score="", cvss3Vector="", cvss3Severity="", sourceLink="", references="", cweIDs="",  published="", lastModified="", mitigation="") #辞書型の生成
        writer.writerow(vdatalist.keys()) #辞書型のkeyをcsvに書き込み
        for i in log_json['scannedCves']: # iはcvdid
            for j in  log_json['scannedCves'][i]['cveContents']: #jは脆弱性ソース先名
                cveid = log_json['scannedCves'][i]['cveContents'][j]
                vdatalist2 = vdatalist
                for a in cveid.keys(): #aは個々の脆弱性情報の詳細の名前
                    if a == 'references':
                        url = list()
                        for b in cveid[a]: #bは脆弱性情報の参照リンク
                            if not b['source']:
                                url.append(b['link'])
                            else:
                                url.append(b['source'] + ' :' + b['link'])
                        urljoin = '\r\n'.join(url)
                        vdatalist2[a] = urljoin
                    else:
                        vdatalist2[a] = cveid[a]
                writer.writerow(vdatalist2.values())