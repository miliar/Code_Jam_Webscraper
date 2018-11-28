#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 1

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = (a); i < (b); i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const int inf = 0x7fffffff;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}

void clear(int i) {

}

int solution(int nTest) {
	int r, c;
	vector<pair<int, pair<int, char> > > v;
	scanf("%d%d", &r, &c);
	gets(buffer);
	For(i, 0, r) {
		For(j, 0, c) {
			char t = getchar();
			if (t != '?') {
				v.pb(mp(i, mp(j, t)));
			}
		}
		gets(buffer);
	}
	v.pb(mp(r, mp(0, '-')));
	sort(all(v));
	//For (i, 0, sz(v)) cerr << v[i].first << " " << v[i].second.first << " " << v[i].second.second << endl;
	int currentRowIndex = 0;
	int previousRow = 0;
	vector<vector<char> > res(r, vector<char>(c, '-'));
	while (currentRowIndex != sz(v) - 1) {
		cerr << currentRowIndex << endl;
		int nextRowIndex = currentRowIndex;
		while (v[nextRowIndex].first == v[currentRowIndex].first) {
			nextRowIndex++;
		}
		int nextRow = v[nextRowIndex].first;
		int currentColumnIndex = currentRowIndex;
		int previousColumn = 0;
		while (currentColumnIndex != nextRowIndex) {
			int nextColumn = v[currentColumnIndex + 1].second.first;
			if (currentColumnIndex + 1 == nextRowIndex) {
				nextColumn = c;
			}
			For (i, previousRow, nextRow) {
				For (j, previousColumn, nextColumn) {
					res[i][j] = v[currentColumnIndex].second.second;
				}
			}
			currentColumnIndex++;
			previousColumn = nextColumn;
		}
		previousRow = nextRow;
		currentRowIndex++;
		//For (i, 0, sz(res)) { For (j, 0, sz(res[i])) cerr << res[i][j]; cerr << endl; }
	}
	puts("");
	For (i, 0, sz(res)) {
		For (j, 0, sz(res[i])) {
			printf("%c", res[i][j]);
		}
		puts("");
	}

	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
