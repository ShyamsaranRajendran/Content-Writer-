#!/bin/bash

FILE_PATH="your_text_file.txt"  
TYPING_DELAY=10

IFS=$'\n' 
while read -r line; do
    xdotool type --delay $TYPING_DELAY "$line"
    xdotool key Return
done < "$FILE_PATH"

unset IFS
