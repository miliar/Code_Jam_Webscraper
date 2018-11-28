#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i = 0; i < int(n); ++i)
#define trav(a,x) for(auto &a : x)

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

bool isTidy(ll n){
	ll curr = 9;
	while(n){
		if(n%10 > curr) return 0;
		curr = n%10;
		n /= 10;
	}
	return 1;
}

int main(){
	cin.sync_with_stdio(0);
	int t;
	cin >> t;
	rep(id,t){
		ll n;
		cin >> n;

		for(ll i = n; i >= 0; --i){
			if(isTidy(i)){
				cout << "Case #" << id+1 << ": " << i << endl;
				break;
			}
		}
	}
	exit(0);
}