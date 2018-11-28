#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <chrono>
#include <numeric>
#include <limits>

using namespace std;

typedef ptrdiff_t ist;
typedef size_t iut;
typedef vector<ist> vi;
typedef pair<ist, ist> pii;

#define RPT(i, k) for(ist i = 0; i < k; ++ i)

#define INF (numeric_limits<ist>::max())

bool trailing_space = true; // for output

struct Solver
{
   ist AC, AJ;
   ist min_s;
   map<pii, ist> int_12;
   map<pii, ist> intervals;
   vector<pii> cs;
   vector<pii> js;
   ist ans;
   ist sum_c;
   ist sum_j;

   void read_input()
   {
      cin >> AC >> AJ;
      cs.resize(AC);
      js.resize(AJ);
      min_s = 1440000;

      for(auto&v:cs)
      {
         cin >> v.first >> v.second;
         if (v.first < min_s) min_s = v.first;
      }
      for(auto&v:js)
      {
         cin >> v.first >> v.second;
         if (v.first < min_s) min_s = v.first;
      }
   }

   void solve()
   {

      sum_c = sum_j = 0;
      for(auto&v:cs)
      {
         v.first -= min_s;
         v.second -= min_s;
         int_12[v] = 1;
         sum_c += v.second - v.first;
      }
      for(auto&v:js)
      {
         v.first -= min_s;
         v.second -= min_s;
         int_12[v] = 2;
         sum_j += v.second - v.first;
      }

      ans = 0;

      ist end = 0;

      ist color = int_12.begin()->second;
      
      for(auto & iter: int_12)
      {
         if (iter.second != color)
         {
            ++ ans;
            color = iter.second;
         }
         else if (iter.first.first > end)
         {
            intervals[pii(iter.first.first-end, end)] = color;
         }
         end = iter.first.second;
      }

      auto last = int_12.rbegin();
      if (last->second !=  int_12.begin()->second)
      {
         ++ ans;
      }
      else if (last->first.second != 1440)
      {
         intervals[pii(1440 - last->first.second, last->first.second)] = color;
      }

      ist sums[3] = {0, sum_c, sum_j};
      for(auto & iter: intervals)
      {
         sums[iter.second] += iter.first.first;
         if (sums[iter.second] > 720) ans += 2;
      }
   }

   void print_output()
   {
      cout << ans;
   }

   void execute()
   {
      read_input();
      chrono::time_point<chrono::high_resolution_clock> start = chrono::high_resolution_clock::now();
      solve();
      chrono::time_point<chrono::high_resolution_clock> finish = chrono::high_resolution_clock::now();
      cerr << "PERF: size: " << AC + AJ << " time: " << chrono::duration_cast<chrono::microseconds>(finish - start).count() << " us\n";
      print_output();
   }
};


int main()
{
   int T = 0;
   cin >> T;
   for (int i = 0; i < T; ++ i)
   {
      cerr << "Solving Case #" << i + 1 << '\n';
      cout << "Case #" << i + 1 << ':';
      if (trailing_space) cout << ' ';
      Solver s;
      s.execute();
      cout << '\n';
   }

   return 0;
}

