#ifdef DEBUG
//#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;

bool Check(long long x) {
  int last = 10;
  while (x) {
    int v = x % 10;
    if (v > last) {
      return false;
    }
    last = v;
    x /= 10;
  }
  return true;
}

long long Update(long long x) {
  std::vector<int> digits;
  long long prev_x = x;
  while (x) {
    digits.push_back(x % 10);
    x /= 10;
  }
  int pos = digits.size() - 1;
  while (digits[pos] <= digits[pos - 1]) {
    --pos;
  }
  --pos;
  long long sub = 0;
  while (pos >= 0) {
    sub = sub * 10 + digits[pos];
    --pos;
  }
  prev_x -= sub + 1;
  return prev_x;
}

void Solve() {
  long long x;
  cin >> x;
  while (!Check(x)) {
    x = Update(x);  
  }
  cout << x << endl;
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        Solve();
    }
    return 0;
}
