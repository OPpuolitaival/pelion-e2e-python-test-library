"""
Copyright 2017 ARM Limited
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import logging
from serial import Serial, SerialException

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class SerialConnection:
    def __init__(self, port=None, baudrate=9600, timeout=1):
        self.ser = Serial(port, baudrate, timeout=timeout)

    def open(self):
        """
        Open serial port connection
        """
        if not self.ser.is_open:
            self.ser.open()

    def readline(self):
        """
        Read line from serial port
        :return: One line from serial stream
        """
        try:
            output = self.ser.readline()
            return output
        except SerialException as se:
            log.debug('Serial connection read error: {}'.format(se))
            return None

    def write(self, data):
        """
        Write data to serial port
        :param data: Data to send
        """
        try:
            self.ser.write(data)
        except SerialException as se:
            log.debug('Serial connection write error: {}'.format(se))

    def close(self):
        """
        Close serial port connection
        """
        self.ser.close()
