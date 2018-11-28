#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>

#define D(x)

using namespace std;

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& vec) {
	os << "[";
	for (int i = 0; i < vec.size(); i++) {
		if (i > 0) os << ", ";
		os << vec[i];
	}
	os << "]";
	return os;
}

int match(const vector<vector<bool>>& edges, int A, int B) {
	map<int, set<int>> fwd, bkwd;

	for (int i = 0; i < A; i++) {
		for (int j = 0; j < B; j++) {
			if (edges[i][j]) {
				fwd[i].insert(j);
			}
		}
	}

	vector<bool> used1(A), used2(B);
	int flow = 0;

	while (true) {
		vector<bool> visited1(A), visited2(B);
		vector<int> parent1(A, -1), parent2(B, -1);

		vector<int> current, next;
		for (int i = 0; i < A; i++) {
			if (!used1[i]) {
				current.push_back(i);
			}
		}

		int last = -1;

		while (!current.empty()) {
			D(cerr << "forward: " << current << endl);
			for (int v : current) {
				visited1[v] = true;

				for (int v2 : fwd[v]) {
					if (visited2[v2]) continue;
					next.push_back(v2);
					parent2[v2] = v;

					if (!used2[v2]) {
						last = v2;
						break;
					}
				}
			}
			if (last >= 0) break;

			swap(current, next);
			next.clear();

			D(cerr << "backward: " << current << endl);
			for (int v : current) {
				visited2[v] = true;
				for (int v2 : bkwd[v]) {
					if (visited1[v2]) continue;
					next.push_back(v2);
					parent1[v2] = v;
				}
			}

			swap(current, next);
			next.clear();
		}

		if (last >= 0) {
			int v2 = last;
			D(cerr << "  v2 = " << v2 << endl);

			int v = parent2[v2];
			fwd[v].erase(v2);
			bkwd[v2].insert(v);
			used2[v2] = true;
			flow++;
			used1[v] = true;

			while (parent1[v] >= 0) {
				D(cerr << "  v = " << v << endl);

				v2 = parent1[v];
				D(cerr << "  v2 = " << v2 << endl);
				bkwd[v2].erase(v);
				fwd[v].insert(v2);

				int v3 = parent2[v2];
				bkwd[v2].insert(v3);
				fwd[v3].erase(v2);
				used1[v3] = true;

				v = v3;
			}
		} else {
			break;
		}
	}

	return flow;
}


int main() {
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++) {
    	int N, C, M;
    	cin >> N >> C >> M;
		if (C != 2) { cerr << "not small!" << endl; return 1; }

		vector<int> P(M), B(M);
		vector<int> seats1, seats2;
		for (int i = 0; i < M; i++) {
			cin >> P[i] >> B[i];

			if (B[i] == 1) {
				seats1.push_back(P[i]);
			} else {
				seats2.push_back(P[i]);
			}
		}

		int X = seats1.size(), Y = seats2.size();

		vector<vector<bool>> canShare(X, vector<bool>(Y));
		for (int i = 0; i < X; i++) {
			for (int j = 0; j < Y; j++) {
				if (seats1[i] > 1 || seats2[j] > 1) canShare[i][j] = true;
			}
		}

		int maxSharedTrains = match(canShare, X, Y);
		int minTrains = X + Y - maxSharedTrains;

		vector<vector<bool>> canShareNoUpgrade(X, vector<bool>(Y));
		for (int i = 0; i < X; i++) {
			for (int j = 0; j < Y; j++) {
				if (seats1[i] != seats2[j]) canShareNoUpgrade[i][j] = true;
			}
		}
		int maxNoUpgrade = match(canShareNoUpgrade, X, Y);
		int upgrades = maxSharedTrains - maxNoUpgrade;

        cout << "Case #" << testCase << ": " << minTrains << " " << upgrades << endl;
    }
}
