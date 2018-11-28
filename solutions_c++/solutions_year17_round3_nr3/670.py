#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

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
//   std::ifstream in("../C-large.in");
   std::ifstream in("../C-small-1-attempt0.in");

   std::cin.rdbuf(in.rdbuf());

//   std::ofstream out("../C-sample.out");
   std::ofstream out("../C-small1.out");
//   std::ofstream out("../C-small2.out");
//   std::ofstream out("../C-large.out");

   std::cout.rdbuf(out.rdbuf());

   solve();
   return 0;
}

using ld = long double;

bool can_level_be_achieved(ld U, ld level, vector<ld> const& P)
{
   ld total = 0;
   for (ld p : P) {
      total += std::max((ld) 0., level - p);
   }
   return total <= U;
}

void solve_case(int t)
{

   int N, K;
   ld U;

   cin >> N >> K;

   cin >> U;

   vector<ld> P(N);

   for (int i = 0; i < N; i++) {
      cin >> P[i];
   }

   sort(P.begin(), P.end());

   ld min_level = 0, max_level = 1;

   int num_iter = 10000;
   for (int i = 0; i < num_iter; i++) {
      auto mid_level = (max_level + min_level) / 2;
      if (can_level_be_achieved(U, mid_level, P)) {
         min_level = mid_level;
      }
      else {
         max_level = mid_level;
      }
   }

   ld product = 1.0;
   for (int i = 0; i < N; i++) {
      product *= std::max(max_level, P[i]);
   }

   cout << product;

   cout << "\n";
}
