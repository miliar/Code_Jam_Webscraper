#include <bits/stdc++.h>

#define ll long long
#define __(x) cout << #x << " : " << x << endl;
#define out(a, i, n) for (int i = 0; i < n; i++) cout << a[i] << " "; cout << endl;
#define mp make_pair
#define pb push_back
#define forn(i, n) for (int i = 0; i < n; i++)
#define N 1111

#define INOUT
#define TIME	

using namespace std;

void print(int test, int ans) {
	cout << "Case #" << test << ": " << ans << endl;
	//printf("Case #%d: %d\n", test, ans);
}

void print(int test, string ans) {
	cout << "Case #" << test << ": " << ans << endl;
}

void print(int test, ll res1, ll res2) {
	cout << "Case #" << test << ": " << res1 << " " << res2 << endl;
}

priority_queue <ll> q;

pair <ll, ll> get_next(ll n) {
	if (n & 1) {
		return mp((n - 1) / 2, (n - 1) / 2);
	} else {
		return mp(n / 2, n / 2 - 1);
	}
}

int main()
{
#ifdef INOUT
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		ll n, k;
		map < ll, ll > m;
		cin >> n >> k;
		m[n] = 1;
		ll kk = 0;
		while (kk < k) {
			map < ll, ll >::iterator it = m.end();
			it--;
			if (kk + it->second >= k) {
				pair <ll, ll> next_pair = get_next(it->first);
				print(test, next_pair.first, next_pair.second);
				break;
			}
			kk += it->second;
			pair <ll, ll> next_pair = get_next(it->first);
			m[next_pair.first] += it->second;
			m[next_pair.second] += it->second;
			m.erase(it);
		}
	}

#ifdef TIME
	cerr << (double) clock() / CLOCKS_PER_SEC;
#endif 
	return 0;
}
