#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <thread>
#include <vector>

using namespace std;

vector<string> result;

void algo(int id, double d, int n, vector<double> k, vector<double> s) {
	string res = "Case #" + to_string(id + 1) +  ": ";
	int i = 0;
	for (int j = 0; j < n; j++) {
		if ((d - k[j]) / s[j] > (d - k[i]) / s[i]) i = j;
	}
	double km = k[i];
	for (int j = 0; j < n; j++) {
		if (k[j] < k[i]) {
			km = min(km, k[j] + s[j] * (k[i] - k[j]) / (s[j] - s[i]));
		}
	}
	double sp = d / (d - km) * s[i];
	res += to_string(sp);
	result[id] = res;
}

int main() {
	int t, n;
	double d;
	cin >> t;
	vector<thread> threads(t);
	result = vector<string>(t);
	for (int i = 0; i < t; i++) {
		cin >> d >> n;
		vector<double> k(n), s(n);
		for (int j = 0; j < n; j++) {
			cin >> k[j] >> s[j];
		}
		threads[i] = thread(algo, i, d, n, k, s);
	}
	for (int i = 0; i < t; i++) {
		threads[i].join();
		cout << result[i] << endl;
	}
}
