#include<bits/stdc++.h>
using namespace std;
int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    string n;
    cin>>n;
    bool f=1;
    while(f){
      f=0;
      for(int j=1;j<n.size();j++)
	if(n[j-1]>n[j]){
	  n[j-1]--;
	  f=1;
	  for(int k=j;k<n.size();k++)n[k]='9';
	}
    }
    cout<<"Case #"<<i<<": ";
    f=1;
    for(int j=0;j<n.size();j++){
      if(f&&n[j]=='0')continue;
      cout<<n[j];
      f=0;
    }
    cout<<endl;
  }
  return 0;
}
