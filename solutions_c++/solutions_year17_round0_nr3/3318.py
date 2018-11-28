#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <stdio.h>
#include <map>
#include <vector>
#include <queue>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
#define min(a,b) a>b ? b:a
#define INF 987654321
typedef long long ll;
ll n;
ll k;
void main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;  // read t. cin kNs that t is an int, so it reads it as such.
	for (int test = 1; test <= t; ++test) {
		scanf("%lld%lld", &n, &k);
		map<ll, ll> m;
		queue<ll> q;
		m[n] = 1;
		q.push(n);
		vector<ll> v;
		v.push_back(n);
		while (!q.empty()){
			ll N = q.front();
			q.pop();
			if (N > 1)
				if (N % 2 == 0){
					ll next1 = N / 2;
					ll next2 = N / 2 - 1;

					if (m.count(next2) == 0){
						v.push_back(next2);
						q.push(next2);
					}
					if (m.count(next1) == 0){
						v.push_back(next1);
						q.push(next1);
					}
					m[next1] += m[N];
					m[next2] += m[N];
				}
				else{
					ll next = N / 2;
					if (m.count(next) == 0){
						v.push_back(next);
						q.push(next);
					}
					m[next] += m[N] * 2;
				}
		}
		sort(v.begin(), v.end());
		ll ans;

		for (int i = v.size() - 1; i >= 0; i--){
			k -= m[v[i]];
			if (k <= 0){
				ans = v[i];
				break;
			}
		}


		if (ans % 2 == 1)
			printf("Case #%d: %lld %lld\n", test, ans / 2, ans / 2);
		else
			printf("Case #%d: %lld %lld\n", test, ans / 2, ans / 2 - 1);
	}
}