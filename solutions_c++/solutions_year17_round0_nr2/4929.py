#include<bits/stdc++.h>

using namespace std;

bool cmp(string a, string b){
  assert(a.length() == b.length());
  for(int i=0;i<a.length();i++){
    if(a[i] < b[i]) return true;
    if(a[i] > b[i]) return false;
  }
  return true;
}

void solve(){
  string s; cin >> s;
  for(int i=0;i<s.length();i++){
    string lb = s.substr(0, i);
    for(int e=i;e<s.length();e++){
      lb = lb + s[i];
    }
    if(cmp(lb, s)){
      continue;
    }
    string ans = s.substr(0,i);
    if(s[i] != '1') ans = ans + (char)(s[i] - 1);
    for(int e=i+1;e<s.length();e++){
      ans = ans + '9';
    }
    cout << ans << "\n";
    return;
  }
  cout << s << "\n";
}

int main(){
  int T; cin >> T;
  for(int i=0;i<T;i++){
    cout << "Case #" << i+1 <<": ";
    solve();
  }
}

