#include<bits/stdc++.h>

using namespace std;

#define ll long long int
#define pb push_back
#define f first
#define s second
#define mod 1e9+7
#define mp make_pair
#define PI 3.14159265
#define eps 0.000001

const int N = 1234567;

int k;

int sol(string s) {
	int n = s.size();
	int ans = 0;
	for(int i = 0; i < n; i++) {
		if(s[i] == '-') {
			if(i + k > n) return INT_MAX;
			else {
				ans++;
				for(int j = i; j < i + k; j++) {
					if(s[j] == '+') s[j] = '-';
					else s[j] = '+';
				}
			}
		}
	}
	return ans;
}

#define test
int main() {
	ios::sync_with_stdio(false); cin.tie(0);
#ifdef test
	freopen("a.in","rt",stdin);
	freopen("a.out","wt",stdout);
#endif
	int tt;
	cin >> tt;
	for(int ii = 1; ii <= tt; ii++) {
		cout << "Case #" << ii << ": ";
		string s;
		cin >> s >> k;
		int ans = sol(s);
		reverse(s.begin(), s.end());
		ans = min(ans, sol(s));
		if(ans != INT_MAX) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}