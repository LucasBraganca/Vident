#!/bin/python3

import argparse
import sys
import traceback

from veriloggen import from_verilog

if sys.version_info < (2, 7):
    import commands
else:
    import subprocess


def commands_getoutput(cmd):
    if sys.version_info < (2, 7):
        return commands.getoutput(cmd)
    else:
        byte_out = subprocess.check_output(cmd.split())
        str_out = byte_out.decode("utf-8")
        return str_out


parser = argparse.ArgumentParser()
parser.add_argument("filename", nargs='+')
args = parser.parse_args()

for file in args.filename:
    try:
        m = from_verilog.read_verilog_module(file)
        with open(file, 'w') as f:
            for mm in m.keys():
                f.write(m[mm].to_verilog())
        f.close()
    except:
        print(traceback.format_exc())

commands_getoutput('rm -rf parser.out parsetab.py')
