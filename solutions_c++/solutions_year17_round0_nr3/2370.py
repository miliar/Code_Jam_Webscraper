#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define mod 1000000007
#define what_is(x) cerr << #x << " is " << x << endl

ll reachCounter = 0;
#define Reached cout<<"Reached here with Counter #"<<reachCounter<<"\n", reachCounter++;

#define N 200005

#define newLine	printf("\n");

#define sll(X) scanf("%lld", &X);
#define pll(X) printf("%lld", X);
#define printAll(X, n)	for(int i=0;i<n;i++)	printf("%lld ", X[i]); newLine;
#define scanAll(X, n)	for(int i=0;i<n;i++)	scanf("%lld", &X[i]);

ll n, k;

int main() {
	freopen("inCLarge", "r", stdin);
	freopen("outCLarge", "w", stdout);

	ll t;
	sll(t);
	for(int cases = 1; cases <= t; cases ++) {
		sll(n);	sll(k);

		cout<<"Case #"<<cases<<": ";
		map<ll, ll> mp;
		mp[-n] = 1;
		ll ans = 0;
		while(1) {
			map<ll, ll>::iterator it = mp.begin();
			// cout<<it->first<<" here\n";
			if((-it->first)&1LL) {
				if(k <= it->second) {
					ans = -it->first;
					break;
				}
				k -= it->second;
				mp[it->first/2] += 2 * it->second;
				mp.erase(it->first);
			} else {
				if(k <= it->second) {
					ans = -it->first;
					break;
				}
				k -= it->second;
				mp[-(-it->first/2 - 1)] += it->second;
				mp[it->first/2] += it->second;
				mp.erase(it->first);
			}
		}
		ll ans1 = 0, ans2 = 0;
		if(ans&1LL) {
			ans1 = ans / 2;
			ans2 = ans / 2;
		} else {
			ans1 = ans / 2;
			ans2 = ans / 2 - 1;
		}
		cout<<ans1<<" "<<ans2<<"\n";
	}
	return 0;
}