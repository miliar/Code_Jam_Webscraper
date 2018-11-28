#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

fstream in, out;

int T;
vector<int> digits;
vector<int> current;
long long num;

int get_next(int idx) {
  long long cand = 0;
  int min = 0;
  if (idx > 0) {
    min = current[idx - 1];
    for (int i = 0; i < idx; ++i) {
      long long add = current[i];
      for (int j = i; j < digits.size() - 1; ++j) {
        add *= 10;
      }
      cand += add;
    }
  }
  int ans = min;
  for (int digit = min; digit <= 9; ++digit) {
    long long add = 0;
    for (int i = idx; i < digits.size(); ++i) {
      add *= 10;
      add += digit;
    }
    long long new_cand = cand + add;
    if (new_cand > num) {
      break;
    } else {
      ans = digit;
    }
  }
  return ans;
}

int main() {
  in.open("B-large.in", fstream::in);
  out.open("probb-large.out", fstream::out);

  in >> T;
  for (int i = 0; i < T; i++) {
    digits.clear();
    current.clear();
    in >> num;
    long long num_copy = num;
    while (num_copy > 0) {
      digits.push_back(num_copy % 10);
      num_copy /= 10;
    }
    reverse(digits.begin(), digits.end());

    for (int j = 0; j < digits.size(); ++j) {
      int next = get_next(j);
      current.push_back(next);
    }
    long long ans = 0;
    for (int j = 0; j < current.size(); ++j) {
      ans *= 10;
      ans += current[j];
    }
    
    out << "Case #" << i + 1 << ": " << ans << endl;
  }
    
  in.close();
  out.close();
  return 0;
}
