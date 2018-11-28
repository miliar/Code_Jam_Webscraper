#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <unordered_map>
#include <unordered_set>

using namespace std;
typedef long long ll;

pair<ll, ll> func(ll n, ll k){
	map<ll, ll> mp;
	mp.insert(make_pair(-n, 1));
	while(1) {
		auto it = mp.begin();
		ll sv = -it->first;
		ll cnt = it->second;
		mp.erase(it);
		if(sv == 1){
			break;
		}
		k -= cnt;
		ll buf = sv - 1;
		ll a = buf / 2;
		ll b = buf - a;
		if(k <= 0){
			return make_pair(b, a);
		}
		mp[-a] += cnt;
		mp[-b] += cnt;
	}

	return make_pair(0, 0);
}

int main(){

#ifdef _CONSOLE
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int countTest;
	cin>>countTest;	
	for(int test = 1; test <= countTest; test++){
		ll n, k;
		cin>>n>>k;

		pair<ll, ll> ans = func(n, k);

		printf("Case #%d: ", test);
		cout<<ans.first<<" "<<ans.second<<"\n";

		cerr<<test<<"\n";
	}
	
	return 0;
}

