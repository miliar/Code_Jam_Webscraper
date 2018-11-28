#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;

int RN, CN;
char G[30][30];
int T[30][30];
vector<char> letters;
vector<pair<int, int>> positions;

void updateT() {
	int i, j;
	for(i=1;i<=RN;++i) {
		for(j=1;j<=CN;++j) {
			T[i][j] = (G[i][j] != '?') + T[i-1][j] + T[i][j-1] - T[i-1][j-1];
		}
	}
}

int range_fill(int left, int top, int right, int bottom, char c) {
	int i, j;
	for(i=top;i<=bottom;++i) {
		for(j=left;j<=right;++j) {
			G[i][j] = c;
		}
	}
	updateT();
}

int range_check(int left, int top, int right, int bottom) {
	return T[bottom][right] - T[top-1][right] - T[bottom][left-1] + T[top-1][left-1];
}

void process() {
	int i,sz = letters.size();
	int x, y, top, left, right, bottom;
	for(i=0;i<sz;++i) {
		x = positions[i].first; //VERT
		y = positions[i].second; //HOR
		//cout << "Checking " << letters[i] << " at (" << x << "," << y << ")" << endl;
		left = 1;
		while(left < y && range_check(left, x, y-1, x)) { ++left; }
		right = CN;
		while(right > y && range_check(y+1, x, right, x)) { --right; }
		top = 1;
		while(top < x && range_check(left, top, right, x-1)) { ++top; }
		bottom = RN;
		while(bottom > x && range_check(left, x+1, right, bottom)) { --bottom; }
		//cout << "Filling from " << left << " to " << right << " and from " << top << " to " << bottom << endl;
		range_fill(left, top, right, bottom, letters[i]);
	}
}

int main() {
	int tc, t, i, j;
	char c;
	char isLetter;
	cin >> t;
	for(tc=1; tc <= t; ++tc) {
		cin >> RN >> CN;
		for(i=1;i<=RN;++i) {
			for(j=1;j<=CN;++j) {
				cin >> G[i][j];
				isLetter = (G[i][j] != '?');
				T[i][j] = isLetter + T[i-1][j] + T[i][j-1] - T[i-1][j-1];
				if (isLetter) {
					letters.push_back(G[i][j]);
					positions.push_back(make_pair(i,j));
				}
			}
		}
		
		/*
		for(i=1;i<=RN;++i) {
			for(j=1;j<=CN;++j) {
				cout << G[i][j];
			}
			cout << endl;
		}*/
		
		process();
		
		cout << "Case #" << tc << ": " << endl;
		
		for(i=1;i<=RN;++i) {
			for(j=1;j<=CN;++j) {
				cout << G[i][j];
			}
			cout << endl;
		}
		memset(G, 0, sizeof(G));
		memset(T, 0, sizeof(T));
		letters.clear();
		positions.clear();
	}
	return 0;
}