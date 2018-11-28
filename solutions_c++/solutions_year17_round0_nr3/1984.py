#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <cassert>

using namespace std;

void solve_case(int t);

void solve()
{
   int T;
   cin >> T;

   for (int t = 1; t <= T; t++) {
      cout << "Case #" << t << ": ";
      solve_case(t);
   }
}

int main()
{
//   std::ifstream in("../C-small-1-attempt0.in");
//   std::ifstream in("../C-small-2-attempt0.in");
   std::ifstream in("../C-large.in");
//   std::ifstream in("../C-sample.in");

   std::cin.rdbuf(in.rdbuf());

//   std::ofstream out("../C-sample.out");
//   std::ofstream out("../C-small1.out");
//   std::ofstream out("../C-small2.out");
   std::ofstream out("../C-large.out");

   std::cout.rdbuf(out.rdbuf());

   solve();
   return 0;
}

void solve_case(int t)
{
   long N, K;
   cin >> N >> K;

   map<long, long> num_free_seats {
      {N, 1}
   };

   long a, b;

   long counter = 0;
   while (counter < K) {
      auto free_seats = num_free_seats.rbegin()->first;
      auto num = num_free_seats.rbegin()->second;
      num_free_seats.erase(free_seats);

      assert(num > 0);

      if (free_seats % 2 == 0) {
         a = free_seats / 2 - 1;
         b = free_seats / 2;
      }
      else {
         a = free_seats / 2;
         b = free_seats / 2;
      }

      num_free_seats[a] += num;
      num_free_seats[b] += num;

      counter += num;
   }

//   cout << N << " " << K << "\n";

//   for (auto const& entry : num_free_seats) {
//      cout << "[" << entry.first << "] = " << entry.second << "\n";
//   }

   cout << max(a, b) << " " << min(a, b);

   cout << "\n";
}
