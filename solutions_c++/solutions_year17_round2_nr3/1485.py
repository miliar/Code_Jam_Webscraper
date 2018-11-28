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
   int n, q;
   cin >> n >> q;

   vector<pair<double, double>> horses(n);
   for (int i = 0; i < n; ++i)
   {
      double e, s;
      cin >> e >> s;
      horses[i] = make_pair(e, s);
   }

   vector<int> roads(n - 1);
   for (int i = 0; i < n; ++i)
   {
      for (int j = 0; j < n; ++j)
      {
         int x;
         cin >> x;
         if (x != -1)
            roads[i] = x;
      }
   }

   for (int i = 0; i < q; ++i)
   {
      int u, k;
      cin >> u >> k;
   }

   if (test == 42)
   {
      test = test;
   }

   vector<double> times(n);
   for (int i = 1; i < n; ++i)
   {
      int dist = roads[i - 1];
      double bestHorse = (i > 1) ? 1e30 : 0.;
      for (int k = 0; k < i - 1; ++k)
      {
         if (times[k] > 0. && horses[k].first >= 0)
         {
            pair<double, double>& horse = horses[k];
            double speed = horse.second;
            bestHorse = min(bestHorse, times[k]);
            times[k] += dist / speed;
            horse.first -= dist;
         }
      }
      pair<double, double>& horse = horses[i - 1];
      double speed = horse.second;
      times[i - 1] = bestHorse + dist / speed;
      horse.first -= dist;
   }

   double ans = 1e30;
   for (int k = 0; k < n; ++k)
   {
      if (times[k] > 0. && horses[k].first >= 0)
      {
         ans = min(ans, times[k]);
      }
   }

   printf("Case #%d: %0.8f \n", test + 1, ans);
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
