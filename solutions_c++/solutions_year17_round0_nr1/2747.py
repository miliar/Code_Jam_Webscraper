#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int main() {
  std::ifstream in;
  in.open("test.in");
  std::ofstream out;
  out.open("test.out");

  int nb_tests;
  in >> nb_tests;

  for (int id_test = 1; id_test <= nb_tests; ++id_test) {
    std::string s;
    int k;
    in >> s >> k;

    std::vector<int> status(s.size());
    for (int i = 0; i < s.size(); ++i) {
      if (s[i] == '-') {
        status[i] = 0;
      } else {
        status[i] = 1;
      }
    }

    int ans = 0;
    std::vector<int> to_prop(s.size());
    int current_prop = 0;
    for (int i = 0; i < s.size() - k + 1; ++i) {
      if (((status[i] + current_prop) & 1) == 0) {
        current_prop = (current_prop + 1) & 1;
        --to_prop[i + k - 1];
        ++ans;
      }
      current_prop = (current_prop + to_prop[i]) & 1;
    }

    bool ok = true;
    for (int i = s.size() - k + 1; i < s.size(); ++i) {
      if (((status[i] + current_prop) & 1) == 0) {
        ok = false;
      }
      current_prop = (current_prop + to_prop[i]) & 1;
    }
    
    out << "Case #" << id_test << ": ";
    if (ok) {
      out << ans << "\n"; 
    } else {
      out << "IMPOSSIBLE\n";
    }
  }

  return 0;
}
