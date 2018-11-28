#define _CRT_SECURE_NO_WARNINGS

#include <math.h>
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
#include <tuple>
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
   int n;
   int k;
   cin >> n;
   cin >> k;
   vector<pair<double, double>> pk;

   const double pi = 3.14159265359;

   for (int i = 0; i < n; ++i) {
      int r;
      int h;
      cin >> r;
      cin >> h;
      
      pk.push_back(make_pair(r,h));
   }
   /*
   sort(pk.begin(), pk.end(),  [](const pair<int, int>& a, const pair<int, int>& b) {
      return long(b.first) * long(b.second) < long(a.first) * long(a.second);
   });*/

   double result = 0;

   for (int i = 0; i < n; ++i) {
      double  r = pk[i].first;
      double  h = pk[i].second;
      double localRes = pi*r*r+ 2.0 * pi*r*h;

      vector<double> availableCakes;

      for (int ii = 0; ii < n; ++ii) {
         if (ii == i || pk[ii].first > pk[i].first) continue;
         availableCakes.push_back(2 * pi*pk[ii].first*pk[ii].second);
      }
      sort(availableCakes.begin(), availableCakes.end());
      reverse(availableCakes.begin(), availableCakes.end());
      if (availableCakes.size()<k-1) continue;
      for (int j = 0; j < k - 1 && j<availableCakes.size(); ++j) {
         localRes += availableCakes[j];
      }
      

      if (localRes > result) result = localRes;

   }


   

   printf("%f\n", result);

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
