#include <algorithm>
#include <cmath>
#include <functional>
#include <iostream>
#include <unordered_set>
#include <string>
#include <thread>
#include <vector>

using namespace std;

vector<string> result;

void algo(int id, int n, int k, vector<int> r, vector<int> h) {
	result[id] = "Case #" + to_string(id + 1) +  ": ";
	vector<pair<int, int>> cr;
	vector<pair<double, int>> ch;
	for (int i = 0; i < n; i++) {
		cr.push_back({r[i], i});
		ch.push_back({double(r[i]) * double(h[i]), i});
	}
	sort(cr.begin(), cr.end(), greater<pair<int, int>>());
	sort(ch.begin(), ch.end(), greater<pair<double, int>>());
	unordered_set<int> del;
	double s = 0;
	for (int i = 0; i < n - k + 1; i++) {
		auto curr = cr[i];
		del.insert(curr.second);
		int rr = curr.first, hh = h[curr.second];
		double ss = M_PI * double(rr) * double(rr) + 2.0 * M_PI * double(rr) * double(hh);
		int c = 1;
		for (int j = 0; j < n; j++) {
			if (c == k) break;
			int ii = ch[j].second;
			if (del.find(ii) == del.end()) {
				int rt = r[ii], ht = h[ii];
				ss += 2.0 * M_PI * double(rt) * double(ht);

				c++;
			}
		}
		s = max(s, ss);
	}
	result[id] += to_string(s);
}

int main() {
	int t, n, k;
	cin >> t;
	vector<thread> threads(t);
	result = vector<string>(t);
	for (int i = 0; i < t; i++) {
		cin >> n >> k;
		vector<int> r(n), h(n);
		for (int j = 0; j < n; j++) {
			cin >> r[j] >> h[j];
		}
		threads[i] = thread(algo, i, n, k, r, h);
	}
	for (int i = 0; i < t; i++) {
		threads[i].join();
		cout << result[i] << endl;
	}
}
