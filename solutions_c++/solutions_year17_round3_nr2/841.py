#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

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
   std::ifstream in("../B-small-attempt0.in");
//   std::ifstream in("../B-large.in");
//   std::ifstream in("../B-sample.in");
//   std::ifstream in("../B-sample.in");

   std::cin.rdbuf(in.rdbuf());

//   std::ofstream out("../B-sample.out");
   std::ofstream out("../B-small.out");
//   std::ofstream out("../B-large.out");

   std::cout.rdbuf(out.rdbuf());

   solve();
   return 0;
}

struct Interval {
   int begin;
   int end;
   char owner;
};


void solve_case(int t)
{

   int Ac, Aj;

   cin >> Ac >> Aj;

   vector<Interval> C(Ac), J(Aj);

   int time_C = 0, time_J = 0;

   for (int i = 0; i < Ac; ++i) {
      cin >> C[i].begin >> C[i].end;
      C[i].owner = 'c';
      time_C += C[i].end - C[i].begin;
   }

   for (int j = 0; j < Aj; ++j) {
      cin >> J[j].begin >> J[j].end;
      J[j].owner = 'j';
      time_J += J[j].end - J[j].begin;
   }

   vector<Interval> all = C;
   for (auto interval : J) {
      all.push_back(interval);
   }

   sort(C.begin(), C.end(), [](Interval const& lhs, Interval const& rhs) {
      return lhs.begin < rhs.begin;
   });

   sort(J.begin(), J.end(), [](Interval const& lhs, Interval const& rhs) {
      return lhs.begin < rhs.begin;
   });

   sort(all.begin(), all.end(), [](Interval const& lhs, Interval const& rhs) {
      return lhs.begin < rhs.begin;
   });

   int total_C = 0, total_J = 0;

   for (auto i : C) {
      total_C += i.end - i.begin;
   }

   for (auto j : J) {
      total_J += j.end - j.begin;
   }

   vector<int> switch_free_for_C, switch_free_for_J;

   int total_free_switch_time = 0;
   int total_free_for_C = 0, total_free_for_J = 0;
   int min_switches = 0;

   for (int i = 0; i + 1 < all.size(); i++) {
      if (all[i].owner == 'c' and all[i + 1].owner == 'c') {
         switch_free_for_C.push_back(all[i + 1].begin - all[i].end);
         total_free_for_C += switch_free_for_C.back();
      } else if (all[i].owner == 'j' and all[i + 1].owner == 'j') {
         switch_free_for_J.push_back(all[i + 1].begin - all[i].end);
         total_free_for_J += switch_free_for_J.back();
      } else {
         min_switches += 1;
         total_free_switch_time += all[i + 1].begin - all[i].end;
      }
   }

   if (all.back().owner == 'c' and all[0].owner == 'c') {
      switch_free_for_C.push_back(1440 - all.back().end + all[0].begin);
      total_free_for_C += switch_free_for_C.back();
   } else if (all.back().owner == 'j' and all[0].owner == 'j') {
      switch_free_for_J.push_back(1440 - all.back().end + all[0].begin);
      total_free_for_J += switch_free_for_J.back();
   } else {
      min_switches += 1;
      total_free_switch_time += 1440 - all.back().end + all[0].begin;
   }

   sort(switch_free_for_C.begin(), switch_free_for_C.end(), std::greater<int>());
   sort(switch_free_for_J.begin(), switch_free_for_J.end(), std::greater<int>());

//   cerr << time_C << " " << total_free_for_C << "\n";
//   cerr << time_J << " " << total_free_for_J << "\n";

   if (time_C + total_free_for_C <= 720 and time_J + total_free_for_J <= 720) {
      cout << min_switches;
   } else if (time_C + total_free_for_C > 720) {
      int time_required = 720 - time_C - total_free_for_C - total_free_switch_time;
      int i = 0;
      while (time_required < 0) {
//         cerr << time_required;
         min_switches += 2;
         time_required += switch_free_for_C[i];
         i++;
//         cerr << i << "\n";
      }
      cout << min_switches;
   } else {
      int time_required = 720 - time_J - total_free_for_J - total_free_switch_time;
      int i = 0;
      while (time_required < 0) {
//         cerr << time_required;
         min_switches += 2;
         time_required += switch_free_for_J[i];
         i++;
      }
      cout << min_switches;
   }

   cout << "\n";
}
