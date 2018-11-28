#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <cstdint>

using namespace std;

int solve(int n, int p, int r[50], int q[50][50]){
	int kits = 0;
	double serv[50][50];
	double max = -1;
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < p; j++) {
			serv[i][j] = q[i][j] / (double)r[i];
			if(serv[i][j] > max || max == -1) {
				max = serv[i][j];
			}
		}
	}

	int start = (max * 1.1) + 1;

	for(int i = start; i > 0; i--) {
		vector<vector<int>> packs;
		double min = i * 0.9;
		double max = i * 1.1;
		int min_packs = -1;
		for(int j = 0; j < n; j++) {
			vector<int> k_places;
			for(int k = 0; k < p; k++) {
				if(serv[j][k] >= min && serv[j][k] <= max) {
					k_places.push_back(k);
				}
			}
			if(min_packs == -1 || k_places.size() < min_packs) {
				min_packs = k_places.size();
			}
			packs.push_back(k_places);
		}

		for(int j = 0; j < n; j++) {
			vector<int> k_places = packs.at(j);
			for(int k = 0; k < min_packs; k++) {
				serv[j][k_places.at(k)] = 0;
			}
		}

		kits += min_packs;
	}

	return kits;
}

int main() {
	int t, n, p;

	cin >> t;

	for(int i = 0; i < t; i++){
		cin >> n;
		cin >> p;

		int r[50];
		int q[50][50];

		for(int i = 0; i < n; i++) {
			cin >> r[i];
		}

		for(int i = 0; i < n; i++) {
			for(int j = 0; j < p; j++) {
				cin >> q[i][j];
			}
		}
		
		cout << "Case #" << (i + 1) << ": " << solve(n, p, r, q) << endl;
	}

	return EXIT_SUCCESS;
}
