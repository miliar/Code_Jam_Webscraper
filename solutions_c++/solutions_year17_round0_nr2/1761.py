#include <bits/stdc++.h>
using namespace std;

bool check(string s) {
  int n=s.size();
  for(int i=0;i<n-1;i++) if(s[i]>s[i+1]) return false;
  return true;
}
string solve(string s) {
  int n = s.size();
  for(int i=0;i<n-1;i++) {
    if(s[i]>s[i+1]) {
      s[i]--;
      for(int j=i+1;j<n;j++) s[j]='9';
      break;
    }
  }
  if(!check(s)) return solve(s);
  return s;
}

int main() {
  int T;
  cin >> T;
  for(int cs=1;cs<=T;cs++) {
    string s;
    cin >> s;
    cout << "Case #" << cs  << ": ";
    s = solve(s);
    for(int i=0;i<s.size();i++) {
      if(s[i]>'0') {
	for(int j=i;j<s.size();j++) cout << s[j];
	cout << endl;
	break;
      }
    }
  }
}
