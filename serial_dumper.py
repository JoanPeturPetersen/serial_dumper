#!python

"""
Usage: serial_dumper.py [--baudrate=BAUD] [--bytesize=BYTESIZE]
                        [--parity=PARITY] [--stopbits=STOPBITS] PORT

Options:
  -h, --help           show this help message and exit
  --baudrate=BAUD      Specify baud rate [default: 9600]
  --bytesize=BYTESIZE  Specify byte size [default: 8]
  --parity=PARITY      Specify parity bit, one of [N, E, O] [default: N]
  --stopbits=STOPBITS  Specify stop bits [1, 2, 1.5] [default: 1]

Example:
  serial_dumper --baudrate=4800 /dev/ttyr01
"""

from docopt import docopt
import serial
import sys


def dump_serial(ser_port, ser_baudrate, ser_bytesize, ser_parity,
        ser_stopbits):
    """
    """
    ser = serial.Serial(port=ser_port, baudrate=ser_baudrate,
        bytesize=ser_bytesize, parity=ser_parity, stopbits=ser_stopbits)
    try:
        while True:
            sys.stdout.write(ser.readline())
    except Exception, e:
        print "Communication problems: ", e
    try:
        ser.close()
    except:
        pass

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Serial dumper 1.0')
    #print arguments
    dump_serial(arguments['PORT'], ser_baudrate=arguments['--baudrate'],
        ser_bytesize=int(arguments['--bytesize']),
        ser_parity=arguments['--parity'],
        ser_stopbits=int(arguments['--stopbits']))
