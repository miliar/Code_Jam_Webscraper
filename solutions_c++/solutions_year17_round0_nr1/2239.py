#include <iostream>
#include <string>
using namespace std;

int tab[2000];
int s[1000];

int main() {
  int t, n, k, f, w;
  string st;
  cin >> t;
  for(int nr = 1; nr <= t; nr ++) {
    f = 0;
    w = 0;
    n = 0;
    cin >> st >> k;
    n = st.length();
    for(int i = 0; i < n; i ++) {
      s[i] = st[i] == '+' ? 1 : 0;
    }
    for(int i = 0; i <= n - k; i ++) {
      f ^= tab[i];
      if(!(s[i] ^ f)) {
        tab[i + k] = 1;
        f = f ^ 1;
        w ++;
      }
    }
    for(int i = n - k + 1; i < n; i ++) {
      f ^= tab[i];
      if(!(s[i] ^ f)) {
        w = -1;
        break;
      }
    }
    for(int i = 0; i <= n; i ++) {
      tab[i] = 0;
    }
    cout << "Case #" << nr <<": ";
    w == -1 ? cout << "IMPOSSIBLE\n" : cout << w << endl;
  }
  
}
