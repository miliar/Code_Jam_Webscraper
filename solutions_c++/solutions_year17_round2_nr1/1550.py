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
   int d, k;
   cin >> d;
   cin >> k;
   
   vector<pair<double, double>> horses(k);

   int hp;
   int hs;
   for (size_t i = 0; i < k; ++i) {
      cin >> hp;
      cin >> hs;
      horses[i] = make_pair(hp, hs);
   }

   sort(horses.begin(), horses.end(), [d](const pair<int, int>& a, const pair<int, int>& b) {
      return double (d-a.first)/double(a.second) < double(d - b.first) / double(b.second);
   });
   double totalTime = 0;
   for (size_t i = 0; i < k - 1; ++i) {
      if (horses[i].second == horses[i + 1].second) continue;
      if (horses[i].first < horses[i + 1].first && horses[i].second <= horses[i + 1].second) continue;
      if (horses[i].first > horses[i + 1].first && horses[i].second >= horses[i + 1].second) continue;

      double h1p = horses[i].first;
      double h1s = horses[i].second;
      double h2p = horses[i + 1].first;
      double h2s = horses[i + 1].second;

      double t =  (h2p - h1p) / (h1s - h2s);
      double p = (h1p) + (h1s)*t;
      totalTime += t;

      for (size_t j = i + 1; j < k; ++j) {
         horses[j].first += horses[j].second * t;
      }
   }
   totalTime += double(d - horses[k - 1].first) / double(horses[k - 1].second);
   double result = double(d) / totalTime;
   printf("%.6f\n", result);
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
