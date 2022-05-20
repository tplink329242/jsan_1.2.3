cd apache-commons/

nohup sh run.sh > full.log 2>&1 &

python3 extract_log.py 5 ${BASH_SOURCE[0]}
