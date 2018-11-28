#include <iostream>
#include <string>
#include <thread>
#include <vector>

using namespace std;

vector<string> result;

void algo(int id, int Ac, int Aj, vector<int> C, vector<int> D, vector<int> J, vector<int> K) {
	result[id] = "Case #" + to_string(id + 1) +  ": ";
	vector<pair<int, int>> time;
	for (int i = 0; i < Ac; i++) {
		time.push_back({C[i], 1});
		time.push_back({D[i], 2});
	}
	for (int i = 0; i < Aj; i++) {
		time.push_back({J[i], 3});
		time.push_back({K[i], 4});
	}
	sort(time.begin(), time.end());
	int tc = 0, tj = 0;
	int n = time.size();
	int c = n / 2;
	for (int i = 0; i < n; i++) {
		if (time[i].second == 1) {
			int start = time[i].first;
			while (i < n - 1 && time[i + 1].second != 3) {
				i++;
				if (time[i].second == 1) c--;
			}
			tc += time[i].first - start;
		}
		if (time[i].second == 3) {
			int start = time[i].first;
			while (i < n - 1 && time[i + 1].second != 1) {
				i++;
				if (time[i].second == 3) c--;
			}
			tj += time[i].first - start;
		}
	}
	if (time[0].second == 1 && time[n - 1].second == 2) {
		tc += 1440 - time[n - 1].first + time[0].first;
		c--;
	}
	if (time[0].second == 3 && time[n - 1].second == 4) {
		tj += 1440 - time[n - 1].first + time[0].first;
		c--;
	}
	if (tc <= 720 && tj <= 720) {
		result[id] += to_string(c);
		return;
	}
	if (tc > 720) {
		vector<int> extra;
		for (int i = 0; i < n - 1; i++) {
			if (time[i].second == 2 && time[i + 1].second == 1) {
				extra.push_back(time[i + 1].first - time[i].first);
			}
		}
		if (time[0].second == 1 && time[n - 1].second == 2) {
			extra.push_back(1440 - time[n - 1].first + time[0].first);
		}
		sort(extra.begin(), extra.end());
		reverse(extra.begin(), extra.end());
		int j = 0;
		while (tc > 720) {
			tc -= extra[j];
			j++;
			c += 2;
		}
	}
	if (tj > 720) {
		vector<int> extra;
		for (int i = 0; i < n - 1; i++) {
			if (time[i].second == 4 && time[i + 1].second == 3) {
				extra.push_back(time[i + 1].first - time[i].first);
			}
		}
		if (time[0].second == 3 && time[n - 1].second == 4) {
			extra.push_back(1440 - time[n - 1].first + time[0].first);
		}
		sort(extra.begin(), extra.end());
		reverse(extra.begin(), extra.end());
		int j = 0;
		while (tj > 720) {
			tj -= extra[j];
			j++;
			c += 2;
		}
	}
	result[id] += to_string(c);
	return;
}

int main() {
	int t, ac, aj;
	cin >> t;
	vector<thread> threads(t);
	result = vector<string>(t);
	for (int i = 0; i < t; i++) {
		cin >> ac >> aj;
		vector<int> c(ac), d(ac), j(aj), k(aj);
		for (int jj = 0; jj < ac; jj++) {
			cin >> c[jj] >> d[jj];
		}
		for (int jj = 0; jj < aj; jj++) {
			cin >> j[jj] >> k[jj];
		}
		threads[i] = thread(algo, i, ac, aj, c, d, j, k);
	}
	for (int i = 0; i < t; i++) {
		threads[i].join();
		cout << result[i] << endl;
	}
}
