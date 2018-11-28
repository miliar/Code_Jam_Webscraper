#include<bits/stdc++.h>
using namespace std;
#define lli long long int

int main(){
	lli i,t,j,l,x;
	string s;
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>s;
		l=s.length();
		if(l==1){
			cout<<"Case #"<<i<<": "<<s<<endl;
			continue;
		}
		bool f;
		while(1){
			f=true;
			for(j=0;j<(l-1);j++){
				if((s[j]-'0')<=(s[j+1]-'0'))	continue;
				f=false;
				s[j]--;
				for(x=j+1;x<l;x++)	s[x]='9';
			}
			if(f)	break;
		}
		for(j=0;j<l;j++){
			if(s[j]!='0')	break;
		}
		cout<<"Case #"<<i<<": ";
		for(;j<l;j++){
			cout<<s[j];
		}
		cout<<endl;
	}	
	return 0;
}