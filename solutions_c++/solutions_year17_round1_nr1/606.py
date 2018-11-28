#include <iostream>
#include <set>
using namespace std;

int n, m;
string s[30];

set<int> x;
set<int> y;


void solve() {
  cin >> n >> m;
  for(int i = 0; i < n; i++) {
    cin >> s[i];
  }

  for(int i = 0; i < n; i++) {
    for(int j = 1; j < m; j++) {
      if(s[i][j] == '?' && s[i][j-1] != '?') {
        s[i][j] = s[i][j-1];
      }
    }
  }

  for(int i = 0; i < n; i++) {
    for(int j = m-2; j >=0; j--) {
      if(s[i][j] == '?' && s[i][j+1] != '?') {
        s[i][j] = s[i][j+1];
      }
    }
  }

  for(int i = 0; i < m; i++) {
    for(int j = 1; j < n; j++) {
      if(s[j][i] == '?' && s[j-1][i] != '?') {
        s[j][i] = s[j-1][i];
      }
    }
  }

  for(int i = 0; i < m; i++) {
    for(int j = n-2; j >=0; j--) {
      if(s[j][i] == '?' && s[j+1][i] != '?') {
        s[j][i] = s[j+1][i];
      }
    }
  }

  for(int i = 0; i < n; i++) {
    cout << s[i] << endl;
  }

}

int main () {
  int t;
  cin >> t;
  for(int i = 1; i <=t; i++) {
    printf("Case #%d:\n", i);
    solve();
  }
}
