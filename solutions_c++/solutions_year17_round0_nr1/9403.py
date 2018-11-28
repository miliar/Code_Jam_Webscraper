#include <bits/stdc++.h>

using namespace std;

int main(){
  int t , k;
  string s;
  cin>>t;
   int ct=1;
  while(t--){
    cin>>s>>k;
    bool sw=true;
    for(int i=0 ; i<s.length(); i++){
      if(s[i]=='-') sw=false;
    }
    if(sw) cout<<"Case #"<<ct<<": 0"<<endl;
    else{
      int c=0;
      for(int i=0 ; i<=s.length()-k; i++){
	if(s[i]=='-'){
	  c++;
	  for(int j=i ; j<i+k; j++){
	    if(s[j]=='-') s[j]='+';
	    else s[j]='-';
	  }
	}
      }
       bool sw2=true;
      for(int i=0 ;i<s.length();i++){
      	 if(s[i]=='-') sw2=false;
      }
      if(!sw2) cout<<"Case #"<<ct<<": IMPOSSIBLE"<<endl;
      else cout<<"Case #"<<ct<<": "<<c<<endl;
     
    }
     ct++;
  }
  return 0;
}
