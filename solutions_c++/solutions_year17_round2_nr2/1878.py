#include <string>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <chrono>
#include <numeric>
#include <limits>
#include <cassert>

using namespace std;

typedef ptrdiff_t ist;
typedef size_t iut;
typedef vector<ist> vi;
typedef pair<ist, ist> pii;

#define INF (numeric_limits<ist>::max())

bool trailing_space = true; // for output

struct HH
{
   unsigned r:10, y:10, o:10, b:10, v:10, g:10;
};

union H
{
   iut h;
   HH hh;
};

void h2d(const H &h, int * data)
{
   data[1] = h.hh.r;
   data[2] = h.hh.y;
   data[3] = h.hh.o;
   data[4] = h.hh.b;
   data[5] = h.hh.v;
   data[6] = h.hh.g;
}

void decr(H & h2, short d)
{
   switch (d) {
   case 1:
      assert(h2.hh.r > 0);
      --h2.hh.r;
      break;
   case 2:
      assert(h2.hh.y > 0);
      --h2.hh.y;
      break;
   case 3:
      assert(h2.hh.o > 0);
      --h2.hh.o;
      break;
   case 4:
      assert(h2.hh.b > 0);
      --h2.hh.b;
      break;
   case 5:
      assert(h2.hh.v > 0);
      --h2.hh.v;
      break;
   case 6:
      assert(h2.hh.g > 0);
      --h2.hh.g;
      break;
   default:
      break;
   }
}


map<pair<iut, short>, short> caches;

struct Solver
{
   short N, R, O, Y, G, B, V;
   short ans;
   H h0;

   void read_input()
   {
      cin >> N >> R >> O >> Y >> G >> B >> V;
   }

   ist solve(const H &h, short ends)
   {
      iut hh = h.h;

      pair<iut, short> he(hh, ends);

      auto iter = caches.find(he);
      if (iter != caches.end()) return iter->second;

      auto & ret = caches[he];

      short start = ends & 7;
      short end = ends/8;

      int data[8] = {};
      h2d(h, data);
      ist cnt = 0;
      ist cnt2 = 0;
      for(auto &d:data) cnt += d;

      if (2 * (data[3] + data[5] + data[6]) - 1 > cnt)
      {
         return ret = (short)(-1);
      }

      for(ist i = 0; i < 8; ++ i)
      {
         if (i != 1 || i != 2 || i != 4) continue;
         ist excl = 0;
         for(ist j = 0; j < 8; ++ j)
         {
            if ((j & i)) excl += data[j];
         }

         if (2 *excl - 1 > cnt)
         {
            return ret = (short)(-1);
         }
      }

      vector<ist> candidates;

      for(ist i = 0; i < 8; ++ i)
      {
         if (data[i] == 0) continue;
         if ( (i & start) > 0 || (cnt == 1 && (i & end) > 0))
         {
            data[i] = 0;
         }
         else
         {
            cnt2 += data[i];
            candidates.push_back(i);

            if (i & (i-1)) data[i] += 1000;
         }
      }

      if (cnt2 == 0)
      {
         return ret = (short)(-1);
      }

      if (cnt == 1)
      {
         ist i = 0;
         for(; i < 8; ++ i) if (data[i]) break;
         return ret = i;
      }

      // let's pick the largest one first
      sort(candidates.begin(), candidates.end(), [data](ist i, ist j)
      {
         return data[i] > data[j];
      });

      for(auto & d: candidates)
      {
         H h2 = h;

         decr(h2, d);

         short ret2 = solve(h2, ((end == 0?d:end) << 3) | d);
         if (ret2 != (short)(-1)) return ret = d;
      }
      return ret = (short)(-1);
   }

   void solve()
   {
      h0.h = 0;
      h0.hh.r = R;
      h0.hh.o = O;
      h0.hh.y = Y;
      h0.hh.g = G;
      h0.hh.b = B;
      h0.hh.v = V;
      ans = solve(h0, 0);
   }

   void print_output()
   {
      if (ans == (short)(-1))
         cout << "IMPOSSIBLE";
      else
      {
         char colors[] = " RYOBVG ";
         cout << colors[ans];
         short ends = (ans << 3) | ans;
         while(true)
         {
            decr(h0, ans);
            if (!h0.h) break;
            ans = solve(h0, ends);
            cout << colors[ans];
            ends -= ends & 7;
            ends |= ans;
         }
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

