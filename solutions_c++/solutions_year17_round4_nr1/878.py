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
      int n, p;
      cin >> n >> p;
      vi g(n);
      vi cnt(p);
      FORN(i, n)
      {
         cin >> g[i];
         g[i] %= p;
         cnt[g[i]]++;
      }
      vi sch(n);
      int pos = 0;
      if (p == 4)
      {
         while (cnt[0] > 0)
         {
            sch[pos] = 0;
            cnt[0]--;
            pos++;
         }
         while (cnt[2] > 2)
         {
            sch[pos] = sch[pos + 1] = 2;
            cnt[2] -= 2;
            pos += 2;
         }
         while (cnt[3] > 0 && cnt[1] > 0)
         {
            sch[pos] = 3; sch[pos + 1] = 1;
            cnt[3] -= 1;
            cnt[1] -= 1;
            pos += 2;
         }
         while (cnt[2] > 0 && cnt[1] > 1)
         {
            sch[pos] = 2; sch[pos + 1] = 1; sch[pos + 2] = 1;
            cnt[2] -= 1;
            cnt[1] -= 2;
            pos += 3;
         }
         while (cnt[3] > 1 && cnt[2] > 0)
         {
            sch[pos] = 3; sch[pos + 1] = 3; sch[pos + 2] = 2;
            cnt[2] -= 1;
            cnt[3] -= 2;
            pos += 3;
         }
         while (cnt[1] > 3)
         {
            sch[pos] = sch[pos+1] = sch[pos+2] = sch[pos+3] = 1;
            cnt[1]-=4;
            pos+=4;
         }
         while (cnt[3] > 0 && cnt[2] > 1 && cnt[1] > 0)
         {
            sch[pos] = 3; sch[pos + 1] = 2; sch[pos + 2] = 2; sch[pos + 3] = 1;
            cnt[2] -= 2;
            cnt[3] -= 1;
            cnt[1] -= 1;
            pos += 4;
         }
         while (cnt[3] > 3)
         {
            sch[pos] = 3; sch[pos + 1] = 3; sch[pos + 2] = 3; sch[pos + 3] = 3;
            cnt[3] -= 4;
            pos += 4;
         }
         while (cnt[3] > 2 && cnt[2] > 0 && cnt[1] > 0)
         {
            sch[pos] = 3; sch[pos + 1] = 3; sch[pos + 2] = 3; sch[pos + 3] = 2; sch[pos + 4] = 1;
            cnt[2] -= 1;
            cnt[3] -= 3;
            cnt[1] -= 1;
            pos += 5;
         }
         while (cnt[3] > 0 && cnt[2] > 0 && cnt[1] > 2)
         {
            sch[pos] = 3; sch[pos + 1] = 2; sch[pos + 2] = 1; sch[pos + 3] = 1; sch[pos + 4] = 1;
            cnt[2] -= 1;
            cnt[3] -= 1;
            cnt[1] -= 3;
            pos += 5;
         }
         while (cnt[3] > 2 && cnt[1] > 2)
         {
            sch[pos] = 3; sch[pos + 1] = 3; sch[pos + 2] = 3; sch[pos + 3] = 1; sch[pos + 4] = 1; sch[pos + 5] = 1;
            cnt[3] -= 3;
            cnt[1] -= 3;
            pos += 6;
         }
      }
      else if (p == 3)
      {
         while (cnt[0] > 0)
         {
            sch[pos] = 0;
            cnt[0]--;
            pos++;
         }
         while (cnt[1] > 0 && cnt[2] > 0)
         {
            sch[pos] = 1; sch[pos + 1] = 2;
            cnt[1] -= 1;
            cnt[2] -= 1;
            pos += 2;
         }
         while (cnt[1] > 2)
         {
            sch[pos] = 1; sch[pos + 1] = 1; sch[pos + 2] = 1;
            cnt[1] -= 3;
            pos += 3;
         }
         while (cnt[2] > 2)
         {
            sch[pos] = 2; sch[pos + 1] = 2; sch[pos + 2] = 2;
            cnt[2] -= 3;
            pos += 3;
         }
      }
      else if (p == 2)
      {
         while (cnt[0] > 0)
         {
            sch[pos] = 0;
            cnt[0]--;
            pos++;
         }
         while (cnt[1] > 0)
         {
            sch[pos] = 1;
            cnt[1] -= 1;
            pos += 1;
         }
      }

      FORN(i, p)
      {
         while (cnt[i] > 0)
         {
            sch[pos] = i;
            cnt[i]--;
            pos++;
         }
      }

      int off = 1;
      int sum = 0;
      FORN(i, n-1)
      {
         sum += sch[i];
         if (sum % p == 0)
            off++;
      }
      cout << off << endl;
   }
}
