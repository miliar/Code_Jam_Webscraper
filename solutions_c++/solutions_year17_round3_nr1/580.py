#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
const double pi = acos(-1);
int n, k;
vector<pair<int, int> > v;
double calc(int in) {
	double ret = 0;
	priority_queue<double> q;
	for (int i = 0; i < n; i++) {
		if (v[i].first <= v[in].first && i != in) {
			q.push(2 * pi * v[i].first * v[i].second);
		}
	}
	if (q.size() < k - 1) return -1e20;
	int c = 0;
	while (c < k - 1) {
		c++;
		ret += q.top();
		q.pop();
	}
	return ret;
}

int main() {

	freopen("readin.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	while (t--) {
		static int tc = 1;
		scanf("%d%d", &n, &k);
		v.clear();
		v.resize(n);
		for (int i = 0; i < n; i++) {
			scanf("%d%d", &v[i].first, &v[i].second);
		}
		double ans = 0;
		for (int i = 0; i < n; i++) {
			double r = v[i].first, h = v[i].second;
			ans = max(ans, calc(i) + pi * r * r + 2.0 * r * pi * h);
		}
		printf("Case #%d: ", tc++);
		cout << fixed << setprecision(9) << ans << endl;
	}

	return 0;
}
