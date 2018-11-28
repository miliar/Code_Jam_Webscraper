#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <tuple>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <numeric>
#include <functional>
using namespace std;

typedef unsigned long long int llui;
typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<string, string> pss;

const int sz = 1e5;

int main() {
  ios::sync_with_stdio(false);
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    string digits;
    cin >> digits;

    for (int i = 1; i < digits.size(); ++i) {
      if (digits[i] >= digits[i - 1]) {
        continue;
      }
      int j;
      for (j = i - 1; j >= 0; --j) {
        --digits[j];
        if (j - 1 >= 0 && digits[j] >= digits[j - 1]) {
          break;
        }
        if (j == 0) {
          break;
        }
      }
      if (digits[0] == '0') {
        digits = string(digits.size() - 1, '9');
        break;
      }
      for (++j; j < digits.size(); ++j) {
        digits[j] = '9';
      }
      break;
    }

    cout << digits << endl;
  }
}

