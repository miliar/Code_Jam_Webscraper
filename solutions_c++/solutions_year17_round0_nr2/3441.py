#include<bits/stdc++.h>
using namespace std;
#define int long long
bool check(string s){
  if(s[0]=='0') return 0;
  for(int i=0;i<(int)s.size()-1;i++)
    if(s[i]>s[i+1]) return 0;
  return 1;
}
string comp(string s1,string s2){
  return stol(s1)>stol(s2)?s1:s2;
}
signed main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    cout<<"Case #"<<t<<": ";
    int n;
    cin>>n;
    string s=to_string(n);
    if(check(s)){
      cout<<s<<endl;
      continue;
    }
    string ans;
    for(int i=0;i<(int)s.size()-1;i++) ans+="9";
    for(int i=0;i<(int)s.size()-1;i++){
      s[s.size()-1-i]='9';
      s[s.size()-2-i]--;
      if(check(s)) ans=comp(ans,s);
    }
    cout<<ans<<endl;
  }
  return 0;
}
