#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <limits>

#include <queue>

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
   ist N, C, M;
   vector<pii> ts;
   ist ans;
   ist pms;

   void read_input()
   {
      cin >> N >> C >> M;
      ts.resize(M);
      for(auto&t:ts) cin >> t.first >> t.second;
   }

   void solve2()
   {
      if (N == 1)
      {
         ans = M;
         return;
      }
      vector<vi> ps(N, vi(2));
      for(auto&t:ts)
      {
         ++ ps[t.first - 1][t.second - 1];
      }
      for(ist i = 0; i < 2; ++ i)
      {
         priority_queue<pii> q;
         for(ist j = 1; j < N; ++ j)
         {
            if (ps[j][1-i])q.push(pii(ps[j][0] + ps[j][1], j));
         }
         while(ps[0][i] && q.size())
         {
            ++ ans;
            -- ps[0][i];
            auto x = q.top();
            q.pop();
            --x.first;
            --ps[x.second][1-i];
            if (ps[x.second][1-i]) q.push(x);
         }
      }
      if (ps[0][0] + ps[0][1])
      {
         RPT(i, N) ans += ps[i][0] + ps[i][1];
         return;
      }

      while(true)
      {
         ist max_c = -1;
         ist max_p = -1;
         ist max_t = 0;

         RPT(i, N)
         {
            if (ps[i][0] + ps[i][1] > max_t)
            {
               max_t = ps[i][0] + ps[i][1];
               max_p = i;
               if (ps[i][0] >= ps[i][1])
               {
                  max_c = 0;
               }
               else
               {
                  max_c = 1;
               }
            }
         }

         if (max_t == 0) return;

         priority_queue<pii> q;
         for(ist i = 0; i < N; ++ i)
         {
            if (i != max_p && ps[i][1-max_c])q.push(pii(ps[i][0] + ps[i][1], i));
         }

         if (!q.size())
         {
            vi sums(2);
            RPT(i, N)RPT(j, 2) if (i != max_p)sums[j] += ps[i][j];
            ist x = min(ps[max_p][1-max_c], sums[max_c]);
            sums[max_c] -= x;
            ps[max_p][1-max_c] -= x;
            ans += x;
            ans += sums[max_c] + ps[max_p][max_c];
            pms = ps[max_p][1-max_c];
            return;
         }
         auto x = q.top();
         ++ ans;
         -- ps[x.second][1 - max_c];
         -- ps[max_p][max_c];
      }
   }

   void solve()
   {
      ans = 0;
      pms = 0;
      if (C == 2)
      {
         solve2();
         return;
      }
   }

   void print_output()
   {
      cout << ans << ' ' << pms;
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

