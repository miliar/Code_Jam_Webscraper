// g++-6 test.cpp

#include <bits/stdc++.h>

using namespace std;

// {{ templetes
#define rep1(i, s, e) for(int i = (s) ; i < (e) ; ++i)
#define rep(i, n)  for(int i = (0) ; i < (n) ; ++i)
#define clr(a, val)  memset(a, val, sizeof a)

#define all(v) v.begin(), v.end()
#define sz(v) (int)v.size()
#define pb  push_back
#define mkp make_pair

#define fi first
#define se second

#define dbg cout << "" 

#define endl '\n'

typedef long long ll;
typedef pair<int, int> pii;

const int mod = 1000000007; 
const int MAX = 100005;

// }} templetes

bool ok (int x) {
	bool ret = true;
	int pre = x % 10 ;
	x /= 10 ;
	while(x) {
		int dig = x % 10;
		if(dig > pre) {
			ret = false;
			break;
		}
		pre = dig;
		x = x / 10;
	}
	return ret;
}

int main() {
	//ios::sycn_with_stdio(0) ;
	int t; cin >> t;
	int ip = 1 ;
	while(t--) {
		int n; cin >> n; 
		for(int i = n ; i >= 1 ; --i) {
			int tmp = i ;
			if(ok(tmp)) {
				printf("Case #%d: %d\n", ip++, tmp);
				break;
			}
		}
	}
	return 0;
}