#include<bits/stdc++.h>
using namespace std;

#define R first
#define H second

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;

	for (int t=1; t<=T; ++t) {

		cout << "Case #" << t << ": ";

		int N, K;
		cin >> N >> K;

		vector< pair<double, double> > cake(N);

		for (int i=0; i<N; ++i) {
			cin >> cake[i].R >> cake[i].H;
		}

		sort(cake.begin(), cake.end());

		vector<double> area;

		for (int i=0; i<K-1; ++i) {
			area.push_back(cake[i].R * cake[i].H);
		}

		double ans = 0;

		for (int i=K-1; i<N; ++i) {
			
			sort(area.begin(), area.end());
			reverse(area.begin(), area.end());

			double sum = 0;
			for (int j=0; j<K-1; ++j) {
				sum += area[j];
			}

			area.push_back(cake[i].R * cake[i].H);

			sum += cake[i].R * cake[i].H;

			ans = max(ans, 2*sum + cake[i].R*cake[i].R);
		}

		printf("%.9f\n", M_PI * ans);
	}

	return 0;
}