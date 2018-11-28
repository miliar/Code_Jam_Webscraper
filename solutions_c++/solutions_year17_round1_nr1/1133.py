#include <iostream>
#include <queue>
#include <string>
#include <thread>
#include <vector>
using namespace std;

vector<vector<string>> result;

void algo(int id, int r, int c, vector<string> cake) {
	vector<string> res = {"Case #" + to_string(id + 1) +  ":"};
	queue<int> row;
	for (int i = 0; i < r; i++) {
		queue<int> col;
		for (int j = 0; j < c; j++) {
			if (cake[i][j] != '?') col.push(j);
		}
		if (!col.empty()) {
			row.push(i);
			for (int j = 0; j < c; j++) {
				if (cake[i][j] == '?') {
					cake[i][j] = cake[i][col.front()];
				} else if (j > col.front()) {
					col.pop();
				}
			}
		}
	}
	for (int i = 0; i < r; i++) {
		if (cake[i] == string(c, '?')) {
			cake[i] = cake[row.front()];
		} else if (i > row.front()) {
			row.pop();
		}
	}
	res.insert(res.end(), cake.begin(), cake.end());
	result[id] = res;
}

int main() {
	int t, r, c;
	cin >> t;
	vector<thread> threads(t);
	result = vector<vector<string>>(t);
	for (int i = 0; i < t; i++) {
		cin >> r >> c;
		vector<string> cake(r);
		for (int j = 0; j < r; j++) {
			cin >> cake[j];
		}
		threads[i] = thread(algo, i, r, c, cake);
	}
	for (int i = 0; i < t; i++) {
		threads[i].join();
		for (string res : result[i]) {
			cout << res << endl;
		}
	}
}
