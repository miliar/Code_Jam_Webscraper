#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <iomanip>

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
//   std::ifstream in("../A-small-attempt0.in");
//   std::ifstream in("../A-sample.in");
//   std::ifstream in("../A-small-attempt0.in");
   std::ifstream in("../A-large.in");
//
   std::cin.rdbuf(in.rdbuf());

//   std::ofstream out("../A-sample.out");
//   std::ofstream out("../A-small.out");
   std::ofstream out("../A-large.out");
//
   std::cout.rdbuf(out.rdbuf());

   solve();
   return 0;
}

void solve_case(int t)
{
   int K, N;
   cin >> N >> K;

   vector<long double> R(N), H(N);
   for (int i = 0; i < N; i++) {
      cin >> R[i] >> H[i];
   }

   long double best_area = 0;

   for (int area_max = 0; area_max < N; area_max++) {
      long double area = 0;
      area = M_PI * R[area_max]*R[area_max] + 2 * M_PI * R[area_max]*H[area_max];

      vector<long double> r_h(N);

      for (int i = 0; i < N; i++) {
         r_h[i] = i != area_max ? R[i] * H[i] : 0;
      }

      sort(r_h.begin(), r_h.end(), std::greater<long double>());

      for (int i = 0; i < K - 1; i++) {
         area += 2 * M_PI * r_h[i];
      }

      if (area > best_area) best_area = area;
   }

   cout << std::setprecision(10) << best_area << "\n";
}
