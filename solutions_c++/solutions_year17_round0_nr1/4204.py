#include<bits/stdc++.h>
using namespace std;
int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    string s;
    int d;
    cin>>s>>d;
    int ans=0;
    for(int j=0;j<s.size()+1-d;j++)
      if(s[j]=='-'){
	for(int k=j;k<j+d;k++){
	  if(s[k]=='-')s[k]='+';
	  else s[k]='-';
	}
	ans++;
      }
    for(int j=0;j<s.size();j++)if(s[j]=='-')ans=-1;
    cout<<"Case #"<<i<<": ";
    if(ans!=-1)cout<<ans<<endl;
    else cout<<"IMPOSSIBLE"<<endl;
  }
  return 0;
}
