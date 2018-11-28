#include <vector>
#include <list>
#include <map>
#include <set>

#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <assert.h>
#include <boost/lexical_cast.hpp>

#define INF 1023123123
#define EPS 1e-11
#define LSOne(S) (S & (-S))

#define M_PI 3.14159265358979323846  /* pi */

#define FORN(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define FORB(X,Y) for (int (X) = (Y);(X) >= 0;--(X))
#define REP(X,Y,Z) for (int (X) = (Y);(X) < (Z);++(X))
#define REPB(X,Y,Z) for (int (X) = (Y);(X) >= (Z);--(X))

#define SZ(Z) ((int)(Z).size())
#define ALL(W) (W).begin(), (W).end()
#define PB push_back

#define MP make_pair
#define A first
#define B second

#define FORIT(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

bool next_combination(vector<int>& v, int k, int N) {
   // We want to find the index of the least significant element
   // in v that can be increased.  Let's call that index 'pivot'.
   int pivot = k - 1;
   while (pivot >= 0 && v[pivot] == N - k + pivot)
      --pivot;

   // pivot will be -1 iff v == {N - k, N - k + 1, ..., N - 1},
   // in which case, there is no next combination.
   if (pivot == -1)
      return false;

   ++v[pivot];
   for (int i = pivot + 1; i < k; ++i)
      v[i] = v[pivot] + i - pivot;
   return true;
}

bool almost_equal(double a, double b)
{
   return abs(a - b) < EPS;
}

void print_case(int i)
{
   cout << "Case #" << i + 1 << ": ";
}

int main()
{
   cout.precision(12);
   int ntc;
   cin >> ntc;

   FORN(kk, ntc)
   {
      print_case(kk);
      int c, n, m;
      cin >> n >> c >> m;
      vector<ii> ms(m);
      FORN(i, m)
      {
         cin >> ms[i].first >> ms[i].second;
         ms[i].first--;
         ms[i].second--;
      }

      vi tbc(c);
      vi tps(n);
      FORN(i, m)
      {
         tbc[ms[i].second]++;
         tps[ms[i].first]++;
      }
      int ans = max(tbc[0], tbc[1]);
      int numones = 0;
      FORN(i, m)
      {
         if (ms[i].first == 0)
            numones++;
      }
      ans = max(numones, ans);
      auto ss = max_element(tps.begin(), tps.end());

      cout << ans << ' ' << max(0, *ss - ans) << endl;
   }
}
