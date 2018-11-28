#include "stdafx.h"

#include <tuple>
#include <iostream>
#include <array>
#include <utility>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>

std::string solve(std::string pancakes, int k)
{
   int steps = 0;
   size_t length = pancakes.size();
   for (size_t i = 0; i <= length - k; ++i)
   {
      if (pancakes[i] == '-')
      {
         std::for_each(pancakes.begin() + i, pancakes.begin() + i + k, [](char& c) {c = (c == '+') ? '-' : '+'; });
         steps++;
      }
   }
   return pancakes.find('-') != std::string::npos ? "IMPOSSIBLE" : std::to_string(steps);
}

int main()
{
   using namespace std;
   std::fstream input("input.txt");
   int testCasesQty;
   input >> testCasesQty;

   int currentTestCase = 1;
   while (testCasesQty--)
   {
      string pancakes;
      input >> pancakes;
      int k;
      input >> k;

      cout << "Case #" << currentTestCase++ << ": " << solve(pancakes, k) << '\n';
   }
}

