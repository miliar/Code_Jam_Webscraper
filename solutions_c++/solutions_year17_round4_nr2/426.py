#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int t, n, m, c;
int ct[1005], ctc[1005]; //how many tickets of type i

int ok(int d) {
	int tot = 0;
	int r[1005], prom[1005];
	memset(prom, 0, sizeof(prom));

	for (int i = 0; i < n; ++i)
		r[i] = ct[i];
	queue<int> q;
	for (int i = 0; i < n; ++i)
		if (r[i] > d)
			q.push(i);

	while (!q.empty()) {
		int t = q.front();
		q.pop();
		if (r[t] <= d)
			continue;
		if (t == 0)
			return -1;
		if (prom[t] >= r[t]-d) {
			prom[t] -= (r[t]-d);
			prom[t-1] += (r[t]-d);
		} else {
			prom[t] = 0;
			prom[t-1] += r[t]-d;
		}

		r[t-1] += r[t]-d;
		r[t] = d;
		if (r[t-1] > d)
			q.push(t-1);
	}

	for (int i = 0; i < n; ++i)
		tot += prom[i];
	return tot;
}

void doit(int abc) {
	cout << "Case #" << abc+1 << ": ";
	memset(ct, 0, sizeof(ct));
	memset(ctc, 0, sizeof(ctc));

	cin >> n >> c >> m;
	for (int i = 0; i < m; ++i) {
		int pi, bi;
		cin >> pi >> bi;
		pi--, bi--;
		ct[pi]++;
		ctc[bi]++;
	}

	int ma = 0;
	for (int i = 0; i < c; ++i)
		ma = max(ma, ctc[i]);
	int lo = ma, hi = m;

	while (lo != hi) {
		int mid = (lo + hi)/2;
		if (ok(mid) == -1) {
			lo = mid+1;
		} else
			hi = mid;
	}

	cout << lo << ' ' << ok(lo) << endl;
}

int main() {
	cin >> t;
	for (int i = 0; i < t; ++i)
		doit(i);
}