#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
using namespace std;

struct Range {
  Range() = default;
  Range(uint64_t len) : m_len(len) {
    auto const toLeft = ToLeft(m_len);
    auto const toRight = ToRight(m_len);

    m_min = min(toLeft, toRight);
    m_max = max(toLeft, toRight);
  }

  static uint64_t ToLeft(uint64_t len) { return (len - 1) >> 1; }

  static uint64_t ToRight(uint64_t len) { return len >> 1; }

  bool operator<(Range const &rhs) const {
    if (m_min != rhs.m_min)
      return m_min > rhs.m_min;
    if (m_max != rhs.m_max)
      return m_max > rhs.m_max;
    return m_len > rhs.m_len;
  }

  uint64_t m_len = 0;
  uint64_t m_min = 0;
  uint64_t m_max = 0;
};

int main() {
  ios_base::sync_with_stdio(0);

  map<Range, uint64_t> ranges;

  int numTests;
  cin >> numTests;

  for (int testNum = 1; testNum <= numTests; ++testNum) {
    uint64_t n, k;
    cin >> n >> k;

    ranges.clear();
    ranges[Range(n)] = 1;

    while (k != 1) {
      auto const range = ranges.begin()->first;
      auto const count = ranges.begin()->second;
      if (count >= k)
        break;

      ranges.erase(ranges.begin());

      auto const toLeft = Range::ToLeft(range.m_len);
      if (toLeft != 0)
        ranges[Range(toLeft)] += count;

      auto const toRight = Range::ToRight(range.m_len);
      if (toRight != 0)
        ranges[Range(toRight)] += count;

      k -= count;
    }

    auto const &range = ranges.begin()->first;
    cout << "Case #" << testNum << ": " << range.m_max << " " << range.m_min
         << endl;
  }
  return 0;
}
