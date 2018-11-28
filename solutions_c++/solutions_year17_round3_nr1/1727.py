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
   int n, k;
   cin >> n >> k;
   vector<pair<double, double>> cakes;
   for (int i = 0; i < n; ++i)
   {
      int r, h;
      cin >> r >> h;
      cakes.push_back(make_pair(r, h));
   }
   sort(all(cakes));
   reverse(all(cakes));
   double best = 0;
   const double pi = 3.14159265359;
   for (int i = 0; i < n - k + 1; ++i)
   {
      double r = cakes[i].first;
      double h = cakes[i].second;
      double cur = pi * r * r + 2 * pi * r * h;
      vector<double> curCakes;
      for (int j = 0; j < n; ++j)
      {
         if (i == j || cakes[j].first > cakes[i].first)
            continue;
         double r = cakes[j].first;
         double h = cakes[j].second;
         curCakes.push_back(2 * pi * r * h);
      }
      sort(all(curCakes));
      reverse(all(curCakes));
      for (int j = 0; j < k - 1; ++j)
      {
         cur += curCakes[j];
      }
      best = max(best, cur);
   }
   printf("Case #%d: %f\n", test, best);
}

int main()
{
   ios_base::sync_with_stdio(false);
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);

   int tests;
   scanf("%d", &tests);

   for (int test = 1; test <= tests; ++test)
   {
      fprintf(stderr, "Solving %d/%d\n", test, tests);
      solve(test);
   }

   return 0;
}
