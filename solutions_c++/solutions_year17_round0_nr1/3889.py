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

void flip(string& s, size_t pos, size_t sz) {
   for (size_t i = pos; i < pos + sz; ++i) {
      if (s[i] == '-') s[i] = '+';
      else s[i] = '-';
   }

}

void solve(int test)
{
   printf("Case #%d: ", test + 1);
   string s;
   cin >> s;
   int k;
   cin >> k;

   int flips = 0;

   for (size_t i = 0; i < s.length()-k+1; ++i) {
      if (s[i] == '-') {
         flip(s, i, k);
         ++flips;
      }
   }
   
   for (size_t i = s.length() - k; i < s.length(); ++i) {
      if (s[i] == '-') {
         printf("IMPOSSIBLE\n");
         return;
      }
   }

   printf("%d\n", flips);

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
