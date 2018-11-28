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
  int64_t n, c, m;
  in >> n >> c >> m;
  vector<int64_t> u_counts(c, 0);
  vector<int64_t> p_counts(n, 0);
  int64_t mx_usr_cnt = 0;
  for (int i = 0; i < m; ++i) {
    int u, p;
    in >> p >> u;
    --p; --u;
    ++u_counts[u];
    ++p_counts[p];
    mx_usr_cnt = std::max(mx_usr_cnt, u_counts[u]);
  }
  for (int trips = mx_usr_cnt;; ++trips) {
    int64_t promotes = 0;
    int64_t possible = 0;
    bool can = true;
    for (int i = 0; i < n && can; ++i) {
      if (p_counts[i] > possible + trips) {
        can = false;
        break;
      }
      if (p_counts[i] > trips) {
        int val = p_counts[i] - trips;
        promotes += val;
        possible -= val;
      } else {
        possible += trips - p_counts[i];
      }
    }
    if (can) {
      out << trips << ' ' << promotes << '\n';
      return;
    }
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