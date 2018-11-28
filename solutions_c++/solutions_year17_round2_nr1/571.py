#include <bits/stdc++.h>
using namespace std;

const int SIZE = 1005;

#define fi first
#define se second

long long N,D;
pair<long long,long long> arr[SIZE];

double solve() {
	double ans = 1e18;
	for (int i = 0; i < N; i++) {
		ans = min(ans, 1.0 * D / (1.0 * (D - arr[i].fi) / arr[i].se) );
	}
	return ans;
	/*
	arr[N++] = make_pair(D, 0);
	sort(arr, arr + N);

	double ans = 1e18;
	double timePassed = 0;

	while (N > 1) {
		double min_time = 1e18;
		long long id = -1;

		for (long long j = 0; j < N - 1; j++) {
			long long dist = (arr[j + 1].fi - arr[j].fi);
			long long speedDiff = (arr[j].se - arr[j+1].se);
			if (speedDiff > 0) {
				double tm = 1.0 * dist / speedDiff;
				if (tm < min_time) {
					min_time = tm;
					id = j;
				}
			}
		}
 
		long long l = 0;
		for (long long j = 0; j < N; j++) {
			if (j != id) {
				arr[j].first += arr[j].second * min_time;
				arr[l++] = arr[j];
			}
		}

		N--;
		timePassed += min_time;

		ans = min(ans, 1.0 * arr[0].fi / timePassed);
	}
	return ans;*/
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin>>t;
	for (long long t_id = 1; t_id <= t; t_id++) {
		cin>>D>>N;
		for (long long i = 0; i < N; i++) {
			long long k, s;
			cin>>k>>s;
			arr[i] = make_pair(k, s);
		}
		printf("Case #%lld: %.7lf\n", t_id, solve());
	}

	return 0;
}
