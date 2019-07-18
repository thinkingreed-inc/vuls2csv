# Vuls log CSV converter
![example](https://img.shields.io/badge/Python-3.6-3776AB.svg?logo=python&style=plastic)

* Convert Vuls's JSON log file to CSV file.

## Description
After scaning server, [Vuls](https://github.com/future-architect/vuls/blob/master/README.md) generate JSON file includeing vulnerability data. This generate vulnerability CSV list from JSON data. This CSV can be opend by Excel.
![example](img/example.png) 

## Environment
Python3.6.7
## Usage
1. Open file 
1. Get JSON type log data from Vuls server (/vuls/results)
1. Save JSON data 
1. Execute `python3  vulslog_cv.py  log.json log.csv`
1. `log.csv` be generated

## Output
```csv
type,cveID,title,summary,cvss2Score,cvss2Vector,cvss2Severity,cvss3Score,cvss3Vector,cvss3Severity,sourceLink,references,cweIDs,published,lastModified,mitigation
redhat_api,CVE-2014-8181,CVE-2014-8181 kernel: scsi: do not fill dirty page content in the SG_IO buffer,"** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem.  When the candidate has been publicized, the details for this candidate will be provided.",2.1,AV:L/AC:L/Au:N/C:P/I:N/A:N,Low,0,,,https://access.redhat.com/security/cve/CVE-2014-8181,,['CWE-665'],2016-05-13T00:00:00Z,0001-01-01T00:00:00Z,
```

## CSV Columns
* "type"  
* "cveID"  
* "title"  
* "summary"  
* "cvss2Score"  
* "cvss2Vector"  
* "cvss2Severity"  
* "cvss3Score"  
* "cvss3Vector"  
* "cvss3Severity"  
* "sourceLink"  
* "references"  
* "cweIDs"  
* "published"  
* "lastModified"  
* "mitigati"  

## Licence
[MIT](LICENSE.txt)