// Problem A. Ample Syrup
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

#define	PI	3.14159265358979323846

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		int n, k, r, h;
		scanf("%d %d", &n, &k);
		vector<pair<int, double> > a(n);
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &r, &h);
			double t = 2.0 * PI * (double) h * (double) r;
			a.push_back(make_pair(r, t));
		}

		sort(a.begin(), a.end());

		double ans = 0;

		while (a.size() >= k) {
			vector<pair<double, int> > b;
			for (int i = 0; i < a.size(); i++)
				b.push_back(make_pair(a[i].second, a[i].first));
			sort(b.begin(), b.end());
			double t = 0.0;
			int max_r = 0;
			for (int i = 0; i < k; i++) {
				t += b[b.size() - i - 1].first;
				max_r = max(max_r, b[b.size() - i - 1].second);
			}
			t += (double) max_r * max_r * PI;

			if (t > ans) ans = t;

			b.clear();
			for (int i = 0; i < a.size() - 1; i++)
				b.push_back(make_pair(a[i].second, a[i].first));
			sort(b.begin(), b.end());
			t = (double) a[a.size() - 1].first * a[a.size() - 1].first * PI;
			t += a[a.size() - 1].second;
			for (int i = 0; i < k - 1; i++)
				t += b[b.size() - i - 1].first;

			if (t > ans) ans = t;

			a.erase(a.end() - 1);
		}

		printf("Case #%d: %.9f\n", ti, ans);
	}

	return 0;
}
