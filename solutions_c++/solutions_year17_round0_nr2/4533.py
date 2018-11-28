#include <iostream>
#include <cmath>
#include <vector>
#include <cassert>
#include <cstdio>
#include <limits>
#include <set>
#include <string>
#include <cstring>
#include <fstream>

using namespace std;

void invert(string& s, int from, int cnt){
  while (cnt) {
    if (s[from] == '-') {
      s[from] = '+';
    }
    else {
      s[from] = '-';
    }
    from++;
    --cnt;
  }
}

int solve_1(int k, string str) {
  int ans = 0;
  for (int i = 0; i <= str.length()-k; ++i) {
    if (str[i] == '+') {
      continue;
    } else {
      invert(str, i, k);
      ans++;
    }
  }
  for (int i = 0; i < k; ++i) {
    if (str[str.length() - k + i] == '-') ans = -1;
  }
  return ans;
}

void f(uint64_t val, const uint64_t& n, uint64_t& mx) {
  if (val > n) return;
  if (val > mx) mx = val;
  for (int i = ((val % 10 == 0)?1: val % 10); i < 10; ++i) {
    f(val * 10 + i, n, mx);
  }
}
long long solve_2(uint64_t n) {
  uint64_t mx = 0;
  f(0, n, mx);
  return mx;
}
int main() {
  ifstream in("input.txt");
  ofstream out("output.txt");
  int T;
  in >> T;
  for (int t_case = 1; t_case <= T; t_case++) {
    uint64_t n;
    in >> n;
    out << "Case #" << t_case << ": " << solve_2(n) << endl;
  }
  out.close();
  return 0;
}
