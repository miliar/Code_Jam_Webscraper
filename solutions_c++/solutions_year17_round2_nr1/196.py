#include <bits/stdc++.h>

using namespace std;

long double meetup_x(pair<int, int> a, pair<int, int> b) {
	int dspeed = b.second - a.second;
	int dx = a.first - b.first;
	assert(dspeed > 0);
	assert(dx > 0);

	long double tim = dx / dspeed;
	return a.first + tim * a.second;
}

long double Solve() {
	int d, n;
	cin >> d >> n;

	vector<pair<int, int>> horses(n);
	for(auto &horse : horses) {
		cin >> horse.first >> horse.second;
	}

	sort(horses.begin(), horses.end(), 
		greater<pair<int, int>>());
	
	pair<int, int> last(-1, -1);
	int now = 0, pos = -1;

	for(auto horse : horses) {
		if(last.first == -1 || last.second >= horse.second
			|| meetup_x(last, horse) >= d) {
			last = horse;
			pos = now;
		}
		++now;
	}

	long double t = 1.0 * (d - last.first) / last.second;
	cerr << t << endl;
	cerr << pos << endl;
	return d / t;
}

int main() {
	int t;
	cin >> t;
	cout << fixed << setprecision(20);
	for(int tt = 1; tt <= t; ++tt) {
		cout << "Case #" << tt << ": " << Solve() << endl;
		cerr << "Done case #" << tt << endl;
	}
	return 0;
}