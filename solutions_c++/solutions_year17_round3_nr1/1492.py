#include <bits/stdc++.h>

#define PI acos(-1)

using namespace std;

int n, k;
long long r[1001], h[1001];

inline long double get(long long R, int idx) {
	vector <long long> v;
	for(int i=0; i<n; i++) if(r[i] <= R && i != idx) v.push_back(r[i]*h[i]);
	if(v.size() < k-1) return 0;
	sort(v.begin(), v.end());
	reverse(v.begin(), v.end());
	long long res = r[idx]*h[idx];
	for(int i=0; i<k-1; i++) res += v[i];
	return res * 2 * PI + PI * R * R;
}

inline long double solve() {
	cin >> n >> k;
	for(int i=0; i<n; i++) cin >> r[i] >> h[i];
	long double mx = 0;
	for(int i=0; i<n; i++) mx = max(mx, get(r[i], i));
	return mx;
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int TC;
	cin >> TC;
	for(int QQ = 1; QQ <= TC; QQ++) {
		cout << "Case #" << QQ << ": ";
		cout << fixed << setprecision(13) << solve() << '\n';
	}
	return 0;
}