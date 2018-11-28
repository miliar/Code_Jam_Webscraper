#include <iostream>
#include <fstream>

#include <string>
#include <vector>

using std::vector;
using std::string;
using std::pair;

void work(std::ifstream& in, std::ofstream& out) {

  size_t N, K;
  in >> N >> K;

  vector<pair<size_t, size_t>> state = { { N, 1 } };
  while (true) {
    size_t ps = 0;
    for (size_t i = 0; i < state.size(); ++i) {
      if (state[i].first > state[ps].first) {
        ps = i;
      }
    }

    auto val = state[ps].first;
    auto count = state[ps].second;

    if (count >= K) {
      size_t mn = (state[ps].first - 1) / 2;
      size_t mx = state[ps].first / 2;
      out << mx << ' ' << mn << '\n';
      return;
    }
    K -= count;
    if (val % 2 == 1) {
      if (val != 1) {
        state[ps].first = state[ps].first / 2;
        state[ps].second = 2 * count;
      }
    } else {
      vector<pair<size_t, size_t>> new_state;
      for (size_t i = 0; i < ps; ++i) {
        new_state.push_back(state[i]);
      }
      state.push_back({ (val - 1) / 2, count });
      state.push_back({ val / 2, count });
      for (size_t i = ps + 1; i < state.size(); ++i) {
        new_state.push_back(state[i]);
      }
      state.swap(new_state);
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