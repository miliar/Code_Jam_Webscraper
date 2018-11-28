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
   string data;

   void read_input()
   {
      cin >> data;
   }

   void solve()
   {
      char c = '0';
      ist i = 0;
      for(; i < data.length(); c = data[i], ++ i)
      {
        if (data[i] < c)
        {
           break;
        }
      }
      for(ist j = i; j < data.length(); ++ j) data[j] = '9';

      if (i < data.length())
      {
           -- i;
           -- data[i];
        while(i > 0 && data[i] < data[i - 1])
        {
           data[i] = '9';
           -- i;
           -- data[i];
        }
      }
      if (data[0] == '0')
      {
          data.erase(data.begin());
      }
   }

   void print_output()
   {
      cout << data;
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

