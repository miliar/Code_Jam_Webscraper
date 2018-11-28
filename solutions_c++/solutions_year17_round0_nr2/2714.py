#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
  std::ifstream in;
  in.open("test.in");
  std::ofstream out;
  out.open("test.out");

  int nb_tests;
  in >> nb_tests;

  for (int id_test = 1; id_test <= nb_tests; ++id_test) {
    long long x;
    in >> x;

    std::vector<int> v;
    while (x) {
      v.push_back(x % 10);
      x /= 10;
    }
    std::reverse(v.begin(), v.end());
    
    std::vector<int> ans_v;
    ans_v.push_back(v[0]);
    bool strictly_smaller = false;
    for (int pos = 1; pos < v.size(); ++pos) {
      if (!strictly_smaller) {
        if (v[pos] >= v[pos - 1]) {
          ans_v.push_back(v[pos]);
        } else {
          int last_value = ans_v[pos - 1];
          int back_pos = pos - 1;
          while (back_pos >= 0 && last_value == ans_v[back_pos]) {
            --ans_v[back_pos];
            --back_pos;
          }
          ++back_pos;
          ++back_pos;
          while (back_pos < pos) {
            ans_v[back_pos] = 9;
            ++back_pos;
          }
          ans_v.push_back(9);
          strictly_smaller = true;
        }
      } else {
        ans_v.push_back(9);
      }
    }

    long long ans = 0;
    for (int pos = 0; pos < ans_v.size(); ++pos) {
      ans = ans * 10 + ans_v[pos];
    }
    
    out << "Case #" << id_test << ": " << ans << "\n";
  }

  return 0;
}
