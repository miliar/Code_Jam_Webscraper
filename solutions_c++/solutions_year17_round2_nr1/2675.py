#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

double solve() {
	int D, N;
	cin >> D >> N;
	vector<pair<long long, long long>> a;
	a.resize(N);
	for(int i = 0; i < N; i++)
		cin >> a[i].first >> a[i].second;
	sort(a.begin(), a.end());
	double speed = 1e100;
	for(const auto &i: a)
		speed = min(speed, i.second + i.second * i.first / (double)(D - i.first));
	return speed;
}
int main(int argc, char argv[]) {
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++)
		cout << "Case #" << i << ": " << fixed << setprecision(7) << solve() << '\n';
	return 0;
}