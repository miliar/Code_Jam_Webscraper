#include<bits/stdc++.h>
using namespace std;

int main(){
	int l,j,t,i,x,k;
	string s;
	cin>>t;
	for(i=1;i<=t;i++){
		int A=0;
		cin>>s>>k;
		l=s.length();
		for(j=0;(j+k-1)<l;j++){
			if(s[j]=='+')	continue;
			A++;
			for(x=j;x<(j+k);x++){
				if(s[x]=='+')	s[x]='-';
				else	s[x]='+';
			}
		}
		bool ans=true;
		for(;j<l;j++){
			if(s[j]=='-'){
				ans=false;
				break;
			}
		}
		if(ans)	cout<<"Case #"<<i<<": "<<A<<endl;
		else	cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}