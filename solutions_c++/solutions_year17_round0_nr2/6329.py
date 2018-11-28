#include "bits/stdc++.h"
using namespace std;

typedef long long ll;

ll solve(ll n){
	string s=to_string(n);
	ll temp=-1;
	for(ll i=s.length()-1;i>=1;i--){
		if((s[i]-'0')>=(s[i-1]-'0'))continue;
		else {
			s[i]='9';
			s[i-1]--;
			temp=i;
		}
	}
	if(temp!=-1){
		for(ll i=temp;i<s.length();i++){
			s[i]='9';
		}
	}
	if(s[0]=='0')s.erase(0,1);
	ll z=stoll(s);
	return z;
}

int main(){
	read("t.txt");
	write("t1.txt");
	int t,tc=1;
	for(scanf("%d",&t);t--;){
		ll num;
		scanf("%lld",&num);
		printf("Case #%d: %lld\n",tc++,solve(num));
	}
}
