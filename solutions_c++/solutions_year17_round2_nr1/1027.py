#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <iomanip>

using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;
typedef pair<int, int> PII;


int main() {
	ios::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		cout << "Case #" << tc << ": ";
		int D;
		int n;
		cin >> D >> n;
		double max_time = 0.0;
		for (int i = 0, speed, dist; i < n; ++i) {
			cin >> dist >> speed;
			double cur_time = (D-dist)/(double)speed;
			max_time = max(max_time, cur_time);
		}
		cout << fixed << setprecision(8) << (D/max_time) << '\n';
	}
}