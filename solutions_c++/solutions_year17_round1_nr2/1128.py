#include <cmath>
#include <iostream>
#include <string>
#include <thread>
#include <unordered_map>
#include <vector>
using namespace std;

vector<string> result;

void algo(int id, int n, int p, vector<int> recipe, vector<vector<int>> package) {
	string res = "Case #" + to_string(id + 1) +  ": ";
	unordered_map<int, unordered_map<int, pair<int, int>>> choice;
	int NUM_MAX = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < p; j++) {
			int min = ceil(double(package[i][j]) / (double(recipe[i]) * 1.1));
			int max = floor(double(package[i][j]) / (double(recipe[i]) * 0.9));
			choice[i][j] = {min, max};
			if (max > NUM_MAX) NUM_MAX = max;
		}
	}
	int count = 0;
	for (int k = 1; k <= NUM_MAX; ) {
		vector<int> kit(n);
		bool flag = false;
		for (pair<int, unordered_map<int, pair<int, int>>> choice1 : choice) {
			flag = false;
			int i = choice1.first;
			for (pair<int, pair<int, int>> choice2 : choice1.second) {
				int j = choice2.first;
				int min = choice2.second.first, max = choice2.second.second;
				if (k >= min && k <= max) {
					flag = true;
					kit[i] = j;
					break;
				}
			}
			if (!flag) break;
		}
		if (flag) {
			count++;
			for (int i = 0; i < n; i++) {
				choice[i].erase(kit[i]);
			}
		} else {
			k++;
		}
	}
	res += to_string(count);
	result[id] = res;
}

int main() {
	int t, n, p, x;
	cin >> t;
	vector<thread> threads(t);
	result = vector<string>(t);
	for (int i = 0; i < t; i++) {
		cin >> n >> p;
		vector<int> recipe(n);
		vector<vector<int>> package(n, vector<int>(p));
		for (int j = 0; j < n; j++) {
			cin >> x;
			recipe[j] = x;
		}
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < p; k++) {
				cin >> x;
				package[j][k] = x;
			}
		}
		threads[i] = thread(algo, i, n, p, recipe, package);
	}
	for (int i = 0; i < t; i++) {
		threads[i].join();
		cout << result[i] << endl;
	}
}
