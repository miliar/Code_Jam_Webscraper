#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <limits>
#include <sstream>
#include <fstream>

using namespace std;
#define ll long long
#define x first
#define y second
#define pii pair<int, int>
#define pdd pair<double, double>
#define L(s) (int)(s).size()
#define vi vector<int>
#define all(s) (s).begin(), (s).end()
#define pb push_back
#define mp make_pair
#define inf 1000000000
#define pi 3.14159265358979323426264

#define sqr(x) ((x) * (x))
#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define REPD(i, n) for (int (i) = (n) - 1; (i) >= 0; (i)--)
#define FOR(i, a, b) for (int (i) = (a); (i) < (b); (i)++)
#define FORD(i,a, b) for (int (i) = (a); (i) >= (b); (i)--)
#define FORI(it, cont) for (auto (it) = (cont).begin(); (it) != (cont).end(); (it)++)
#define eps std::numeric_limits<double>::epsilon()

int main()
{
   freopen("A.in", "r", stdin);
   freopen("A_out.txt", "w", stdout);
   int t;
   int d, n;
   vector<pii> k;
   k.reserve(1000);
   cin >> t;
   double mintime = 0;
   cout.precision(6);
   cout.setf(std::ios::fixed, ios::floatfield);
   REP(test, t)
   {
      cin >> d >> n;
      mintime = 0;
      k.resize(n);
      REP(i, n) cin >> k[i].x >> k[i].y;

      REP(i, n)
      {
         double t1 = double (d - k[i].x) / double(k[i].y);
         if (t1 > mintime)
         {
            mintime = t1;
         }
      }
      double res = double(d) / mintime;

      cout << "Case #" << test + 1 << ": " << res << endl;
   }

   return 0;
}

