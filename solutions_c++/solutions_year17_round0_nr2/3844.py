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
#include <cmath>
#include <limits>
#include <cassert>
#include <math.h>
#include <memory.h>

//#pragma comment(linker, "/STACK:134217728")

using namespace std;
using namespace tr1;

#define all(c) (c).begin(), (c).end()
#define CLEAR(x) memset(x,0,sizeof x)

typedef long long ll;
typedef unsigned long long ull;

void solve(int test)
{
   printf("Case #%d: ", test + 1);
   string n;
   cin >> n;
   if (n.length() == 1) {
      printf("%s\n", n.c_str());
      return;
   }
   bool isTidy = true;
   size_t lastInc = 0;
   size_t i = 1;
   while (i < n.length()) {
      if (n[i] >= n[i - 1]) {
         if (n[i] > n[i - 1]) {
            lastInc = i;
         }
         ++i;
      }
      else {
         isTidy = false;
         break;
      }
   }

   if (isTidy) {
      printf("%s\n", n.c_str());
      return;
   }

   string result;
   result += n.substr(0, lastInc);
   result += n[lastInc] - 1;
   result.append(n.length() - lastInc-1, '9');

   i = 0;
   while (result[i] == '0') {
      ++i;
   }

   result = result.substr(i, result.length() - i);
   printf("%s\n", result.c_str());
}

int main()
{
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
