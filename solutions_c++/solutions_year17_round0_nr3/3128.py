#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>

using namespace std;

void solve() {
  uint64_t n, k;
  cin >> n >> k;
  map<int64_t, int64_t> nexts;
  nexts[n] += 1;
  int64_t x, y;
  for(int64_t i = 0; i < k;){
    auto it = nexts.rbegin();
    int64_t d = it->first;
    int64_t cnt = it->second;
    nexts.erase(d);
    x = (d - 1) / 2;
    y = d - 1 - (d - 1) / 2;
    if((d - 1) / 2){
      nexts[(d - 1) / 2] += cnt;
    }
    if(d - 1 - (d - 1) / 2){
      nexts[d - 1 - (d - 1) / 2] += cnt;
    }
    i += cnt;
  }
  if(x < y){
    swap(x, y);
  }
  cout << x << ' ' << y << endl;
}

int main() {
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; ++test) {
    cout << "Case #" << test << ": ";
    solve();
  }
}
