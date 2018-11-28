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

pair<ll, ll> decompose(ll num)
{
   pair<ll, ll> p;
   p.first = num % 2 == 0 ? num / 2 - 1 : num / 2;
   p.second = num / 2;
   return p;
}

void fill_ps(vector<vector<char>>& ps)
{
   int r = 0;
   for (int c = 0; c < ps.size(); c++)
   {
      if (ps[r][c] == '.')
      {
         ps[r][c] = '+';
      }
   }
   r = ps.size() - 1;
   for (int c = 1; c < ps.size() - 1; c++)
   {
      if (ps[r][c] == '.')
      {
         ps[r][c] = '+';
      }
   }
}

void fill_xs(vector<vector<char>>& xs)
{
   int r = 0;
   int fc = 0;
   for (int c = 0; c < xs.size(); c++)
   {
      if (xs[r][c] == 'x')
      {
         fc = c;
         break;
      }
   }
   for (r = 0; r < xs.size(); r++)
   {
      if (xs[r][fc] == '.')
      {
         xs[r][fc] = 'x';
      }
      fc = (fc + 1) % xs.size();
   }
}

vector<vector<char>> merge_diffs(vector<vector<char>>& ps, vector<vector<char>>& xs)
{
   auto ret = vector<vector<char>>(ps.size(), vector<char>(ps.size(), '.'));
   FORN(r, ps.size())
   {
      FORN(c, ps.size())
      {
         if (ps[r][c] == '+' && xs[r][c] == '.')
            ret[r][c] = '+';
         else if (ps[r][c] == '+' && xs[r][c] == 'x')
            ret[r][c] = 'o';
         else if (ps[r][c] == '.' && xs[r][c] == 'x')
            ret[r][c] = 'x';
      }
   }
   return ret;
}

bool validate(vector<vector<char>>& all)
{
   bool valid = true;
   FORN(r, all.size())
   {
      bool cross = false;
      FORN(c, all.size())
      {
         if (cross && (all[r][c] == 'o' || all[r][c] == 'x'))
         {
            valid = false;
         }
         cross |= (all[r][c] == 'o' || all[r][c] == 'x');
      }
   }
   FORN(c, all.size())
   {
      bool cross = false;
      FORN(r, all.size())
      {
         if (cross && (all[r][c] == 'o' || all[r][c] == 'x'))
         {
            valid = false;
         }
         cross |= (all[r][c] == 'o' || all[r][c] == 'x');
      }
   }
   return valid;
}

void print_diffs(vector<vector<char>>& old, vector<vector<char>>& new_)
{
   int beauty = 0;
   vector<string> out;
   FORN(r, old.size())
   {
      FORN(c, old.size())
      {
         if (new_[r][c] == 'x')
            beauty++;
         if (new_[r][c] == '+')
            beauty++;
         if (new_[r][c] == 'o')
            beauty += 2;

         if (old[r][c] != new_[r][c])
         {
            out.push_back(boost::lexical_cast<string>(new_[r][c]) + " " + boost::lexical_cast<string>(r + 1) + " " + boost::lexical_cast<string>(c + 1));
         }
      }
   }
   cout << beauty << ' ' << out.size() << endl;
   FORN(i, out.size())
   {
      cout << out[i] << endl;
   }
}

int main()
{
   int ntc;
   cin >> ntc;

   FORN(kk, ntc)
   {
      print_case(kk);
      int n, m;
      cin >> n >> m;
      vector<vector<char>> xs(n, vector<char>(n, '.'));
      vector<vector<char>> ps(n, vector<char>(n, '.'));
      vector<vector<char>> all(n, vector<char>(n, '.'));
      FORN(i, m)
      {
         char p;
         int r, c;
         cin >> p >> r >> c;
         r--;
         c--;
         if (p == 'o')
         {
            xs[r][c] = 'x';
            ps[r][c] = '+';
            all[r][c] = p;
         }
         else if (p == 'x')
         {
            xs[r][c] = p;
            all[r][c] = p;
         }
         else
         {
            ps[r][c] = '+';
            all[r][c] = p;
         }
      }

      fill_ps(ps);
      fill_xs(xs);
      auto res = merge_diffs(ps, xs);
      print_diffs(all, res);
   }
}
