#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<map>
#include<set>
#include<cmath>
#include<cassert>
#include<queue>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;

double P[55];

void solve() {
	int N, K;
	cin >> N >> K;
	double U;
	cin >> U;
	for (int i = 0; i < N; i++)
		cin >> P[i];
	double low = 0, high = 1;
	for (int i = 0; i < 100; i++) {
		const double med = (low+high)/2;
		double sum = 0;
		for (int j = 0; j < N; j++) {
			double tmp = max(0., med-P[j]);
			sum += tmp;
		}
		if (sum < U) low = med;
		else high = med;
	}
	double ans = 1;
	for (int i = 0; i < N; i++) {
		ans *= max((low+high)/2, P[i]);
	}
	printf("%.10lf\n", ans);
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		solve();
	}
	return 0;
}
