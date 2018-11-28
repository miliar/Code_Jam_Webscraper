#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <string>
#include <cstring>
#include <cassert>
#include <climits>
using namespace std;

typedef long long ll;

template<typename TH>
void debug_vars(const char* data, TH head){
	cerr << data << "=" << head << "\n";
}

template<typename TH, typename... TA>
void debug_vars(const char* data, TH head, TA... tail){
	while(*data != ',') cerr << *data++;
	cerr << "=" << head << ",";
	debug_vars(data+1, tail...);
}

#ifdef LOCAL
#define debug(...) debug_vars(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) {}
#endif

/////////////////////////////////////////////////////////

const ll maxN = 1e18+10;

vector<ll> slot;

ll pow2(int n) 
{
	ll ret = 1LL;
	while(n--) ret*=2;
	return ret;
}

void init() 
{
	ll a = 1LL;
	slot.push_back(a);
	while(a<maxN) {
		a*=2LL;
		slot.push_back(slot.back()+a);	
	}
}

pair<ll, ll> solve(ll n, ll k) 
{
	ll ans;
	int index = lower_bound(slot.begin(), slot.end(), k) - slot.begin();
	if (index==0) {
		ans = n;
	} else {
		--index;
		debug(index);
		ll value = slot[index];
		n-=value;
		k-=(value+1);
		debug(value, n, k);
		ll q = pow2(index+1);
		ll d = n/q;
		ll r = n%q;
		debug(q, d, r);
		ans = d;
		if (k < r) ans++;

		debug(ans);
	}

	ans--;

	ll a = ans/2;
	ll b = ans/2;

	if (2LL*a!=ans) {
		b++;
	}

	debug(a, b);
	return {b, a};
}

int main()
{
	init();
	int t;
	cin>>t;
	for (int T = 1; T <= t; ++T) {
		ll n,k;
		cin>>n>>k;
		auto it = solve(n, k);
		cout<<"Case #"<<T<<": "<<it.first<<" "<<it.second<<"\n";
	}
}
