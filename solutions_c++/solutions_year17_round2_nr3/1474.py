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

double solveDP(size_t i, double prevE, double prevS, double curretTime, int n, vector<double>& e, vector<double>& s, vector<double>& d) {
   if (i == n-1) {
      return curretTime;
   }
   else {
      if (e[i] - d[i]<0) return solveDP(i + 1, prevE - d[i], prevS, curretTime + d[i] / prevS, n, e, s, d);
      if (prevE - d[i] < 0) return  solveDP(i + 1, e[i] - d[i], s[i], curretTime + d[i] / s[i], n, e, s, d);
      

      double r2 = solveDP(i+1, prevE - d[i], prevS, curretTime + d[i] / prevS, n, e,s,d);
      double r1 = solveDP(i + 1, e[i] - d[i], s[i], curretTime + d[i] / s[i], n, e, s, d);
      
      return min(r1, r2);

   }
}

void solve(int test)
{
   printf("Case #%d: ", test + 1);
   int n;
   cin >> n;
   int q;
   cin >> q;

   if (q != 1) {
      printf("FFFF");
      return;
   }

   vector<double > e(n);
   vector<double> s(n);
   for (size_t i = 0; i < n; ++i) {
      cin >> e[i];
      cin >> s[i];
   }
   int fullD = 0;
   vector<double> d(n);
   for (size_t i = 0; i < n; ++i) {
      for (size_t j = 0; j < n; ++j) 
      {
         int curD;
         cin >> curD;
         if (curD != -1) {
            d[i] = curD;
            fullD += curD;
         }
      }
   }

   int u;
   int v;
   for (size_t i = 0; i < q; ++i) {
      cin >> u;
      cin >> v;
   }

   double totalTime = 0;

   totalTime = solveDP(1, e[0]-d[0], s[0], d[0]/s[0], n , e,s, d);


   printf("%.6f\n", totalTime);

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
