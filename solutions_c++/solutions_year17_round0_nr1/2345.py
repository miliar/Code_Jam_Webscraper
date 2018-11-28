#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <sstream>
#include <iostream>
using namespace std;

fstream in, out;

int T;
int K, S;
string pancakes;

int main() {
  in.open("A-large.in", fstream::in);
  out.open("proba-large.out", fstream::out);

  in >> T;
  for (int i = 0; i < T; ++i) {
    in >> pancakes >> K;
    int ans = 0;
    
    for (int j = 0; j < pancakes.size() - K + 1; ++j) {
      if (pancakes.at(j) == '-') {
        ++ans;
        for (int k = j; k < j + K; ++k) {
          if (pancakes[k] == '-') {
            pancakes[k] = '+';
          } else {
            pancakes[k] = '-';
          }
        }
      }
    }

    bool is_ok = true;
    for (int j = 0; j < pancakes.size(); ++j) {
      if (pancakes[j] == '-') {
        is_ok = false;
      }
    }

    ostringstream ans_ss;
    if (is_ok) {
      ans_ss << ans;
    } else {
      ans_ss << "IMPOSSIBLE";
    }
    string ans_str = ans_ss.str();
    
    out << "Case #" << i + 1 << ": " << ans_str << endl;
  }
    
  in.close();
  out.close();
  return 0;
}
