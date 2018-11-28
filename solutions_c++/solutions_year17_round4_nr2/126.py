#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

int dominantNumber(const vector<int>& v) {
	int candidate = -1, rep = 0;
	for (size_t i = 0; i < v.size(); i++) {
		if (v[i] == candidate) {
			rep++;
		} else {
			rep--;
			if (rep < 0) {
				candidate = v[i];
				rep = 1;
			}
		}
	}
	return candidate;
}

int main() {
	int t;
	cin >> t;
	for (int testCase = 1; testCase <= t; testCase++) {
		int n, c, m;
		int rideCount = 0, promotionCount = 0;
		cin >> n >> c >> m;
		vector<vector<int>> customerTickets(c);
		for (int i = 0; i < m; i++) {
			int p, b;
			cin >> p >> b;
			customerTickets[b - 1].push_back(p - 1);
		}
		for (auto&& v : customerTickets) {
			std::sort(v.begin(), v.end());
		}
		std::sort(customerTickets.begin(), customerTickets.end(), [](const vector<int>& lhs, const vector<int>& rhs) {
			return lhs.size() > rhs.size();
		});
		int a = std::count(customerTickets[0].begin(), customerTickets[0].end(), 0);
		int b = std::count(customerTickets[1].begin(), customerTickets[1].end(), 0);
		rideCount = std::max(a + b, (int)customerTickets[0].size());
		{
			int d1 = dominantNumber(customerTickets[0]);
			int d2 = dominantNumber(customerTickets[1]);
			a = std::count(customerTickets[0].begin(), customerTickets[0].end(), d1);
			b = std::count(customerTickets[1].begin(), customerTickets[1].end(), d1);
			if (a + b > rideCount) {
				promotionCount = a + b - rideCount;
			}
			a = std::count(customerTickets[0].begin(), customerTickets[0].end(), d2);
			b = std::count(customerTickets[1].begin(), customerTickets[1].end(), d2);
			if (a + b > rideCount) {
				promotionCount = a + b - rideCount;
			}
		}
		cout << "Case #" << testCase << ": " << rideCount << ' ' << promotionCount << endl;
	}
    return 0;
}
