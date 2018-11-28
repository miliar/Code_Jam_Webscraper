#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long ll;
int t;
ll k, n;

int main(void) {
	FILE *fin = fopen("C-large.in", "r");
	FILE *fout = fopen("output.txt", "w");

	fscanf(fin, "%d", &t);
	for (int iter = 1; iter <= t; iter++) {
		fprintf(fout, "Case #%d: ", iter);
		fscanf(fin, "%lld%lld", &n, &k);

		vector<pair<ll, ll>> v = { {n, 1} };
		ll nsplit = 0;
		bool finish = false;
		while (true) {
			vector<pair<ll, ll>> tmp;
			for (auto p : v) {
				ll dist = p.first, cnt = p.second;
				dist--;
				ll m1 = max(dist / 2, dist - dist / 2), m2 = min(dist / 2, dist - dist / 2);
				
				if (k <= nsplit + cnt) {
					finish = true;
					fprintf(fout, "%lld %lld\n", m1, m2);
					break;
				}

				bool inserted = false;
				for (int i = 0; !inserted && i < tmp.size(); i++)
					if (tmp[i].first == m1) {
						tmp[i].second += cnt;
						inserted = true;
					}
				if (!inserted) tmp.push_back({ m1, cnt });

				inserted = false;
				for (int i = 0; !inserted && i < tmp.size(); i++)
					if (tmp[i].first == m2) {
						tmp[i].second += cnt;
						inserted = true;
					}
				if (!inserted) tmp.push_back({ m2, cnt });
				nsplit += cnt;
			}
			if (finish) break;
			v = tmp;
			sort(v.begin(), v.end(), greater<pair<ll, ll>>());
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}