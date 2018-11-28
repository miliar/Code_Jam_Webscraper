#include<cstring>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

long long n, k;
vector<pair <long long, long long >> map;

long long solve(long long step) {
	while (step < k) {
		long long max_value = map[0].first;
		long long count = map[0].second;
		long long jump = 1;
		if (step == k - 1) return max_value;
		if (step + count < k) jump = count;
		else jump = k - 1 - step;
		if (count >= 1) count = count - jump;
		if (count == 0) map.erase(map.begin());
		
		if (max_value % 2 == 1) {
			bool exist = false;
			for (int i = 0; i < map.size(); i++) {
				if (map[i].first == (max_value - 1) / 2) {
					map[i].second += 2 * jump;
					exist = true;
				}
			}
			if (!exist) {
				map.push_back(make_pair((max_value - 1) / 2, 2 * jump));
			}
		}
		else {
			bool firstexist = false;
			bool secondexist = false;
			for (int i = 0; i < map.size(); i++) {
				if (map[i].first == (max_value) / 2) {
					map[i].second += jump;
					firstexist = true;
				}else if (map[i].first == (max_value) / 2 - 1) {
					map[i].second += jump;
					secondexist = true;
				}
			}
			if (!firstexist) {
				map.push_back(make_pair((max_value) / 2, jump));
			}
			if (!secondexist) {
				map.push_back(make_pair((max_value) / 2 - 1, jump));
			}

		}
		step += jump;
	}
}

int main() {
	int cases;
	cin >> cases;
	for (int cc = 1; cc <= cases; ++cc) {
		vector<pair <long long, long long >> empty;
		swap(map, empty);
		cin >> n >> k;
		map.push_back(make_pair(n, 1));
		long long sol = solve(0);

		if (sol % 2 == 1)
			cout << "Case #" << cc << ": " << (sol - 1) / 2 << " " << (sol - 1) / 2 << endl;
		else
			cout << "Case #" << cc << ": " << sol / 2 << " " << sol / 2 - 1 << endl;
	}
	system("PAUSE");
	return 0;
}

