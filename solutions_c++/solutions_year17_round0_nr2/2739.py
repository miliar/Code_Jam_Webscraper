#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
typedef long long int ll;


void solve() {
  string s;
  cin>>s;
  int ptr=1;
  int n=s.size();
  while(ptr<n) {
    if(s[ptr]<s[ptr-1]) {--ptr;break;}
    ptr++;
  }
  if(ptr!=n) {
    for(int i=ptr+1;i<n;++i) s[i]='9';
    while(ptr>=0) {
      s[ptr]--;
      if(ptr+1<n) s[ptr+1]='9';
      if(ptr==0 || s[ptr]>=s[ptr-1]) break;
      --ptr;
    }
    while(s[0]=='0')s=s.substr(1);
  }
  cout<<s<<endl;;


}
int main() {
  int t;cin>>t;REP(i,t) {
    cout<<"Case #"<<(i+1)<<": ";
    solve();
  }

}
