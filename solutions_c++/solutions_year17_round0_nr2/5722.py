#include<bits/stdc++.h>
using namespace std;



int main(){
  
  int t;
  cin>>t;

  for(int T=1;T<=t;T++){
    
    string s;
    cin>>s;

    int idx=-1;
    for(int i=0;i<s.size()-1;i++){
      
      if(s[i]>s[i+1]){
	
	for(int j=i;j>=0;j--)
	  if(s[j]>s[j+1])idx=j,s[j]--;
	
	break;
      }
      
    }
    
    if(idx!=-1){
      for(int i=idx+1;i<s.size();i++)s[i]='9';
      if(s[0]=='0')s=s.substr(1,s.size()-1);
    }
    
    cout<<"Case #"<<T<<": "<<s<<endl;
  }
  
  return 0;
}
