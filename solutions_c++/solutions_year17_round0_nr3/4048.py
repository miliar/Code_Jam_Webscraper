#include "stdafx.h"

#include <tuple>
#include <iostream>
#include <array>
#include <utility>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>

using ull = unsigned long long;

std::string solve(ull N, ull K)
{
   std::map<ull, ull> freeStallRegions = { {N,1} };
   for (int i = 0; i < K - 1; ++i)
   {
      auto freeStallRegion = freeStallRegions.rbegin();
      auto freeStallRegionLength = freeStallRegion->first;
      if (freeStallRegionLength % 2 == 0)
      {
         freeStallRegions[freeStallRegionLength/2] += 1;
         freeStallRegions[freeStallRegionLength / 2 - 1] += 1;
      }
      else
      {
         freeStallRegions[(freeStallRegionLength - 1) / 2] += 2;
      }
      if (freeStallRegion->second > 1)
      {
         freeStallRegion->second--;
      }
      else
      {
         freeStallRegions.erase(freeStallRegion->first);
      }
   }

   auto freeStallRegion = freeStallRegions.rbegin();

   std::ostringstream oss;
   auto freeStallRegionLength = freeStallRegion->first;
   if (freeStallRegionLength % 2 == 0)
   {
      oss << freeStallRegionLength / 2 << " " << freeStallRegionLength / 2 - 1;
   }
   else
   {
      oss << (freeStallRegionLength - 1) / 2 << " " << (freeStallRegionLength - 1) / 2;
   }
   return oss.str();
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
      ull N, K;
      input >> N >> K;

      cout << "Case #" << currentTestCase++ << ": " << solve(N, K) << '\n';
   }
}

