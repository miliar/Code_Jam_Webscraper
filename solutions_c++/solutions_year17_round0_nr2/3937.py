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

using namespace std;

int main() {
  #ifndef TEST
  	ios_base::sync_with_stdio(false);
  	cin.tie(0);
  #endif
  int T;
  cin >> T;
  for (int Case = 1; Case <= T; Case++) {
    string s;
    cin >> s;
    int n = s.size();
    bool works = true;
    for (int i = 0; i < n-1; i++) {
      if (s[i] > s[i+1]) {
        works = false;
        break;
      }
    }
    if (!works) {
      for (int i = 0; i < n-1; i++) {
        if (s[i] >= s[i+1]) {
          s[i]--;
          for (int j = i+1; j < n; j++) {
            s[j] = '9';
          }
          break;
        }
      }
    }
    int j;
    for (j = 0; j < n && s[j] == '0'; j++);
    string ans = s.substr(j, string::npos);
    cout << "Case #" << Case << ": " << ans << '\n';
  }
}
