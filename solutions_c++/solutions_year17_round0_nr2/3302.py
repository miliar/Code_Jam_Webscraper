#include <bits/stdc++.h>
using namespace std;

#define pb         push_back

typedef long long ll;
const ll INF = 1000000000000000000ll;
const ll MOD = 1000000007ll;
const double EPS = 1e-8;

bool check(ll num){
	ll bef = 10;
	while(num > 0){
		ll x = num % 10;
		if(x > bef) return false;

		num /= 10;
		bef = x;
	}
	return true;
}

int main(void) {
	//ios_base::sync_with_stdio(false);
	//cin.tie(0);
	
	int t;
	cin >> t;

	for(int l=1; l<=t; l++){
		ll ans = 0;
		string n;
		cin >> n;

		for(int i=n.size()-1; i>=1; i--){
			if((n[i-1] - '0') > (n[i] - '0')){
				for(int j=i; j<n.size(); j++){
					n[j] = '9';
				}
				n[i-1]--;
			}
		}

		//cout << n << endl;

		printf("Case #%d: ", l);
		bool f = true;
		for(int i=0; i<n.size(); i++){
			if(f && n[i] == '0'){
					
			}else{
				f = false;
				cout << n[i];
			}
		}
		puts("");
	}
	
	return 0;
}
