module Main where

import Debug.Trace
import System( getArgs )
import Text.Printf


match_count "" "" = 1
match_count "" _ = 1
match_count _ "" = 0
match_count (pattern:patterns) (str:strs) | pattern == str = mod (match_count patterns strs + match_count (pattern:patterns) strs) 1000
match_count patterns (str:strs) = match_count patterns strs

_match_count (a1:a2:_) = printf "%04d\n" result
                         where result = (mod (match_count a1 a2) 10000) :: Int

main = do
    args <- getArgs
    _match_count args


