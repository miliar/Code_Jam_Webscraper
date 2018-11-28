#include <vector>
#include <iostream>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <utility>
#include <map>

#define FOR(i, n) for(int i = 0; i < n; i++)
#define MP(a, b) make_pair(a, b)

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

string s;

void solve(int tc) {
  cin >> s;
  cout << "Case #" << tc << ": ";
  if (s.length() == 1) {
    cout << s << endl;
    return;
  }
  for (int i = (int)s.length() - 1; i >= 1; i--) {
    if (s[i] < s[i-1]) {
      if (s[i-1] == '0') s[i-1] = '9'; else s[i-1]--;
      for (int j = i; j < s.length(); j++) s[j] = '9';
    }
  }
  if (s[0] == '0') s = s.substr(1);
  cout << s << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  int tt;
  cin >> tt;
  FOR(i, tt) {
    solve(i+1);
  }
  return 0;
}


