#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <cstring>

using namespace std;

typedef ptrdiff_t ist;
typedef size_t iut;
typedef vector<ist> vi;
typedef pair<ist, ist> pii;

bool trailing_space = true; // for output

struct rect
{
   ist rs, re, cs, ce;

   bool contains(const rect & other) const
   {
     return other.rs >= rs && other.re <= re &&
other.cs >= cs && other.ce <= ce;
   }

   bool empty() const
   {
     return rs >= re;
   }
};

struct Solver
{
   ist R, C;
   vector<string> data;
   rect letters[256];

   void read_input()
   {
      cin >> R >> C;
      data.resize(R);
      for(auto &d: data) cin >> d;
   }

   void solve(const rect & rec)
   {
cerr << rec.rs << rec.re << rec.cs << rec.ce << '\n';
      set<ist> rows;
      set<ist> cols;
      ist max_r = rec.rs;
      ist max_c = rec.cs;
      ist min_r = rec.re;
      ist min_c = rec.ce;

      for(ist i = rec.rs + 1; i <= rec.re; ++ i) rows.insert(i);
      for(ist i = rec.cs + 1; i <= rec.ce; ++ i) cols.insert(i);

      ist count = 0;

      char m = 0;

      for(char c = 'A'; c <= 'Z'; ++ c)
      {
         if (!letters[c].empty() && rec.contains(letters[c]))
         {
            ++ count;
            m = c;
            max_r = max(max_r, letters[c].rs);
            max_c = max(max_c, letters[c].cs);
            min_r = min(min_r, letters[c].re);
            min_c = min(min_c, letters[c].ce);
            for(ist r = letters[c].rs + 1; r < letters[c].re; ++ r)
            {
               rows.erase(r);
            }
            for(ist c2 = letters[c].cs + 1; c2 < letters[c].ce; ++ c2)
            {
               cols.erase(c2);
            }
         }
      }

      if (count == 1)
      {
         for(ist r = rec.rs; r < rec.re; ++ r)
         for(ist c = rec.cs; c < rec.ce; ++ c)
            data[r][c] = m;
         return;
      }

      for(auto & r: rows)
      {
         if (r <= max_r && r >= min_r)
         {
            rect rec1 = rec;
            rect rec2 = rec;
            rec1.re = r;
            rec2.rs = r;
            solve(rec1);
            solve(rec2);
            return;
         }
      }

      for(auto & c: cols)
      {
         if (c <= max_c && c >= min_c)
         {
            rect rec1 = rec;
            rect rec2 = rec;
            rec1.ce = c;
            rec2.cs = c;
            solve(rec1);
            solve(rec2);
            return;
         }
      }
   }

   void solve()
   {
      memset(letters, 0, sizeof(letters));
      for(char c = 'A'; c <= 'Z'; ++ c)
      {
         letters[c] = rect({R, 0, C, 0});
      }
      for(ist i = 0; i < R; ++ i)
      for(ist j = 0; j < C; ++ j)
      {
         auto c = data[i][j];
         if (c != '?')
         {
            if (letters[c].rs > i) letters[c].rs = i;
            if (letters[c].re <= i + 1) letters[c].re = i + 1;
            if (letters[c].cs > j) letters[c].cs = j;
            if (letters[c].ce <= j + 1) letters[c].ce = j + 1;
         }
      }

      rect rec({0, R, 0, C});
      solve(rec);
   }

   void print_output()
   {
      for(auto &d: data)
         cout << '\n' << d;
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

