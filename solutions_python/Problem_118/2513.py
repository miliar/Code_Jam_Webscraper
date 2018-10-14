#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from abc import abstractmethod, ABCMeta

class Solver(object):
  __metaclass__ = ABCMeta

  def __init__(self, inpath):
    self.fhi = open(inpath)
    self.fho = open('-out'.join(os.path.splitext(inpath)), 'w')
    self.cases = int(self.fhi.readline(), 10)
    self.run()

  @abstractmethod
  def run(self):
    pass

  def report(self, case, value):
    self.fho.write('Case #%d: %s\n' % (case, value))
