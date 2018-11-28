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
   ist N, K;
   vector<pair<double, double> > ps;
   double ans;

   void read_input()
   {
      cin >> N >> K;
      ps.resize(N);
      for(auto &p: ps) cin >> p.first >> p.second;
   }

   void solve()
   {
      ans = 0;

      RPT(i, N)
      {
         double ans2 = ps[i].first * ps[i].first + 2 * ps[i].first * ps[i].second;
         vector<double> ps2;
         RPT(j, N)
         {
            if (j == i || ps[j].first > ps[i].first) continue;
            ps2.push_back(2*ps[j].first * ps[j].second);
         }

         if (ps2.size() + 1 < K) continue;

         sort(ps2.begin(), ps2.end());

         ans2 = accumulate(ps2.end() - K + 1, ps2.end(), ans2);

         if (ans2 > ans) ans = ans2;

      }

      ans *= 3.141592653589793238463;
   }

   void print_output()
   {
      cout << fixed << setprecision(9) <<  ans;
   }

   void execute()
   {
      read_input();
      chrono::time_point<chrono::high_resolution_clock> start = chrono::high_resolution_clock::now();
      solve();
      chrono::time_point<chrono::high_resolution_clock> finish = chrono::high_resolution_clock::now();
      cerr << "PERF: size: " << N << " time: " << chrono::duration_cast<chrono::microseconds>(finish - start).count() << " us\n";
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

