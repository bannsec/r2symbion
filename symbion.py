#!/usr/bin/env python3

import r2lang
import sys
import angr, claripy
#import multiprocessing
#import threading
from time import sleep

class R2Symbion(object):

    def __init__(self):
        pass
        #self.project = angr.Project(r2.cmdj['ij']['core']['file'])

    def _call(self, s):
        s = s.lower()

        # Not for us
        if not s.startswith('symb'):
            return

        print('doing it')
        p = angr.Project(r2.cmdj('ij')['core']['file'])
        #p = threading.Thread(target=angr.Project, args=[r2.cmdj('ij')['core']['file']])
        print('blerg')
        #p.start()
        #p.join()
        #print('blerg')
        #self.project = angr.Project(r2.cmdj['ij']['core']['file'])

    def plugin(self, a):
        return {
            "name": "R2Symbion",
            "licence": "GPLv3",
            "desc": "Integration plugin for angr Symbion.",
            "call": self._call,
        }

r2symb = R2Symbion()
success = r2lang.plugin("core", r2symb.plugin)
