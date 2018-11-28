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

std::string solve(const std::string& N, int startFrom)
{
   if (N.empty())
      return std::string();

   std::string result;
   ull input = std::stoull(N);

   for (int i = startFrom; i <= N[0] - '0'; ++i)
   {
      std::string temp(N.size(), i + '0');
      ull tempUll = std::stoull(temp);
      if (tempUll <= input)
      {
         result = temp;
         startFrom = std::max(startFrom, i);
      }
   }
   return result.empty() ? std::string(N.size() - 1, '9') :
      (result[0] + ((result[0] < N[0]) ? std::string(N.size() - 1, '9') : solve(N.substr(1), startFrom)));
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
      string N;
      input >> N;

      cout << "Case #" << currentTestCase++ << ": " << solve(N, 1) << '\n';
   }
}

