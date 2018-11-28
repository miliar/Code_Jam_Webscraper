// problemA.cpp : Defines the entry point for the console application.
//

#include <iostream> 
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Times {
	int B;
	int E;
	bool IsJ;

	bool operator <(const Times& other) const { return B < other.B; }
};
void main() {
	int t = 0;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		int ac;
		int aj;
		cin >> ac >> aj;
		vector<Times> times;
		for (int j = 0; j < ac; j++) {
			Times tt;
			cin >> tt.B >> tt.E;
			tt.IsJ = false;
			times.push_back(tt);
		}
		for (int j = 0; j < aj; j++) {
			Times tt;
			cin >> tt.B >> tt.E;
			tt.IsJ = true;
			times.push_back(tt);
		}
		sort(times.begin(), times.end());
		int result = 0;
		if (times.size() == 1) {
			result = 2;
		}
		else {
			if (times[0].IsJ == times[1].IsJ) {
				result = (times[1].E - times[0].B <= 720 || times[1].B - times[0].E >= 720) ? 2 : 4;
			}
			else {
				result = 2;
			}
		}
		cout << "Case #" << i << ": " << result << endl;
	}
}