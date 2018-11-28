#include<bits/stdc++.h>
#define rep(x,a,b) for(x=a;x<b;x++)
#define SIZE
typedef long long int ll;
using namespace std;
ll i,j,kase;
bool fixed(string str){
	bool flag=true;
	for(i=0;i<str.length()-1;i++){
		if(str[i]>str[i+1]){
			flag=false;
			break;
		}	
	}
	return flag;
}
int main(){
	ios::sync_with_stdio(false);
	//cin.tie(0);'
	ll t;
	cin>>t;
	for(kase=1;kase<=t;kase++){
		string str;
		cin>>str;
		ll n=str.length();
		string ans;
		ll breflag;
		while(!fixed(str)){
			for(i=1;i<n;i++){
				if(str[i]<str[i-1]){
					breflag=i;
					break;
				}	
			}
			if(breflag>0 && breflag<n){
				str[breflag-1]=str[breflag-1]-1;
				for(i=breflag;i<n;i++){
					str[i]='9';
				}
			}
		}
		bool flag=false;
		cout<<"Case #"<<kase<<": ";
		for(i=0;i<n;i++){
			if(str[i]!='0'){
				flag=true;
			}
			if(flag)
				cout<<str[i];	
		}
		cout<<endl;
	}
	return 0;
}

