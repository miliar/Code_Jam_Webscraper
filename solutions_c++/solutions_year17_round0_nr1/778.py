#include <iostream>
#include <string>

using namespace std;

int flip(string &s, int len, int pos) {
  if (pos+len>s.size()) return 1;
  for (int i=0; i<len; ++i) {
    if (s[pos+i]=='-') s[pos+i]='+';
    else if (s[pos+i]=='+') s[pos+i]='-';
  }
  return 0;
}

int done(string &s) {
  for (int i=0; i<s.size(); ++i)
    if (s[i]=='-')
      return i;
  return -1;
}

int main() {
  int cas, len, ret, pos, fail;
  string s;
  cin>>cas;

  for (int k=1; k<=cas; ++k) {
    cin>>s>>len;
    ret = 0;
    fail = 0;

    while (1) {
      pos = done(s);
      if (pos<0) break;
      if (flip(s, len, pos)) {fail=1; break;}
      ++ret;
    }
    if (fail) cout<<"Case #"<<k<<": IMPOSSIBLE"<<endl;
    else cout<<"Case #"<<k<<": "<<ret<<endl;
  }

  return 0;
}
