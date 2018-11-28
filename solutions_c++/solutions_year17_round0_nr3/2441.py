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
    llui K, N;
    cin >> N >> K;

    cout << "Case #" << t << ": ";

    map<llui, llui> nodes;
    nodes[N] = 1;

    bool find_answer = false;

    while (true) {
      for (auto iter = nodes.rbegin(), iter_end = nodes.rend(); iter != iter_end; ++iter) {
        if (iter->second >= K) {
          llui v = iter->first;
          --v;
          cout << v / 2 + (v % 2 == 1) << " " << v / 2 << endl;
          find_answer = true;
          break;
        } else {
          K -= iter->second;
        }
      }

      if (find_answer) {
        break;
      }

      for (auto iter = nodes.begin(), iter_end = nodes.end(); iter != iter_end;) {
        llui v = iter->first;
        llui c = iter->second;

        --v;
        nodes[v / 2 + (v % 2 == 1)] += c;
        nodes[v / 2] += c;

        auto tmp = iter++;
        nodes.erase(tmp);
      }
    }
  }  // for each testcase
}

