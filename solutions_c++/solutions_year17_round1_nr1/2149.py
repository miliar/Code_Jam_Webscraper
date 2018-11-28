#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int T;
string b[26];
int r, c;

void process(string& s) {
  int it = 0;
  for(;it<c;it++) {
    if(s[it] == '?') break;
  }
  char ch;
  for(int i=0;i<c;i++) {
    if (s[i] != '?') {
      ch = s[i];
      for(;it<=i;it++) s[it] = s[i];
    }
  }
  for(;it<c;it++) s[it] = ch;
}

bool cc(const string & s) {
  for(int t =0 ;t<s.size();t++) if(s[t] != '?') return true;
  return false;
}

int main () {

  cin >> T;

  for(int tc=1;tc<=T;tc++) {
    cin >> r >> c;
    for(int i=0;i<r;i++) cin >> b[i];

    int x;
    for(x=0;x<r;x++) {
      int y = 0;
      for(y=0;y<c;y++) if (b[x][y] != '?') break;
      if (y != c) break;
    }
    process(b[x]);
    for(int i=x+1;i<r;i++) {
      if(!cc(b[i])) b[i] = b[i-1];
      else process(b[i]);
    }
    for(int i=x-1;i>=0;i--) {
      if(!cc(b[i])) b[i] = b[i+1];
      else process(b[i]);
    }

    printf("Case #%d:\n",tc);
    for(int i=0;i<r;i++) cout << b[i] << endl;
  }

  return 0;
}
