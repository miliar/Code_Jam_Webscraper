#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <unordered_map>
#include <map>
#include <vector>
#include <unordered_set>
#include <set>


using namespace std;

int t;
string str;
int k;

int main() {
  cin.sync_with_stdio(0);
  cin >> t;
  for (int test_case = 1; test_case <= t; test_case++) {
    cin >> str >> k;
    int ans = 0;
    for (int i = 0; i < str.size()-k+1; i++) {
      if (str[i] == '-') {
        ans++;
        for (int j = i; j < i + k; j++) {
          if (str[j] == '-') str[j] = '+';
          else str[j] = '-';
        }
      }
    }
    for (int i = 0; i < str.size(); i++) {
      if (str[i] == '-') ans = -1;
    }
    cout << "Case " << "#" << test_case << ": ";
    if (ans == -1) cout << "IMPOSSIBLE";
    else cout << ans;
    cout << "\n";
  }
}
