#include <vector>
#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

struct Use {
	vector<int> list;


	inline bool bad() {
		return list.size() == 0;
	}

	inline bool check(Use& u) {
		auto end = u.list.size() - 1;
		auto my_end = list.size() - 1;
		if (u.list[0] <= list[0] && list[0] <= u.list[end]) return true;
		if (u.list[0] <= list[my_end] && list[my_end] <= u.list[end]) return true;
		return false;
	}
	Use(int val, int ing_size) {
		int min_count = val / ing_size;
		while (min_count >= 1) {
			if (min_count * ing_size * 0.9 <= val
				&& val <= min_count * ing_size * 1.1) {
				list.push_back(min_count);
			}
			else break;

			min_count--;
		}

		min_count = val / ing_size + 1;
		while (true) {
			if (min_count * ing_size * 0.9 <= val
				&& val <= min_count * ing_size * 1.1) {
				list.push_back(min_count);
			}
			else break;

			min_count++;
		}

		sort(list.begin(), list.end());
	}

	bool operator< (const Use& u) {
		return list[0] + list[list.size() - 1] < u.list[0] + u.list[u.list.size() - 1];
	}

	Use() {
	}
};

int greedy(vector<vector<Use>>& data, int N, int P) {
	vector<int> selected(N, -1);
	int i = 0;

	int max_selected = 0;
	while (i < data[0].size()) {
		Use top = data[0][i];

		bool failed_top = false;
		vector<int> temp_selected(N, 0);
		for (int j = 1; j < N; j++) {
			bool found = false;
			for (int k = selected[j] + 1; k < data[j].size(); k++) {
				if (data[j][k].check(top)) {
					found = true;
					temp_selected[j] = k;
					break;
				}
			}

			if (!found) {
				failed_top = true;
				break;
			}
		}
		if(!failed_top) {
			selected = temp_selected;
			max_selected++;
		}
		i++;
	}

	return max_selected;
}

int main() {
	ifstream in("B-small-attempt0.in");
	ofstream out("out.txt");

	int T;
	string temp;
	getline(in, temp);
	T = stoi(temp);

	int current = 1;
	while (T) {
		string s;
		getline(in, s);

		int N = stol(s.substr(0, s.find(" ")));
		int P = stol(s.substr(s.find(" ")));

		vector<int> ingrid(N);
		getline(in, s);
		int bef = 0;
		for (int i = 0; i < N; i++) {
			ingrid[i] = stol(s.substr(bef, s.find(" ", bef)));
			bef = s.find(" ", bef + 1) + 1;
		}

		bef = 0;
		vector<vector<int>> Q(N, vector<int>(P));

		for (int i = 0; i < N; i++) {
			getline(in, s);
			for (int j = 0; j < P; j++) {
				Q[i][j] = stol(s.substr(bef, s.find(" ", bef)));
				bef = s.find(" ", bef + 1) + 1;
			}

			bef = 0;
		}

		vector<vector<Use>> data(N, vector<Use>());
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < P; j++) {
				Use u(Q[i][j], ingrid[i]);
				if (!u.bad()) {
					data[i].push_back(u);
				}
			}
		}

		for (int i = 0; i < N; i++) {
			sort(data[i].begin(), data[i].end());
		}

		

		T--;
		out << "Case #" << current << ": " << greedy(data, N, P) << endl;
		current++;
	}
}