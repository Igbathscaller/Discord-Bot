all: main.py
	nohup python3 main.py &
test: main.py
	python3 main.py
connect1: 
	ssh pi_1@192.168.1.25
connect2: 
	ssh pi_2@192.168.1.26
