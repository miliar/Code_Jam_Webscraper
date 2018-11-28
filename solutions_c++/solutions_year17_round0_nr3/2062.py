#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <vector>

using namespace std;

void update_map(std::map<int64_t, int64_t>& m, int64_t k, int64_t v) {
  auto it = m.find(k);
  if(it == m.end()) {
    m.emplace(k, v);
  } else {
    it->second += v;
  }
}

void solve(int64_t case_, int64_t size, int64_t people) {
  std::map<int64_t, int64_t> data;
  data[size] = 1;
  int64_t count = 0;
  while(true) {
    auto it = data.rbegin();
    count += it->second;
    int64_t b = it->first / 2;
    int64_t s = it->first - b - 1;
    // cout << it->first << " " << it->second << " " << count << endl;
    if (count >= people) {
      if (b < s) {
        std::cerr << "failure!!!!" << std::endl;
        exit(1);
      }
      std::cout << "Case #" << case_ << ": " << b << " " << s << endl;
      break;
    }
    if(b > 0) {
      update_map(data, b, it->second);
    }
    if (s > 0) {
      update_map(data, s, it->second);
    }
    data.erase(std::next(it).base());
  }

}

int main() {
  int t_num;
  cin >> t_num;
  for (auto t = 1; t <= t_num; ++t) {
    int64_t size, n;
    cin >> size >> n;
    solve(t, size, n);
  }
}
