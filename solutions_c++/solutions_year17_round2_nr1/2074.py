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

#define INF (numeric_limits<double>::max())

bool trailing_space = true; // for output

struct Solver
{
   double D;
   ist N;
   vector<pair<double, double> > hs;
   double ans;

   void read_input()
   {
      cin >> D >> N;
      hs.resize(N);
      for(auto &h: hs) cin >> h.first >> h.second;
   }

   void solve()
   {
      ans = INF;

      for(auto & h: hs)
      {
         double s = h.second + (h.first * h.second)/(D - h.first);
         if (s < ans) ans = s;
      }
   }

   void print_output()
   {
      cout <<  fixed << setprecision(6) <<  ans;
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

