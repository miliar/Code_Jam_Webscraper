#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
typedef pair<long long, long long> ii;
const double pi = 3.1415926535897932384626433832795028841971;
vector<ii> v; //r, h
priority_queue<long long> rh;
long long sum;
long long rlt;
long double qqqq;
int main() {

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	long long t, n, k, buf1, buf2,cs=1;
	scanf("%lld", &t);
	for (long long i = 0; i < t; i++) {
		scanf("%lld %lld", &n, &k);

		for (long long j = 0; j < n; j++) {
			scanf("%lld %lld", &buf1, &buf2);
			v.push_back(ii(buf1, buf2));
		}

		sort(v.begin(), v.end());
		//puts("==");
		while (1) {
			if (n <= 0) break;
			long long lartgest_r = v[n - 1].first;
			sum = lartgest_r * lartgest_r;
			sum += 2 * v[n - 1].first * v[n - 1].second;
			for (long long ch = 0; ch < n - 1; ch++) {
				rh.push(2 * v[ch].first * v[ch].second);
			}

			for (long long qq = 1; qq <= k - 1 && !rh.empty(); qq++) {
				sum += rh.top(); rh.pop();
			}
			//puts("==");

			rlt = max(rlt, sum);
			n--;
			sum = 0;
		}
		qqqq = (long double)rlt * pi;
		printf("Case #%lld: %.9lf\n", cs++, qqqq);

		v.clear();
		while (!rh.empty()) rh.pop();
		rlt = 0;
		sum = 0;
	}

	return 0;
}