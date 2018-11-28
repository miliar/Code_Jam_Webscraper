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
#include <climits>
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
   freopen("C-small-2-attempt0.in", "r", stdin);
   freopen("C_out.txt", "w", stdout);
   int t;
   ll n, k;
   ll res1, res2;
   cin >> t;
   REP(test, t)
   {
      cin >> n >> k;
      ll i = 0;
      ll p2 = 1;
      while (1 << (i + 1) <= k)
      {
         i++;
      }
      p2 = 1 << i;
      ll leftDots = n - p2 + 1;
      ll minD = leftDots / p2;
      ll countBig = leftDots % p2;
      if (k - p2 < countBig)
      {
         res1 = minD / 2;
         res2 = minD - res1;
      }
      else
      {
         res1 = (minD - 1) / 2;
         res2 = minD - res1 - 1;
      }
      cout << "Case #" << test + 1 << ": " << res2 << ' ' << res1 << endl;
   }

   return 0;
}

