#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <utility>
#include <sstream>
#include <queue>
#include <cstdint>
#include <unordered_map>

using namespace std;


void copyRow(vector <string> & mat, int s, int d){
	int n = mat[s].length();
	for (int i = 0; i < n; i++){
		mat[d][i] = mat[s][i];
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++){
		int r, c;
		cin >> r >> c;
		vector<string> mat(r);
		for (int i = 0; i < r; i++){
			cin >> mat[i];
		}
		vector<bool> row(r, false);
		for (int i = 0; i < r; i++){
			char f;
			bool found = false;
			for (int j = 0; j < c && !found; j++){
				if (mat[i][j] != '?'){
					found = true;
					f = mat[i][j];
				}
			}
			if (!found && i>0 && row[i - 1]){
				copyRow(mat, i - 1, i);
				row[i] = true;
			}
			if (found){
				for (int j = 0; j < c; j++){
					if (mat[i][j] == '?'){
						mat[i][j] = f;
					}
					else f = mat[i][j];
				}
				row[i] = true;
			}
		}
		for (int i = r - 1; i >= 0; i--){
			if (!row[i]){
				copyRow(mat, i + 1, i);
			}
		}

		cout << "Case #" << z << ":" << endl;
		for (int i = 0; i < r; i++) cout << mat[i] << endl;

	}
	return 0;
}