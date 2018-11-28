#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <iomanip>
#include <stack>
#include <sstream>
#include <queue>
#include <set>
#include <functional>
#include <ctime>

#define endl '\n'
#define eps 1e-9
#define ll long long int
#define INF 123456

using namespace std;

void flip(string &s, int i) {
  if (s[i] == '+') {
    s[i] = '-';
  }
  else {
    s[i] = '+';
  }
}

int main() {
  #ifndef TEST
  	ios_base::sync_with_stdio(false);
  	cin.tie(0);
  #endif
  int T;
  cin >> T;
  for (int Case = 1; Case <= T; Case++) {
    string original;
    cin >> original;
    int n = original.size();
    int k;
    cin >> k;
    string test = original;
    int ret = INF;
    int temp_ret = 0;
    for (int i = 0; i < n; i++) {
      if (test[i] == '-') {
        temp_ret++;
        if (i+k-1 >= n) {
          temp_ret = INF;
          break;
        }
        for (int j = 0; j < k; j++) {
          flip(test, i+j);
        }
      }
    }
    ret = min(temp_ret, ret);
    test = original;
    temp_ret = 0;
    for (int i = n-1; i >= 0; i--) {
      if (test[i] == '-') {
        if (i-k+1 < 0) {
          temp_ret = INF;
          break;
        }
        temp_ret++;
        for (int j = 0; j < k; j++) {
          flip(test, i-j);
        }
      }
    }
    ret = min(ret, temp_ret);
    string ans = (ret == INF ? "IMPOSSIBLE" : to_string(ret));
    cout << "Case #" << Case << ": " << ans << '\n';
  }
}
