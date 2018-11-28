#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
using namespace std;

void fill(vector<string> &cakes, int row, int col) {
    for(int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            if (cakes[i][j] != '?') {
                replace(cakes[i].begin(), cakes[i].begin() + j, '?', cakes[i][j]);
            }
        }
        for (int j = col - 1; j > -1; --j) {
            if (cakes[i][j] != '?') {
                replace(cakes[i].begin() + j, cakes[i].end(), '?', cakes[i][j]);
            }
        }
    }

    for(int i = 0; i < col; ++i) {
        for (int j = 0; j < row - 1; ++j) {
            if (cakes[j][i] != '?' && cakes[j+1][i] == '?') {
                cakes[j+1][i] = cakes[j][i];
            }
        }
        for (int j = row - 1; j > 0; --j) {
            if (cakes[j][i] != '?' && cakes[j-1][i] == '?') {
                cakes[j-1][i] = cakes[j][i];
            }
        }
    }
}

void solve(int case_num) {
    int row = 0, col = 0;
    vector<string> cakes;
    cin >> row >> col;
    for (int i = 0; i < row; ++i) {
        string one_row;
        cin >> one_row;
        cakes.push_back(one_row);
    }
    fill(cakes, row, col);
    cout << "Case #" << case_num << ":" << endl;
    for (auto s : cakes) {
    	cout << s << endl;
    }
}

int main() {
	int n = 0;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        solve(i + 1);
    }
	return 0;
}