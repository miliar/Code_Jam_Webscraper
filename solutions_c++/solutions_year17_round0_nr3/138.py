#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <chrono>
#include <numeric>

using namespace std;

typedef ptrdiff_t ist;
typedef size_t iut;
typedef vector<ist> vi;
typedef pair<ist, ist> pii;

bool trailing_space = true; // for output

map<pii, pii> caches;

struct Solver
{
   ist N, K;
   pii ans;

   void read_input()
   {
      cin >> N >> K;
   }

   pii & solve(pii &k)
   {
      auto iter = caches.find(k);
      if (iter != caches.end()) return iter->second;
      auto &res = caches[k];

      if (k.second == 0)
      {
         res.first = k.first/2;
         res.second = (k.first-1)/2;
         return res;
      }

      pii k1(k.first/2, k.second/2);
      pii k2((k.first-1)/2, (k.second-1)/2);

      auto & r1 = solve(k1);
      auto & r2 = solve(k2);

      if (r1.second > r2.second || (r1.second == r2.second && r1.first > r2.first))
         res = r1;
      else res = r2;
      return res;
   }

   void solve()
   {
      pii k(N, K - 1);

      ans = solve(k);
   }

   void print_output()
   {
      cout << ans.first << ' ' << ans.second;
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

