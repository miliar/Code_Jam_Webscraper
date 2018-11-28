#include <bits/stdc++.h>

using namespace std;
typedef vector<vector<char> > mat;

void print_mat(mat m);
mat solve_A(mat matrix);

int main() {
	int len;
	vector<mat> in;
	
	cin >> len;
	for (int i = 1; i <= len; ++i) {
		int C, R;
		mat inp;
		cin >> C >> R;
		for (int j = 0; j < C; ++j) {
			vector<char> row;
			for (int k = 0; k < R; ++k) {
				char c;
				cin >> c;
				row.push_back(c);
			}
			inp.push_back(row);
		}
		in.push_back(inp);
	}
	
	for (int i = 0; i < len; ++i) {
		if(i != 0)
			cout << endl;
		cout << "Case #" << i + 1<< ":";
		print_mat(solve_A(in[i]));
		// if(i != len - 1)
			// cout << endl;
	}
	
	return 0;
}

void print_mat(mat m) {
	for (int j = 0; j < m.size(); ++j) {
		cout << endl;
		for (int k = 0; k < m[0].size(); ++k) {
			cout << m[j][k];
		}		
	}
}

mat solve_A(mat matrix) {
	mat m = matrix;
	for (int j = 0; j < m.size(); ++j) {
		list<char> letters;
		for (int k = 0; k < m[0].size(); ++k) {
			if(m[j][k] != '?')
				letters.push_back(m[j][k]);
		}
		for (int k = 0; k < m[0].size(); ++k) {
			if(m[j][k] != '?' && m[j][k] != letters.front())
				letters.pop_front();
			if(m[j][k] == '?' || m[j][k] == letters.front()) {
				if(letters.empty()) {
					m[j][k] = '?';
				} else {
					m[j][k] = letters.front();
				}
			}
		}
	}
	for (int j = 1; j < m.size(); ++j) {
		bool flag = false;
		for (int k = 0; k < m[0].size(); ++k) {
			if(m[j][k] != '?') {
				flag = true;
			}
		}
		if(!flag) {
			for (int k = 0; k < m[0].size(); ++k) {
				m[j][k] = m[j-1][k];
			}
		}
	}
	for (int j = m.size()-2; j >= 0 ; --j) {
		bool flag = false;
		for (int k = 0; k < m[0].size(); ++k) {
			if(m[j][k] != '?') {
				flag = true;
			}
		}
		if(!flag) {
			for (int k = 0; k < m[0].size(); ++k) {
				m[j][k] = m[j+1][k];
			}
		}
	}
	return m;
}














