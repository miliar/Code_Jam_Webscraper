#include <bits/stdc++.h>
using namespace std;
int main(){
	int T,k;
	cin>>T;
	for(int t=1;t<=T;t++){
		int f1=1,f2=1,j,c1=0,c2=0;
		string s;
		cin>>s;
		string s2=s;
		cin>>k;
		for(j=0;j<=s.size()-k;j++){
			if(s[j]=='-'){
				//cout<<j<<" j"<<endl;
				c1++;
				for(int l=j;l<j+k;l++){
					if(s[l]=='-') s[l]='+';
					else s[l]='-';
				}
			}
		}
		for(;j<s.size();j++) if(s[j]=='-') f1=0;
		//cout<<f1<<" "<<c1<<endl;
		s=s2;
		for(j=s.size()-1;j>=k-1;j--){
			if(s[j]=='-'){
				//cout<<j<<" j"<<endl;
				c2++;
				for(int l=j;l>j-k;l--){
					if(s[l]=='-') s[l]='+';
					else s[l]='-';
				}
			}
		}
		for(;j>=0;j--) if(s[j]=='-') f2=0;
		//cout<<f2<<" "<<c2<<endl;
		if(f1&f2) cout<<"Case #"<<t<<": "<<min(c1,c2)<<endl;
		else if(f1) cout<<"Case #"<<t<<": "<<c1<<endl;
		else if(f2) cout<<"Case #"<<t<<": "<<c2<<endl;
		else cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}