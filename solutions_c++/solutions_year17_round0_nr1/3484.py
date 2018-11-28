#include<bits/stdc++.h>
using namespace std;
#define int long long
signed main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    cout<<"Case #"<<t<<": ";
    string s;
    int k;
    cin>>s>>k;
    int n=s.size(),ans=0;
    for(int i=0;i<=n-k;i++){
      if(s[i]!='+'){
	ans++;
	for(int j=0;j<k;j++){
	  if(s[i+j]=='+') s[i+j]='-';
	  else s[i+j]='+';
	}
      }
    }
    bool f=1;
    for(int i=0;i<n;i++) f&=s[i]=='+';
    //cout<<s<<endl;
    if(f) cout<<ans<<endl;
    else  cout<<"IMPOSSIBLE"<<endl;
  }
  return 0;
}
