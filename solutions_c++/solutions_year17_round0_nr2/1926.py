#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

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
//   std::ifstream in("../B-small-attempt0.in");
   std::ifstream in("../B-large.in");
//   std::ifstream in("../B-sample.in");

   std::cin.rdbuf(in.rdbuf());

//   std::ofstream out("../B-sample.out");
//   std::ofstream out("../B-small.out");
   std::ofstream out("../B-large.out");

   std::cout.rdbuf(out.rdbuf());

   solve();
   return 0;
}

void solve_case(int t)
{
   long number;
   cin >> number;

   vector<int> digits;

   for (auto x : to_string(number)) {
      digits.push_back(x - '0');
   }

   if (digits.size() == 1) {
      cout << number << "\n";
      return;
   }


   bool changed;

   do {
      changed = false;

      for (int i = 0; i < digits.size() - 1; i++) {
         if (digits[i] > digits[i + 1]) {
            changed = true;
            digits[i] = digits[i] - 1;

            for (int k = i + 1; k < digits.size(); k++) {
               digits[k] = 9;
            }
         }
      }
   }
   while (changed);

   bool trailing = true;
   for (auto digit : digits) {
      if (digit == 0 and trailing) {
         continue;
      }

      trailing = false;
      cout << digit;
   }

   cout << "\n";
}
