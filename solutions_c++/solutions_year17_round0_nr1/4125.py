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

int flips(const std::string& s, int k)
{
   vector<bool> b(s.size());
   REP(i, L(s))
   {
      b[i] = (s[i] == '+');
   }
   int counter = 0;
   REP(i, L(b) - k + 1)
   {
      if (!b[i])
      {
         counter++;
         REP(j, k)
         {
            b[i + j] = !b[i + j];
         }
      }
   }
   FOR(i, L(b) - k, L(b))
   {
      if (!b[i])
      {
         return -1;
      }
   }
   return counter;
}

int main()
{
   freopen("A-large.in", "r", stdin);
   freopen("A_out.txt", "w", stdout);
   int t;
   std::string a;
   int k;
   cin >> t;
   REP(test, t)
   {
      cin >> a >> k;
      int res = flips(a, k);
      if (res < 0)
      {
         cout << "Case #" << test + 1 << ": IMPOSSIBLE" << endl;

      }
      else
         cout << "Case #" << test + 1 << ": " << res << endl;
   }

   return 0;
}

