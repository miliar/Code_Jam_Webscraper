#include <algorithm>
#include <iostream>
#include <limits>
#include <bitset>
#include <vector>
#include <string>
#include <map>
#include <stack>
#include <unordered_map>

using namespace std;

typedef unsigned long long ull;
const ull IMPOSSIBLE = std::numeric_limits<ull>::max(); 

string solve(ull N) {
	string s = std::to_string(N);

	size_t pos = s.size() - 1;
  if (0 == pos) {
    return s;
  }

  while (pos > 0) {
    if (s[pos] < s[pos-1]) {
      s[pos] = '9';
      for (size_t i = pos + 1; i < s.size() && s[i] != '9'; ++i) {
        s[i] = '9';
      }
      if (s[pos-1] > '0') {
        s[pos-1] -= 1;
      } else {
        s[pos-1] = '9';
      }
    }
    --pos;
  }

  if (s[0] == '0') {
    s.erase(0,1);
  }
  return s;
}

int main() {
  std::ios::sync_with_stdio(false);

  ull T; cin >> T;
  for (ull i = 1; i <= T; ++i) {
		ull N; cin >> N;
    cout << "Case #" << i << ": " << solve(N) << '\n';
  }
}
