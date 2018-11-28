#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;

const int MM = 1e9 + 7;
const double eps = 1e-8;
const int MAXN = 2e6 + 10;

ll n, k;

void prework(){

}

void read(){

}

map<ll, ll> mp;

void solve(int casi){
	cout << "Case #" << casi << ": ";
	cin >> n >> k;
	mp.clear();
	mp[-n] = 1;
	k--;
	for(; k != 0; ){
		auto maki = mp.begin();
		ll R = -maki->first, CNT = maki->second;
		mp.erase(maki);
		if (k >= CNT){
			k -= CNT;
			if (R % 2 == 1){
				mp[-(R/2)] += CNT * 2;
			}
			else{
				mp[-(R/2)] += CNT;
				mp[-(R/2-1)] += CNT;
			}
		}
		else{
			mp[-R] = CNT - k;
			CNT = k;
			k = 0;
			if (R % 2 == 1){
				mp[-(R/2)] += CNT * 2;
			}
			else{
				mp[-(R/2)] += CNT;
				mp[-(R/2-1)] += CNT;
			}
		}
	}
	auto maki = mp.begin();
	ll R = -maki->first, CNT = maki->second;
	if (R % 2 == 1)
		cout<<R/2<<' '<<R/2<<endl;
	else
		cout<<R/2<<' '<<max(0ll, R/2-1)<<endl;
}

void printans(){

}


int main(){
	std::ios::sync_with_stdio(false);
	prework();
	int T = 1;
	cin>>T;
	for(int i = 1; i <= T; i++){
		read();
		solve(i);
		printans();
	}
	return 0;
}


