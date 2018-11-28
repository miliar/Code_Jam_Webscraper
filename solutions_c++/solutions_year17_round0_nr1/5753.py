#include<bits/stdc++.h>
using namespace std;

int main(){
  
  int t;
  cin>>t;

  string s;
  int n;
  
  for(int T=1;T<=t;T++){
    
    cin>>s;
    cin>>n;

    int cnt=0;
    
    for(int i=0;i<s.size()-n+1;i++)
      if(s[i]=='-'){
	for(int j=0;j<n;j++)
	  s[i+j]=(s[i+j]=='-'?'+':'-');
	cnt++;
      }
    
    bool flag=true;
    
    for(int i=0;i<s.size();i++)
      if(s[i]=='-')flag=false;
    
    cout<<"Case #"<<T<<": ";
    if(flag)cout<<cnt<<endl;
    else cout<<"IMPOSSIBLE"<<endl;
  }
  
  return 0;
}
