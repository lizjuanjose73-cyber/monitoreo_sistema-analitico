#!/bin/bash

LOG_FILE="system.log"

# Timestamp
echo "TIME: $(date '+%Y-%m-%d %H:%M:%S')" >> $LOG_FILE

# CPU (solo número)
CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}')
echo "CPU: $CPU" >> $LOG_FILE

# RAM (% usada)
RAM=$(free | awk '/Mem:/ {printf("%.2f"), $3/$2 * 100}')
echo "RAM: $RAM" >> $LOG_FILE

# DISCO (% usado en /)
DISK=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
echo "DISK: $DISK" >> $LOG_FILE

echo "----------------------" >> $LOG_FILE
