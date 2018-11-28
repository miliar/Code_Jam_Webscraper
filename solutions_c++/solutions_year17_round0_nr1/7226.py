#include <bits/stdc++.h>
using namespace std;

int main() {
	unordered_map<char,char> mp;
	mp['-']='+';
	mp['+']='-';
	long long int i,t,j,k,ct,m;
	string s;
	cin>>t;
	for(i=0;i<t;i++){
		cin>>s>>k;
		ct=0;
		for(j=0;j<=s.size()-k;j++){
			if(s[j]=='-'){
				for(m=j;m<=j+k-1;m++){
					s[m]=mp[s[m]];
				}
				ct++;
			}
		}
		int flag=1;
		for(j=s.size()-k+1;j<s.size();j++){
			if(s[j]=='-'){
				flag=0;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(flag){
			cout<<ct<<endl;
		}
		else{
			cout<<"IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}