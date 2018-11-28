#include <fstream>
#include <algorithm>

using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

typedef long double ld;

const int MAXN = 1000;
const ld INF = 1e18;
const ld M_PI = 3.14159265358979323846;

struct pan {
	ld r, h;
};

bool operator < (pan a, pan b) {
	return a.r > b.r;
}

int n, k;
pan p[MAXN];
ld d[MAXN];

ld solve() {
	cin >> n >> k;
	for (int i = 0; i < n; ++i)
		cin >> p[i].r >> p[i].h;
	sort(p, p + n);
	for (int i = 0; i < k; ++i)
		d[i] = -INF;
	for (int i = 0; i < n; ++i) {
		for (int j = k - 1; j > 0; --j)
			d[j] = max(d[j], d[j - 1] + 2 * M_PI * p[i].r * p[i].h);
		d[0] = max(d[0], M_PI * p[i].r * p[i].r + 2 * M_PI * p[i].r * p[i].h);
	}
	return d[k - 1];
}

int main() {
	ios_base::sync_with_stdio(0);
	cout.precision(10);
	cout << fixed;
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		cout << "Case #" << i << ": " << solve() << endl;
	cin >> t;
	return 0;
}