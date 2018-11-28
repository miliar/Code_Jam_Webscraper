/*
 Author:    sergioRG
*/
#include <bits/stdc++.h>
using namespace std;

int get_first_blank(string& s) {
  for(int i=0; i<int(s.size()); ++i) {
    if(s[i] == '-') return i;
  }
  return -1;
}

char complement(char s) {
  return s == '-' ? '+' : '-';
}

void flip(string& s, int start, int amount) {
  for(int i=start; i<start+amount; ++i) {
    s[i] = complement(s[i]);
  }
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(0);
  int T;
  cin >> T;
  for(int test_case=1; test_case<=T; ++test_case) {
    string s;
    int k;
    cin >> s >> k;
    int n = int(s.size());
    int ans = 0;
    bool changes = true;
    while(changes) {
      changes = false;
      int to_change = get_first_blank(s);
      if(to_change != -1  && to_change <= n-k) {
        changes = true;
        flip(s, to_change, k);
        ++ans;
      }
    }
    cout << "Case #" << test_case << ": ";
    if(get_first_blank(s) != -1) {
      cout << "IMPOSSIBLE" << endl;
    }
    else {
      cout << ans << endl;
    }
  }
}
