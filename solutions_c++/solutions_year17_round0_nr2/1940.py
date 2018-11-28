#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <iomanip>
#include <array>
#include <math.h>
#include <cassert>
#include <limits>
#include <memory.h>

//#pragma comment(linker,"/STACK:102400000,102400000") // 100 mb

#pragma warning(disable : 4996)

using namespace std;

#define all(c) (c).begin(), (c).end()

typedef long long ll;
typedef unsigned long long ull;

void solve(int test)
{
   string s;
   cin >> s;

   const size_t n = s.length();

   int nonDecrease = -1;
   for (int i = 0; i < n - 1; ++i)
   {
      if (s[i] > s[i + 1])
      {
         nonDecrease = i;
         break;
      }
   }

   if (nonDecrease != -1)
   {
      char ch = s[nonDecrease];
      if (ch == '1')
         s.assign(n - 1, '9');
      else
      {
         auto pos = s.find_first_of(ch);
         s[pos]--;
         fill(s.begin() + pos + 1, s.end(), '9');
      }
   }

   printf("Case #%d: %s \n", test + 1, s.c_str());
}

int main()
{
   ios_base::sync_with_stdio(false);
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);

   int tests;
   scanf("%d", &tests);

   for (int test = 0; test < tests; ++test)
   {
      fprintf(stderr, "Solving %d/%d\n", test + 1, tests);
      solve(test);
   }

   return 0;
}
