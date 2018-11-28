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

#define M_PI           3.14159265358979323846  /* pi */

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

void print_case(int i)
{
   cout << "Case #" << i + 1 << ": ";
}

bool almost_equal(double a, double b)
{
   return abs(a - b) < EPS;
}

double calc_failure(vector<double> vc)
{
   double prob = 1.0;
   FORN(i, vc.size())
   {
      prob *= vc[i];
   }
   return prob;
}

int main()
{
   cout.precision(12);
   int ntc;
   cin >> ntc;

   FORN(kk, ntc)
   {
      print_case(kk);
      int n, k;
      cin >> n >> k;
      double units;
      cin >> units;
      vector<double> cores(n+1);
      cores[n] = 1.0;
      FORN(i, n)
      {
         cin >> cores[i];
      }

      sort(cores.begin(), cores.end());

      FORN(i, n)
      {
         int nrcoresequal = 1;
         REP(j, 1, n)
         {
            if (!almost_equal(cores[i], cores[j]))
            {
               break;
            }
            nrcoresequal++;
         }
         double nextcore = cores[nrcoresequal];
         double diff = nextcore - cores[0];
         double tospend = min(units, nrcoresequal * diff);
         FORN(j, nrcoresequal)
         {
            cores[j] += tospend / nrcoresequal;
         }
         units -= tospend;
      }

      cout << calc_failure(cores) << endl;
   }
}
