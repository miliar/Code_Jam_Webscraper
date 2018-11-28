#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <iomanip>
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
   ist N, P;
   vi data;
   ist ans;

   void read_input()
   {
      cin >> N >> P;
      data.resize(N);
      for(auto&d: data) cin >> d;
   }

   void solve()
   {
      ans = 0;
      vi ds(P);
      for(auto &d: data) ++ ds[d%P];
      ans = ds[0];
      ds[0] = 0;

      for(ist i = 1; 2 * i < P; ++ i)
      {
         ist t = min(ds[i], ds[P-i]);
         ans += t;
         ds[i] -= t;
         ds[P-i] -= t;
      }
      if (P%2 == 0)
      {
         ans += ds[P/2]/2;
         ds[P/2] %= 2;
      }
      if (P == 1) return;
      if (P == 2)
      {
         if (ds[1]) ans += 1;
         return;
      }
      if (P == 3)
      {
         ist t = ds[1] + ds[2];
         ans += t/3;
         if (t%3) ++ ans;
         return;
      }
      if (P == 4)
      {
         ist t = ds[1] + ds[3];
         if (ds[2]) t += 2;
         ans += t/P;
         if (t%P) ++ ans;
      }

   }

   void print_output()
   {
      cout << ans;
   }

   void execute()
   {
      read_input();
      solve();
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

