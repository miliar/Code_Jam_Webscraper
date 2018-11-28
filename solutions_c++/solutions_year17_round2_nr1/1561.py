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

bool check(ll dist, const vector<ll>& positions, const vector<ll>& speeds, double speed)
{
   const size_t n = positions.size();
   double myTime = dist / speed;
   for (int i = 0; i < n; ++i)
   {
      double otherTime = (dist - positions[i]) / (double)speeds[i];
      if (otherTime > myTime)
      {
         return false;
      }
   }
   return true;
}

void solve(int test)
{
   ll dist, n;
   cin >> dist >> n;

   vector<ll> positions(n);
   vector<ll> speeds(n);
   for (int i = 0; i < n; ++i)
   {
      cin >> positions[i] >> speeds[i];
   }
   if (test == 92)
   {
      test = test;
   }

   double l = 1e-6;
   double r = 1e20;
   for (int i = 0; i < 1000; ++i)
   {
      double delta = abs(r - l);
      double mid = (l + r) / 2.;
      if (check(dist, positions, speeds, mid))
      {
         l = mid;
      }
      else
      {
         r = mid;
      }
   }

   printf("Case #%d: %0.8f \n", test + 1, l);
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
