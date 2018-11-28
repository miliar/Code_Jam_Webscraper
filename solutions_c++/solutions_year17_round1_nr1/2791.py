#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

const int MaxN = 100;

int nTests;
int nRows, nCols;
int a[MaxN][MaxN];
bool found;

struct Rect {
	int x1, y1, x2, y2;
	bool exist;
	bool avail;
};
Rect rect[MaxN];

int DX[] = {-1, 1, 0, 0};
int DY[] = {0, 0, -1, 1};

vector<string> words_separation(string line) {
	vector<string> ret;
	ret.clear();
	int i = 0;
	while (i < line.length()) {
		if (line[i] == ' ') {
			++i;
			continue;
		}
		string str = "";
		for (int j = i; j < line.length(); ++j) {
			if (line[j] != ' ') {
				str += line[j];
				i = j;
			} else {
				break;
			}
		}
		++i;
		ret.push_back(str);
	}
	return ret;
}

bool violate(int k, int x1, int y1, int x2, int y2) {
	for (int i = 1; i <= 26; ++i) {
		if ((i != k) && (rect[i].exist)) {
			if (rect[i].x1 > x2) {
				continue;
			}
			if (rect[i].y1 > y2) {
				continue;
			}
			if (rect[i].x2 < x1) {
				continue;
			}
			if (rect[i].y2 < y1) {
				continue;
			}
			return true;
		}
	}
	return false;
}

bool full() {
	for (int i = 0; i < nRows; ++i) {
		for (int j = 0; j < nCols; ++j) {
			bool cover = false;
			for (int v = 1; v <= 26; ++v) {
				if (rect[v].exist) {
					if ((i >= rect[v].x1) && (j >= rect[v].y1) && (i <= rect[v].x2) && (j <= rect[v].y2)) {
						cover = true;
						break;
					}
				}
			}
			if (!cover) {
				return false;
			}
		}
	}
	return true;
}

void Back_Tracking() {
	if (full()) {
		found = true;
		return;
	}
	for (int k = 1; k <= 26; ++k) {
		if ((rect[k].exist) && (rect[k].avail)) {
			int x1 = rect[k].x1;
			int y1 = rect[k].y1;
			int x2 = rect[k].x2;
			int y2 = rect[k].y2;

			if (x1 > 0) {
				if (!violate(k, x1 - 1, y1, x2, y2)) {
					rect[k].x1 = x1 - 1;
					Back_Tracking();
					if (found) {
						return;
					}
					rect[k].x1 = x1;
				}
			}

			if (y1 > 0) {
				if (!violate(k, x1, y1 - 1, x2, y2)) {
					rect[k].y1 = y1 - 1;
					Back_Tracking();
					if (found) {
						return;
					}
					rect[k].y1 = y1;
				}
			}

			if (x2 + 1 < nRows) {
				if (!violate(k, x1, y1, x2 + 1, y2)) {
					rect[k].x2 = x2 + 1;
					Back_Tracking();
					if (found) {
						return;
					}
					rect[k].x2 = x2;
				}
			}

			if (y2 + 1 < nCols) {
				if (!violate(k, x1, y1, x2, y2 + 1)) {
					rect[k].y2 = y2 + 1;
					Back_Tracking();
					if (found) {
						return;
					}
					rect[k].y2 = y2;
				}
			}

			rect[k].avail = false;
			Back_Tracking();
			if (found) {
				return;
			}
			rect[k].avail = true;
		}
	}
}

int main(int argc, char **argv) {
	string line;
	getline(cin, line);
	nTests = atoi(line.c_str());
	for (int test = 1; test <= nTests; ++test) {
		getline(cin, line);
		vector<string> words = words_separation(line);
		nRows = atoi(words[0].c_str());
		nCols = atoi(words[1].c_str());
		for (int i = 1; i <= 26; ++i) {
			rect[i].exist = false;
			rect[i].avail = false;
		}
		for (int i = 0; i < nRows; ++i) {
			getline(cin, line);
			for (int j = 0; j < nCols; ++j) {
				if (line[j] == '?') {
					a[i][j] = 0;
				} else {
					a[i][j] = (int)(line[j] - 'A') + 1;
					int v = a[i][j];
					rect[v].x1 = i;
					rect[v].y1 = j;
					rect[v].x2 = i;
					rect[v].y2 = j;
					rect[v].exist = true;
					rect[v].avail = true;
				}
			}
		}
		found = false;
		Back_Tracking();
		for (int v = 1; v <= 26; ++v) {
			if (rect[v].exist) {
				for (int i = rect[v].x1; i <= rect[v].x2; ++i) {
					for (int j = rect[v].y1; j <= rect[v].y2; ++j) {
						a[i][j] = v;
					}
				}
			}
		}
		cout << "Case #" << test << ":" << endl;
		for (int i = 0; i < nRows; ++i) {
			for (int j = 0; j < nCols; ++j) {
				char ch = (char)((a[i][j] - 1) + 'A');
				cout << ch;
			}
			cout << endl;
		}
	}
	return 0;
}