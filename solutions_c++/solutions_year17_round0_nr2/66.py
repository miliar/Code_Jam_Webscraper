#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int tt,n;
string s;

string get(char ch,int n) {
  string s="";
  for (int i=0;i<n;++i) s+=ch;
  return s;
}

string solve(string s) {
  int n = s.size();
  int cur = 0;
  bool flag=false;
  for (int i=1;i<n;++i) {
    if (s[i]>s[i-1]) cur=i;
    if (s[i]<s[i-1]) {
      flag=true;
      break;
    }
  }
  if (flag) {
    if (s[cur]=='1') return get('9',n-1);
    else return s.substr(0,cur)+char(s[cur]-1)+get('9',n-cur-1);
  } else return s;
}

int main() {
  freopen("b.in","r",stdin);
  freopen("b.out","w",stdout);
  
  cin >> tt;
  for (int ii=1;ii<=tt;++ii) {
    cin >> s;
    printf("Case #%d: ",ii);
    cout << solve(s) << endl;
  }
}