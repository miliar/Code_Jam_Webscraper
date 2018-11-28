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

struct Solver
{
   ist N;
   vi pls; // +
   vi diags; // x
   ist ans;
   vi in;
   vi out;

   vector<vi> edges;

   ist index(ist r, ist c)
   {
      return r * N + c;
   }

   void solve_diags()
   {
      set<ist> rows;
      set<ist> cols;

      for(ist i = 0; i < N; ++ i)
      {
         rows.insert(i);
         cols.insert(i);
      }

      for(ist r = 0; r < N; ++ r)
         for(ist c = 0; c < N; ++ c)
            if (diags[index(r,c)])
            {
               rows.erase(r);
               cols.erase(c);
            }

      for(auto i1 = rows.begin(), i2 = cols.begin(); i1 != rows.end() && i2 != cols.end(); ++ i1, ++ i2)
      {
         ++ ans;
         out[index(*i1, *i2)] = 2;
      }
   }

   // bipartie match
   void solve_pls()
   {
      edges.assign(2 * N - 1, vi(2 * N - 1));

      for(ist r = 0; r < N; ++ r)
         for(ist c = 0; c < N; ++ c)
         {
            edges[r+c][N - 1 + r - c] = 1;
         }
      for(ist r = 0; r < N; ++ r)
         for(ist c = 0; c < N; ++ c)
         {
            if (pls[index(r,c)])
            {
               ist x = r + c;
               ist y = N - 1 + r - c;
               for(ist z = 0; z < 2 * N - 1; ++ z)
               {
                  edges[x][z] = 0;
                  edges[z][y] = 0;
               }
            }
         }
      // now find maximum match

      vi matches(2 * N - 1, -1);

      for (ist j = 0; j < 2 * N - 1; ++ j)
      {
         vi visited(2 * N - 1);
         dfs(j, visited, matches);
      }

      for(ist x = 0; x < 2 * N - 1; ++ x)
      {
         if (matches[x] == -1) continue;
         ist y = matches[x];
         ist r = (x + y + 1 - N) / 2;
         ist c = (x - y + N - 1) / 2;
         ++ ans;
         out[index(r,c)] |= 1;
      }
   }

   bool dfs(ist j, vi & visited, vi & matches)
   {
      for (ist i = 0; i < 2 * N - 1; ++ i)
      {
         if (edges[i][j] && !visited[i])
         {
            visited[i] = 1;

            if (matches[i] < 0 || dfs(matches[i], visited, matches))
            {
               matches[i] = j;
               return true;
            }
         }
      }
      return false;
   }

   void read_input()
   {
      ans = 0;
      cin >> N;
      pls.resize(N * N);
      diags.resize(N * N);
      in.resize(N * N);
      ist M;
      cin >> M;
      for(ist i = 0; i < M; ++ i)
      {
         char s;
         ist r, c;
         cin >> s >> r >> c;
         -- r;
         -- c;
         if (s == '+' || s == 'o')
         {
            pls[index(r,c)] = 1;
            in[index(r,c)] += 1;
            ++ ans;
         }
         if (s == 'x' || s == 'o')
         {
            diags[index(r,c)] = 1;
            in[index(r,c)] += 2;
            ++ ans;
         }
      }
   }

   void solve()
   {
      out.resize(N * N);
      solve_diags();
      solve_pls();
   }

   void print_output()
   {
      cout << ans;

      vector<pii> output;

      for(ist r = 0; r < N; ++ r)
         for(ist c = 0; c < N; ++ c)
         {
            ist ind = index(r,c);
            if (out[ind]) output.push_back(pii(ind, out[ind] | in[ind]));
         }
      cout << ' ' << output.size();

      string s = " +xo";

      for(auto &p: output)
      {
         cout << '\n' << s[p.second] << ' ' << p.first/N + 1 << ' ' << p.first % N + 1;
      }
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

