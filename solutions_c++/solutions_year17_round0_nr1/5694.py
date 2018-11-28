#include <iostream>
#include <limits>
#include <bitset>
#include <vector>
#include <string>
#include <map>
#include <unordered_map>

using namespace std;

typedef unsigned long long ull;
const ull IMPOSSIBLE = std::numeric_limits<ull>::max(); 

string solution;
unordered_map<string, ull> cache;

std::string flip(std::string input, size_t location, ull K) {
  for (size_t i = location; i < location + K; ++i) {
    input[i] = (input[i] == '-') ? '+' : '-';
  }
  return input;
}

ull solve(const std::string& pancakes, ull K, ull flips) {
  if (pancakes == solution) {
    return flips;
  } else {
    ull result = IMPOSSIBLE;
    for (size_t i=0; i <= pancakes.size() - K; ++i) {
      auto toTest = flip(pancakes, i, K);
      auto it = cache.find(toTest);
      if (it != cache.end()) {
        if (it->second != IMPOSSIBLE) {
          ull newResult = flips + it->second + 1;
          result = (newResult < result) ? newResult : result;
        }
      } else {
        cache.emplace(toTest, IMPOSSIBLE);
        auto newResult = solve(toTest, K, flips+1);
        if (IMPOSSIBLE != newResult) {
          cache[toTest] = newResult - (flips+1);
        }
        result = (newResult < result) ? newResult : result;
      }
    }
    return result;
  }
}

int main() {
  std::ios::sync_with_stdio(false);

  ull T; cin >> T;
  for (ull i = 1; i <= T; ++i) {
    cache.clear();
    ull K; string pancakes_str; cin >> pancakes_str >> K;
    solution = string(pancakes_str.size(), '+');
    const auto answer = solve(pancakes_str, K, 0);
    cout << "Case #" << i << ": ";
    if (answer == IMPOSSIBLE) {
      cout << "IMPOSSIBLE";
    } else {
      cout << answer;
    }
    cout << '\n';
  }
}
