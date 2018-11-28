#include <bits/stdc++.h>
using namespace std;
const long double pi = 3.14159265358979323846;

bool cmp (const pair<pair<long double, long double>, long double>& a, const pair<pair<long double, long double>, long double>&  b) {
	return (a.second > b.second) || (a.second == b.second && (a.first.first > b.first.first || (a.first.first == a.first.first && a.first.second > a.first.second)));
}

int main()
{
	int T;
	cin >> T;
	vector < pair<pair<long double, long double>, long double> > c;
	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		long double K, N;
		cin >> N >> K;
		while (N--) {
			long double temp1, temp2;
			cin >> temp1 >> temp2;
			c.push_back(make_pair(make_pair(temp1,temp2), (long double) 2.0 * (long double) temp1 * (long double) temp2));
		}
		sort(c.begin(), c.end(), cmp);

		long double sum = 0;
		long double max = c[0].first.first;
		for (int j = 0; j < K; ++j) {
			sum += (long double) c[j].second;
			if (max < c[j].first.first) {
				max = (long double) c[j].first.first;
			}
		}

		pair<pair<long double, long	double>, long double> min = c[K-1];

		pair<long double, long double> lastmax = c[K-1].first;
		for (int j = K-1; j < c.size(); ++j) {
			if (lastmax.first < c[j].first.first || (lastmax.first == c[j].first.first && lastmax.second < c[j].first.second)) {
				lastmax = c[j].first;
			}
		}

		if (lastmax.first > max && ((long double) lastmax.first * (long double) lastmax.first + ((long double) 2.0 * (long double) lastmax.first * (long double) lastmax.second) - ((long double) max * (long double) max)) >= ((long double) min.second)) {
			max = lastmax.first;
			sum -= min.second;
			sum = sum + ((long double) 2.0 * (long double) lastmax.first * (long double) lastmax.second);
		}

		sum += (long double) max * (long double) max;
		sum *= (long double) pi;

		cout << setprecision(6) << fixed << sum << endl;
		c.clear();
	}
	return 0;
}