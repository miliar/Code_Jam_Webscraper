#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool ok(string s){
  string s1=s;
  sort(s1.begin(),s1.end());
  return s1==s;
}

string fix(string s){
  string ans=s;
  for(int i=1; i<s.size(); i++){
    if(s[i]<s[i-1]){
      if(((i==1) && s[i-1]=='1') || s[i-1]==0){
        ans=string(s.size()-1, '9');
      }else{
        ans=s;
        ans[i-1]--;
        for(int j=i; j<ans.size(); j++) ans[j]='9';
      }
    }
  }
  return ans;
}

int main() {
  int T; cin>>T;
  for(int t=1; t<=T; t++){
    string s; cin>>s;
    string ans=s;
    while(!ok(ans)) ans = fix(ans);
    printf("Case #%d: %s\n", t, ans.c_str());
  }
}
