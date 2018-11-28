#include <algorithm>
#include <iostream>
#include <limits>
#include <bitset>
#include <vector>
#include <string>
#include <map>
#include <stack>
#include <unordered_map>
#include <tuple>
#include <queue>

using namespace std;

typedef unsigned long long ull;
typedef pair<unsigned long, unsigned long> cell;

void print(int level, const vector<cell>& cells) {
  return;
  cout << "level: " << level << " =";
  for (auto& x: cells) {
    cout << " (" << x.first << "," << x.second << ")";
  }
  cout << '\n';
}

void emplace(vector<cell>& cells, unsigned long x) {
  if (x&1) {
    auto val = (x-1)/2;
    cells.emplace_back(val, val);
  } else {
    auto val = (x)/2;
    cells.emplace_back(val, (val > 1) ? val-1 : 0);
  }
}

cell solve(ull N, ull K) {
  vector<cell> current;
  vector<cell> newCells;

  current.clear();
  newCells.clear();
  ull level = 1;

  emplace(current, N);
  print(level, current);
  while ((level + current.size() -1 )< K) {
    newCells.reserve(2 * current.size());
    for (const auto& cell : current) {
      emplace(newCells, cell.first);
      emplace(newCells, cell.second);
    }
    sort(newCells.begin(), newCells.end(), [](cell a, cell b) {
      if (a.first > b.first) {
        return true;
      } if (a.first == b.first) {
        return a.second > b.second;
      }
      return false;
    });
    current.swap(newCells);
    newCells.clear();
    level *= 2;
    print(level, current);
  }
  // cout << current.size() << '\n';

  // for (auto& x: current) {
  //   cout << "(" << x.first << "," << x.second << ") ";
  // }

  // cout << "K = " << K << " level = " << level << " K - level: " << K-level << " size: " << current.size() << '\n';
  cell& answer = current[K-level];
  // cout << "Returning " << answer.first << ", " << answer.second << '\n';
  return answer;
}

int main() {
  std::ios::sync_with_stdio(false);

  ull T; cin >> T;
  for (ull i = 1; i <= T; ++i) {
    ull K, N; cin >> N >> K;
    cell result = solve(N, K);
    cout << "Case #" << i << ": " << result.first << ' ' << result.second << '\n';
  }
}
