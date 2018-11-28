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
   double U;
   vector<double> ais;
   double ans;

   void read_input()
   {
      cin >> N >> K >> U;
      ais.resize(N);
      for(auto &ai: ais) cin >> ai;
      sort(ais.begin(), ais.end());
   }

   void solve()
   {
      ans = 0;

      RPT(i, N)
      {
         double sum = accumulate(ais.begin(), ais.begin() + i + 1, U);
         sum /= (double)(i + 1);
         if (sum > 1.0000000001) continue;
         if (sum + 0.000000001 < ais[i]) continue;
         double ans2 = 1.0;
         RPT(j, N)
         {
            if (j <= i)
            {
               ans2 *= sum;
            }
            else ans2 *= ais[j];
         }

         if (ans2 > ans) ans = ans2;
      }

   }

   void print_output()
   {
      cout << fixed << setprecision(9) << ans;
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

