// 
#include "bits/stdc++.h"
#define ll long long
using namespace std;
const int N=1e5+1;
string s;
int k;
void flip(int i){
	for(int j=i;j<i+k;j++){
		if(s[j]=='+') s[j]='-';
		else s[j]='+';
	}
}
bool find(){
  for(int i=0;i<s.length();i++){
    if(s[i]=='-') return 0;
  }	
  return 1;
}
int main(){
     int t;
     cin>>t;
     int r=1;
     while(t--){
		cin>>s;
		cin>>k;
		int flag=0;
		int cnt=0;
		for(int i=0;i<s.length()-k+1;i++){
		   if(s[i]=='-'){
		      flip(i);
		      cnt++;
		   }
		   bool e=find();
		   if(e==1) {
				  flag=1;
				  break;
		   }
		}
		if(flag==0) 
		cout<<"Case #"<<r++<<": "<<"IMPOSSIBLE"<<endl;
		else
		cout<<"Case #"<<r++<<": "<<cnt<<endl;
	 }
return 0;
}

