#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def solve(naomi_blocks, ken_blocks):
  # war
  war_score = 0
  naomi_blocks_w = set(naomi_blocks)
  ken_blocks_w = set(ken_blocks)
  while naomi_blocks_w:
    # naomi
    naomi_block = max(naomi_blocks_w)
    naomi_blocks_w.remove(naomi_block)
    # ken
    candidates = tuple(filter(naomi_block.__lt__, ken_blocks_w))
    if not candidates:
      # naomi got point
      war_score += 1
      ken_block = min(ken_blocks_w)
    else:
      # ken got point
      ken_block = min(candidates)
    ken_blocks_w.remove(ken_block)
  # deceitful war
  deceitful_war_score = 0
  naomi_blocks_dw = set(naomi_blocks)
  ken_blocks_dw = set(ken_blocks)
  while naomi_blocks_dw:
    # naomi
    naomi_block = min(naomi_blocks_dw)
    if min(naomi_blocks_dw) < min(ken_blocks_dw):
      fake_naomi_block_candidates = tuple(filter(naomi_block.__lt__, ken_blocks_dw))
      fake_naomi_block_candidates = sorted(fake_naomi_block_candidates, reverse=True)
      if len(fake_naomi_block_candidates) > 1:
        fake_naomi_block = (fake_naomi_block_candidates[0] + fake_naomi_block_candidates[1]) / 2
      else:
        fake_naomi_block = naomi_block
    else:
      fake_naomi_block = 1.0
    naomi_blocks_dw.remove(naomi_block)
    # ken
    candidates = tuple(filter(fake_naomi_block.__lt__, ken_blocks_dw))
    if not candidates:
      # naomi got point
      deceitful_war_score += 1
      ken_block = min(ken_blocks_dw)
    else:
      # ken got point
      ken_block = min(candidates)
    ken_blocks_dw.remove(ken_block)
  return deceitful_war_score, war_score


if __name__ == "__main__":
  input_filepath = sys.argv[1]

  with open(input_filepath, "rt") as input_file:
    T = int(next(input_file))

    for i in range(1, T + 1):
      N = int(next(input_file))
      naomi_blocks = tuple(map(float, next(input_file).split(" ")))
      ken_blocks = tuple(map(float, next(input_file).split(" ")))
      assert(len(naomi_blocks) == N)
      assert(len(ken_blocks) == N)
      sol = solve(naomi_blocks, ken_blocks)
      print("Case #%u: %u %u" % (i, sol[0], sol[1]))

    assert(i == T)
