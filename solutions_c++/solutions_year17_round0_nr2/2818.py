#include <bits/stdc++.h>
#define ll long long
using namespace std;
const ll maxt=107;
ll N[maxt];
ll ret[maxt];

vector<ll> separate(ll num){
	vector<ll> ret;
	while(num){
		ret.push_back(num%10);
		num=num/10;
	}
	return ret;
}

vector<ll> manipulate(vector<ll> digits,ll num){
	ll n=0;
	while(n!=num){
		digits[n]=9;
		++n;
	}
	digits[n]=digits[n]==0?9:digits[n]-1;
	return digits;
}

ll powll(ll num,ll times){
	if(times==0)return 1;
	ll ret=num;
	for(ll a=0;a<times-1;++a){
		ret*=num;
	}
	return ret;
}

ll mix(vector<ll> digits){
	ll ret=0;
	for (ll a=0;a<digits.size();++a){
		ret+=digits[a]*powll(10,a);
	}
	return ret;
}

bool check(vector<ll> digits,ll& digit){
	bool check=true;
	ll maxD=digits.size();
	for(ll b=maxD-2;b>=0;--b){
		if(digits[b+1]>digits[b]){
			check=false;
			digit=b;
			break;
		}
	}
	return check;
}

int main(){
	ll T;
	cin>>T;
	for(ll a=0;a<T;++a)cin>>N[a];
	for(ll a=0;a<T;++a){
		ll digit=0;
		vector<ll> digits=separate(N[a]);
		while(!check(digits,digit)){
			digits=manipulate(digits,++digit);
			digits=separate(mix(digits));
		}
		ret[a]=mix(digits);
	}
    for(ll a=0;a<T;++a)cout<<"Case #"<<a+1<<": "<<ret[a]<<endl;
}
