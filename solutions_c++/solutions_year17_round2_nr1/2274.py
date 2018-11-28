#include <bits/stdc++.h>
using namespace std;

struct Section {
	double start, end;
	int speed;
};

void solve() {
	int d, n;
	cin >> d >> n;
	vector<pair<int, int>> horses(n);
	for(auto &h : horses) {
		cin >> h.first >> h.second;
	}
	sort(horses.begin(), horses.end());
	vector<Section> sections = {{d, d, 0}};
	while(n--) {
		double meet;
		while(horses[n].second <= sections.back().speed || (meet = horses[n].first + horses[n].second * (sections.back().start - horses[n].first) / (horses[n].second - sections.back().speed)) > sections.back().end) {
			sections.pop_back();
		}
		sections.back().start = meet;
		sections.push_back({horses[n].first, meet, horses[n].second});
	}
	double time = 0;
	for(auto &s : sections) {
		if(s.speed) {
			time += (s.end - s.start) / s.speed;
		}
	}
	cout << ' ' << fixed << setprecision(6) << d / time << '\n';
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ':';
		solve();
	}
	return 0;
}
