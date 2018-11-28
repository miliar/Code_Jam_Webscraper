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

void print(int test, ll ans) {
	cout << "Case #" << test << ": " << ans << endl;
	//printf("Case #%d: %d\n", test, ans);
}

void print(int test, string ans) {
	cout << "Case #" << test << ": " << ans << endl;
}

ll get_num(string s) {
	ll res = 0;
	for (int i = 0; i < s.length(); i++) {
		res = res * 10 + (s[i] - '0');
	}
	return res;
}

ll pows[20];

void init() {
	pows[0] = 1ll;
	for (int i = 1; i < 19; i++) {
		pows[i] = pows[i - 1] * 10ll;
	}
}

ll run(string s) {
	ll res = 0;
	ll s_num = get_num(s);
	int n = s.length();
	for (int i = 0; i < n; i++) {
		ll num = res * pows[n - i];
		for (int j = i; j < n; j++) {
			num += (s[i] - '0') * pows[n - j - 1];
		}
		if (num > s_num) {
			num = res * pows[n - i];
			num += ((s[i] - '0') - 1) * pows[n - i - 1];
			for (int j = i + 1; j < n; j++) {
				num += 9ll * pows[n - j - 1];
			}
			return num;
		}
		res = res * 10 + (s[i] - '0');
	}
	return s_num;
}

int main()
{
#ifdef INOUT
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	
	int tests;
	cin >> tests;
	ll ans = 0;
	init();
	for (int test = 1; test <= tests; test++) {
		string num;
		cin >> num;
		print(test, run(num));
	}
	
#ifdef TIME
	cerr << (double) clock() / CLOCKS_PER_SEC;
#endif 
	return 0;
}
