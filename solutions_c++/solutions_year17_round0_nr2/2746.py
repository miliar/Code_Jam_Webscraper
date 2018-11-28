#include <bits/stdc++.h>
using namespace std;
#define ll long long
vector<ll> numbers;
const ll MAX = 1e18 + 100;
void dfs(ll n, int end){
	if(n != 0 && n < MAX) numbers.push_back(n);
	if( n > 2e17) return;
	ll m = n * 10;
	for(int i = end; i < 10; i++){
		dfs(m + i, i);
	}
}
int main(){
	dfs(0, 1);
	sort(numbers.begin(), numbers.end());
	cerr << numbers.size() << endl;
	cerr << "time taken = " << clock() / (double) CLOCKS_PER_SEC << endl;
	int t; ll n;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt ++){
		scanf("%lld", &n);
		auto it = upper_bound(numbers.begin(), numbers.end(), n);
		--it;
		printf("Case #%d: %lld\n", tt, *it);
	}
}