#include "bits/stdc++.h"
#define ll long long
#define K ll t; cin>>t; for(ll Th=1;Th<=t;Th++)
using namespace std;
int main(){
	K{
		bool flag=true;
		ll count=0;
		string s; ll k;
		cin>>s>>k; ll l=s.length();
		ll z=0;
		while(1){
			if(z>=l) break;
			if(s[z]=='+') {z++;continue;}
			else{
				ll right=z+k-1;
				if(right>=l) {flag=false;break;}
				count++;
				for(int i=z;i<=right;i++){
					if(s[i]=='+') s[i]='-';
					else s[i]='+';
				}
			}
		}
		if(flag)cout<<"Case #"<<Th<<": "<<count<<'\n';
		else cout<<"Case #"<<Th<<": "<<"IMPOSSIBLE"<<'\n';
	}
		
	return 0;
}
