#!/usr/bin/python3

import curses
import sys
import time

def waitFrame(start, fps, next_frame):
    while True:
        now = time.perf_counter()
        # Exit this function delta reaches time to display a next frame.
        if next_frame / fps <= now-start:
            return
def play(window, fname, set_fps):
    # Initialize start_time
    start_time = time.perf_counter()
    # curses.delay_output(0)

    try:
        f = open(fname)
        # Initialize counter of played out frames.
        framecount = 0
        # Display all lines in order.
        for line in f:
            # Reset cursor position after complete to show a frame.
            if line[0] == 'R':
                window.move(0, 0)
                # curses.delay_output(0)
                # Wait next frame
                waitFrame(start_time, set_fps, framecount)
                # Increase frame counter.
                framecount+=1
            else:
                # Output current line to stdout.
                window.addstr(line)
                # Refresh window.
                window.refresh()
    except curses.error:
        window.addstr(0, 0, "Windows size is too small")
        window.addstr(
            1, 0, "Required Windows Size X, Y: 161, 61 Current: %s, %s" % window.getmaxyx())
        window.addstr(2, 0, "Expand window size and try again.")
        window.addstr(3, 0, "Press any key to exit...")
        window.refresh()
        window.getch()
    except:
        raise

# Entry point of this application.
# Terminate the application if no argument set.
def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <file_name> <fps>")
        return
    fn_list = sys.argv[1]
    set_fps = int(sys.argv[2])
    curses.wrapper(play, fn_list, set_fps)
main()
