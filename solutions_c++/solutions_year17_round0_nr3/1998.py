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
   ll n, k;
   cin >> n >> k;

   ll t = 1;
   ll sum = 0;
   ll x;
   while (true)
   {
      if (t == k)
      {
         x = n / t;
         break;
      }
      if (t > k)
      {
         t /= 2;
         sum -= t;
         ll leftTotal = n - sum;
         ll left = k - sum;
         x = n / t;
         if (x * left + (x - 1) * (t - left) > leftTotal)
         {
            --x;
         }
         break;
      }
      sum += t;
      t *= 2;
   }

   if (x)
      --x;
   ll l = x / 2;
   ll r = x - l;
   printf("Case #%d: %lld %lld\n", test + 1, max(l, r), min(l, r));
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
