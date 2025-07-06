#!/usr/bin/env python3

import os
from datetime import datetime
import argparse

# --- Configuration ---
LOG_DIR = "/home/ignito/docs/p_120/pomodoro_log"  # Replace with your actual absolute path  # inside your project-120 folder
os.makedirs(LOG_DIR, exist_ok=True)

def get_today_filename():
    return datetime.now().strftime("%Y-%m-%d") + ".md"

def log_entry(start, end, session_type, description):
    filename = os.path.join(LOG_DIR, get_today_filename())

    with open(filename, "a") as f:
        if os.stat(filename).st_size == 0:
            f.write(f"# 🧠 Study Log: {datetime.now().strftime('%Y-%m-%d')}\n\n")
            f.write("## 🎯 Slot Format: [Start - End] ⏱️ Duration\n\n")
            f.write("### ✅ Pomodoro Sessions\n\n")

        f.write(f"- [{start} - {end}]  {'✅ In' if session_type == 'study' else '☕ Out'} \t '{description}' \n")

    print(f"✅ Logged in: {filename}")

# --- CLI Interface ---
parser = argparse.ArgumentParser(description="Log your Pomodoro study sessions.")
parser.add_argument("--start", help="Start time in HH:MM (24hr)", required=False)
parser.add_argument("--end", help="End time in HH:MM (24hr)", required=False)
parser.add_argument("--type", choices=["study", "break"], required=True, help="Type of session")
parser.add_argument("--desc", required=True, help="Short description of what you did")

args = parser.parse_args()

# Default to current time if start/end not given
now = datetime.now().strftime("%H:%M")
start_time = args.start if args.start else now
end_time = args.end if args.end else now

log_entry(start_time, end_time, args.type, args.desc)
