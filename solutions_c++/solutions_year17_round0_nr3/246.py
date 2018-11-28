#define NDEBUG
#include <algorithm>
#include <cassert>
#include <functional>
#include <iostream>
#include <map>
#include <string>
#include <tuple>
using namespace std;

typedef long long int64;

string solve() {
  int64 N, K;
  cin >> N >> K;
  map<int64, int64, greater<int64> > groups;
  groups[N] = 1;
  while (1) {
    auto it = groups.begin();
    int64 size, count;
    tie(size, count) = *it;
    assert(size > 0);
    groups.erase(it);
    if (count >= K) {
      return to_string(size / 2) + " " + to_string((size - 1) / 2);
    }
    K -= count;
    groups[(size-1) / 2] += count;
    groups[(size) / 2] += count;
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) { // caret here
    cout << "Case #" << tt << ": " << solve() << '\n';
  }
}
