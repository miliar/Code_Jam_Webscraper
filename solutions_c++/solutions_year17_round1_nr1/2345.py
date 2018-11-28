#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct Point {
	Point(int x, int y) {
		this->x = x;
		this->y = y;
	}
	int x, y;
};

void fill(char rectangular[][26], int R, int C, Point seed) {
	// cout << R << " " << C << " " << seed.x << " " << seed.y << endl;
	char ch = rectangular[seed.x][seed.y];
	int left = seed.y, right = seed.y + 1, top = seed.x, bottom = seed.x + 1;

	for (top = seed.x - 1; top >= 0; --top) {
		bool flag = false;
		for (int j = left; j < right; ++j) {
			if (rectangular[top][j] != '?') {
				flag = true;
				break;
			}
		}
		if (flag) {
			break;
		}
	}
	top++;

	for (left = seed.y - 1; left >= 0; --left) {
		bool flag = false;
		for (int i = top; i < bottom; ++i) {
			if (rectangular[i][left] != '?') {
				flag = true;
				break;
			}
		}
		if (flag) {
			break;
		}
	}
	left++;

	for (right = seed.y + 1; right < C; ++right) {
		bool flag = false;
		for (int i = top; i < bottom; ++i) {
			if (rectangular[i][right] != '?') {
				flag = true;
				break;
			}
		}
		if (flag) {
			break;
		}
	}

	for (bottom = seed.x + 1; bottom < R; ++bottom) {
		bool flag = false;
		for (int j = left; j < right; ++j) {
			if (rectangular[bottom][j] != '?') {
				flag = true;
				break;
			}
		}
		if (flag) {
			break;
		}
	}

	// cout << ch << " " << top << " " << bottom << " " << left << " " << right << endl;

	for (int i = top; i < bottom; ++i) {
		for (int j = left; j < right; ++j) {
			rectangular[i][j] = ch;
		}
	}

}

void search(char rectangular[][26], int R, int C) {
	vector<Point> seeds;
	for (int i = 0; i < R; ++i) {
		for (int j = 0; j < C; ++j) {
			if (rectangular[i][j] != '?') {
				seeds.push_back(Point(i, j));
				// cout << i << " " << j << " " << rectangular[i][j] << endl;
			}
		}
	}
	for (vector<Point>::iterator iter = seeds.begin(); iter != seeds.end(); ++iter) {
		fill(rectangular, R, C, *iter);
	}
}

void run(istream &in, ostream &out) {
	int T;
	in >> T;
	char rectangular[26][26];
	for (int i = 0; i < T; ++i) {
		int R, C;
		in >> R >> C;
		string str;
		for (int j = 0; j < R; ++j) {
			in >> str;
			for (int k = 0; k < C; ++k) {
				rectangular[j][k] = str[k];
			}
		}
		search(rectangular, R, C);
		out << "Case #" << (i + 1) << ":" << endl;
		for (int j = 0; j < R; ++j) {
			for (int k = 0; k < C; ++k) {
				out << rectangular[j][k];
			}
			out << endl;
		}
	}
}

int main() {
	// ifstream fin("A-large.in");
	// ofstream fout("A-large.out");
	// run(fin, fout);
	run(cin, cout);
	// string str;
	// cin >> str;
	return 0;
}