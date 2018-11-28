#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <utility>
#include <iomanip>
#include <map>
#include <string>
#define INF 1000000000
#define HAND_TYPE 1
#define TEST 10
#define SMALL 100
#define LARGE 1000
#define INPUT_SITUATION LARGE
#define MAKE_OUTFILE
using namespace std;
typedef long long s64;
typedef unsigned long long u64;
int T,ans;
char grid[25][25];
int R,C;
int main() {
	if (INPUT_SITUATION == TEST) 
		freopen("test_input.txt","r",stdin);
	else if (INPUT_SITUATION == SMALL)
		freopen("A-small.in","r",stdin);
	else if (INPUT_SITUATION == LARGE)
		freopen("A-large.in","r",stdin);
	#ifdef MAKE_OUTFILE
	freopen("output.txt","w",stdout);
	#endif
	cin >> T;
	bool empty;
	int first, firstRow;
	for (int cas=0; cas<T; cas++) {
		cin >> R >> C;
		for (int i=0; i<R; ++i) {
			for (int j=0; j<C; ++j) {
				cin >> grid[i][j];
			}
		}
		firstRow = -1;
		for (int i=0; i<R; ++i) {
			empty = true;
			for (int j=0; j<C; ++j) {
				if (grid[i][j] != '?') {
					first = j;
					empty = false;
					break;
				}
			}
			if (empty) {
				continue;
			} else if (firstRow == -1) {
				firstRow = i;
			}
			for (int j=0; j<first; ++j) {
				grid[i][j] = grid[i][first];
			}
			for (int j=first+1; j<C; ++j) {
				if (grid[i][j] == '?') {
					grid[i][j] = grid[i][first];
					continue;
				}
				if (grid[i][j] != grid[i][j-1]) {
					first = j;
				}
			}
		}
		for (int i=0; i<firstRow; i++) {
			for (int j=0; j<C; j++) {
				grid[i][j] = grid[firstRow][j];
			}
		}
		for (int i=firstRow+1; i<R; i++) {
			if (grid[i][0] != '?') continue;
			for (int j=0; j<C; j++) {
				grid[i][j] = grid[i-1][j];
			}
		}
		cout << "Case #" << cas+1 << ":\n";
		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
				cout << grid[i][j];
			}
			cout << '\n';
		}
	}
	return 0;
}
