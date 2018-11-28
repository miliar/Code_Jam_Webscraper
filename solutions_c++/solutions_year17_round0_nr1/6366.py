#include "bits/stdc++.h"
using namespace std;

int k,ans=0;

bool ck(string s){
	for(int i=0;i<s.length();i++){
		if(s[i]=='0')return 0;
	}
	return 1;
}
void solve(string& s,int k1){
	if(k1>s.length()-k)return ;
	for(int i=k1;i<s.length()-k+1;i++){
		if(s[i]=='0'){
			for(int j=i;j<i+k;j++){	
				if(s[j]=='0')s[j]='1';
				else s[j]='0';
			}
			break;
		}
	}
	int temp=-1;
	for(int i=0;i<s.length();i++){
		if(s[i]=='0'){
			temp=i;
			break;
		}
	}
	if(temp>=0){
		solve(s,temp);
	}
	ans++;
}

int main(){
//	read("t.txt");
//	write("t2.txt");
	int t,tc=1;
	string s;
	for(scanf("%d",&t);t--;){
		ans=0;
		cin>>s>>k;
		for(int i=0;i<s.length();i++){
			if(s[i]=='-')s[i]='0';
			else s[i]='1';
		}
		if(!ck(s))solve(s,0);
		if(ck(s))printf("Case #%d: %d\n",tc++,ans);
		else printf("Case #%d: IMPOSSIBLE\n",tc++);
	}
}
