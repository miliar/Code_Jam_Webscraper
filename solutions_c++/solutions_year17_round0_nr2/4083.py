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

void minusSymb(std::string& a, size_t pos)
{
   if (pos == 0 && a[pos] == '1')
   {
      a = std::string(a.size() - 1, '9');
   }
   else
   {
      if (a[pos] == '0')
      {
         minusSymb(a, pos - 1);
      }
      else
      {
         a[pos]--;
         if (pos > 0 && a[pos - 1] > a[pos])
         {
            minusSymb(a, pos - 1);
         }
         else
         {
            fill(a.begin() + pos + 1, a.end(), '9');
         }
      }
   }
}

int main()
{
   freopen("B-large.in", "r", stdin);
   freopen("B_out.txt", "w", stdout);
   int t;
   std::string a;
   cin >> t;
   REP(test, t)
   {
      cin >> a;

      size_t i = 1;
      while (i < a.size() && a[i - 1] <= a[i])
      {
         i++;
      }
      if (a.size() == i)
      {
         cout << "Case #" << test + 1 << ": " << a << endl;
         continue;
      }
      minusSymb(a, i - 1);

      cout << "Case #" << test + 1 << ": " << a << endl;
   }

   return 0;
}

