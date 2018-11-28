#include <iostream>
#include <fstream>

#include <string>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>

using namespace std;

using std::vector;
using std::string;
using std::pair;

struct State {
  int city;
  int horse;
  int64_t capacity;


  bool operator<(const State& other) const {
    return make_tuple(city, horse, capacity) < make_tuple(other.city, other.horse, other.capacity);
  }
};

void work(std::ifstream& in, std::ofstream& out) {
  int n, p;
  in >> n >> p;
  vector<int> vals(p);
  for (size_t i = 0; i < n; ++i) {
    int v;
    in >> v;
    vals[v % p]++;
  }
  int rest = n - vals[0];
  int ans = vals[0];
  if (p == 2) {
    ans += (vals[1] + 1) / 2;
    out << ans << '\n';
    return;
  } else if(p == 3) {
    int mn = std::min(vals[1], vals[2]);
    vals[1] -= mn;
    vals[2] -= mn;
    rest -= mn;
    ans += mn;
    ans += (vals[1] + vals[2] + 2) / 3;
    out << ans << '\n';
    return;
  } else {
    assert(p == 4);
    ans += vals[2] / 2;
    rest -= vals[2] / 2;
    vals[2] = vals[2] % 2;

    int mn = std::min(vals[1], vals[3]);
    vals[1] -= mn;
    vals[3] -= mn;
    rest -= mn;
    ans += mn;
    if (vals[2]) {
      if (rest > 2) {
        rest -= 3;
        ans++;
      }
    }
    ans += (rest + 3) / 4;
    out << ans << '\n';
  }
}

int main() {

  std::ifstream in("input.in");
  std::ofstream out("output.out");

  size_t T;
  in >> T;

  for (size_t i = 0; i < T; ++i) {
    out << "Case #" << i + 1 << ": ";
    work(in, out);
  }
  return 0;
}