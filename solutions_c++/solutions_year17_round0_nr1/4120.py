#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <numeric>
using namespace std;
void problem() {
  string s;
  int p;
  cin >> s >> p;
  size_t l = s.length();
  vector<int> v(s.length());
  for (int i = 0; i < l; ++i) {
    v[i] = s[i] == '+' ? 1 : -1;
  }
  int t = 0;
  for (int i = 0; i <= l - p; ++i) {
    while (i <= l - p && v[i] > 0) {
      i++;
    }
    if (i > l - p)
      break;
    for (int j = 0 ; j < p; ++j) {
      v[i + j] *= -1;
    }
    t++;
  }
  if (std::accumulate(v.begin(), v.end(), 0) != s.length()) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  cout << t << endl;
}

int main() {
  ifstream in("../in");
  cin.rdbuf(in.rdbuf());

  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cout << "Case #" << (i + 1) << ": ";
    problem();
  }

  return 0;
}