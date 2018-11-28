#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;

map<pll, pll> cac;

pll go(pll p){
	if(cac.count(p)) return cac[p];
	ll v = p.first - 1;

	ll v1 = v/2;
	ll v2 = v - v1;

	ll k = p.second;
	if(k == 0) return make_pair(v1, v2);
	--k;
	ll k1 = k/2;
	ll k2 = k - k1;

	pll p1 = go(make_pair(v1, k1));
	pll p2 = go(make_pair(v2, k2));
	return cac[p] = max(p1, p2);

}

int main(){
	int T;
	cin >> T;
	for(int tc=1; tc <= T; ++tc){
		pll p;
		cin >> p.first >> p.second;
		--p.second;
		pll ret = go(p);
		cout << "Case #" << tc << ": " << ret.second << " " << ret.first << endl;
	}
}