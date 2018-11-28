#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <cassert>
#include <cmath>

#include <iostream>
#include <fstream>
#include <algorithm>
#include <utility>
#include <string>
#include <iterator>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <array>
#include <map>
#include <set>
#include <deque>
#include <set>
#include <unordered_set>
#include <unordered_map>

//#include<bits/stdtr1c++.h>

#define fi first
#define se second
#define inf 2147483647
#define mod 1000000009

#define mset(a, s) memset(a, s, sizeof(a))
#define forall(i,a,b) for(int i=a;i<b;++i)
#define max(a, b) (a < b ? b : a)
#define min(a, b) (a > b ? b : a)
#define all(a) a.begin(), a.end()
#define len(a) sizeof a/sizeof a[0]

/*/ --remove first * or add / before to enable scan--
#define scan(x) do{while((x=getchar())<0); for(x-='0';(_=getchar())>='0';x=(x<<3)+(x<<1)+_-'0');}while(0);
char _;//*/

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int T;
int n, m;

char grid[101][101];
bool orig[101][101];
map<ii, char> mp;
int drow[101], dcol[101], ddiag[202], drdiag[202];

void printGrid() {
	//for (int i = 0; i < n; ++i) {
	//	for (int j = 0; j < n; ++j) {
	//		cerr << grid[i][j]; 
	//	}
	//	cerr << '\n';
	//}
	//cerr << endl;
}

int main(int argc, const char * argv[])
{
	scanf("%d", &T);

	for (int tc = 0; tc < T; ++tc) {
		scanf("%d%d", &n, &m);

		mset(grid, 0);
		mset(orig, 0);
		mset(drow, 0);
		mset(dcol, 0);
		mset(ddiag, 0);
		mset(drdiag, 0);

		mp.clear();

		int ans = 0;
		
		for (int i = 0; i < m; ++i) {
			char c = ' '; int row, col;
			while (c == ' ' || c == '\n' || c == '\r') c = getchar();
			scanf("%d %d", &row, &col);

			--row;
			--col;

			int diag = row + col;
			int rdiag = row + (n-col-1);

			grid[row][col] = c;
			orig[row][col] = true;

			if (c == 'o') { 
				// temporary measure to convert all initial x to o automatically
/*				if (c == 'x') {
					grid[row][col] = 'o';
					mp[{row, col}] = 'o';
				} */

				drow[row] += 200000;
				dcol[col] += 200000;
				ddiag[diag] += 200000;
				drdiag[rdiag] += 200000;
				ans += 2;
			}
			else if (c == '+') {
				ddiag[diag] += 100000;
				drdiag[rdiag] += 100000;
				++ans;
			}
			else if (c == 'x') {
				drow[row] += 100000;
				dcol[col] += 100000;
				++ans;
			}
	
		}

		// fill top, bottom with + where possible
		int row = 0;
		while (true){
			for (int col = 0; col < n; ++col) {
				int diag = row + col;
				int rdiag = row + (n - col - 1);

				if (grid[row][col] == NULL && !(ddiag[diag]) && !(drdiag[rdiag])) {
					grid[row][col] = '+';
					++ans;
					ddiag[diag] += 1;
					drdiag[rdiag] += 1;
					mp[{ row, col }] = grid[row][col];
				}
			}
			if (row == n - 1) break;
			row = n - 1;
		}

		// fill left, right with + where possible
		int col = 0;
		while (true) {
			for (int row = 0; row < n; ++row) {
				int diag = row + col;
				int rdiag = row + (n - col - 1);

				if (grid[row][col] == NULL && !(ddiag[diag]) && !(drdiag[rdiag])) {
					grid[row][col] = '+';
					++ans;
					ddiag[diag] += 1;
					drdiag[rdiag] += 1;
					mp[{ row, col }] = grid[row][col];
				}
			}
			if (col == n - 1) break;
			col = n - 1;
		}

		// add x where possible
		for (int row = 0; row < n; ++row) {
			for (int col = 0; col < n; ++col) {
				if (grid[row][col] == NULL && !(drow[row]) && !(dcol[col])) {
					grid[row][col] = 'x';
					++ans;

					drow[row] += 1;
					dcol[col] += 1;

					mp[{ row, col }] = grid[row][col];
				}
			}
		}
		printGrid();


		// add o's to top, bottom where most efficient or don't add at all
		row = 0;
		while (true){
			int best = INT_MIN, bestcol = 0;
			for (int col = 0; col < n; ++col) {
				if (grid[row][col] == 'o') continue;
				int value;

				if (grid[row][col] == 'x' || grid[row][col] == '+') {
					if (orig[row][col]) {
						value = 200001;
					}
					else {
						value = 3;
					}
				}
				else value = 2;

				int diag = row + col;
				int rdiag = row + (n - col - 1);

				value -= drow[row] + dcol[col] + ddiag[diag] + drdiag[rdiag];

				if (value > best) {
					best = value;
					bestcol = col;
				}
				
			}

			if (best > 0) {
				int rcdelta = 2;
				int ddelta = 2;

				if (grid[row][bestcol] == '+') {
					if (orig[row][bestcol]) {
						ddelta -= 100000;
					}
					else {
						ddelta = 1;
					}
				}

				if (grid[row][bestcol] == 'x') {
					if (orig[row][bestcol]) {
						rcdelta -= 100000;
					}
					else {
						rcdelta = 1;
					}
				}

				grid[row][bestcol] = 'o';
				mp[{ row, bestcol }] = 'o';

				drow[row] += rcdelta;
				dcol[bestcol] += rcdelta;
				ddiag[row + bestcol] += ddelta;
				drdiag[row + n - bestcol - 1] += ddelta;

				for (int i = 0; i < n; ++i) {
					if (grid[row][i] == 'x') {
						grid[row][i] = NULL;
						mp.erase({ row, i });
						drow[row] -= 1;
						dcol[i] -= 1;
					}

					if (grid[i][bestcol] == 'x') {
						grid[i][bestcol] = NULL;
						mp.erase({ i, bestcol });
						drow[i] -= 1;
						dcol[bestcol] -= 1;
					}

					int nr = row + i, nc = bestcol + i;
					if (nr < n && nc < n && grid[nr][nc] == '+') {
						grid[nr][nc] = NULL;
						mp.erase({ nr, nc });
						ddiag[nr + nc] -= 1;
						drdiag[nr + n - nc - 1] -= 1;
					}

					nr = row - i, nc = bestcol - i;
					if (nr >= 0 && nc >= 0 && grid[nr][nc] == '+') {
						grid[nr][nc] = NULL;
						mp.erase({ nr, nc });
						ddiag[nr + nc] -= 1;
						drdiag[nr + n - nc - 1] -= 1;
					}

					nr = row - i, nc = bestcol + i;
					if (nr >= 0 && nc < n && grid[nr][nc] == '+') {
						grid[nr][nc] = NULL;
						mp.erase({ nr, nc });
						ddiag[nr + nc] -= 1;
						drdiag[nr + n - nc - 1] -= 1;
					}

					nr = row + i, nc = bestcol - i;
					if (nc >= 0 && nr < n && grid[nr][nc] == '+') {
						grid[nr][nc] = NULL;
						mp.erase({ nr, nc });
						ddiag[nr + nc] -= 1;
						drdiag[nr + n - nc - 1] -= 1;
					}
				}

				ans += best;
			} // if best > 0

			if (row == n-1) break;
			row = n-1;
		} // while
		
		// add o's to left, right where most efficient or don't add at all
		col = 0;
		while (true){
			int best = INT_MIN, bestrow = 0;
			for (int row = 0; row < n; ++row) {
				if (grid[row][col] == 'o') continue;
				int value;

				if (grid[row][col] == 'x' || grid[row][col] == '+') value = 3;
				else value = 2;

				int diag = row + col;
				int rdiag = row + (n - col - 1);

				value -= drow[row] + dcol[col] + ddiag[diag] + drdiag[rdiag];

				if (value > best) {
					best = value;
					bestrow = row;
				}
				
			}

			if (best > 0) {
				int rcdelta = 2;
				int ddelta = 2;

				if (grid[bestrow][col] == '+') {
					if (orig[bestrow][col]) {
						ddelta -= 100000;
					}
					else {
						ddelta = 1;
					}
				}

				if (grid[bestrow][col] == 'x') {
					if (orig[bestrow][col]) {
						rcdelta -= 100000;
					}
					else {
						rcdelta = 1;
					}
				}

				grid[bestrow][col] = 'o';
				mp[{ bestrow, col }] = 'o';

				drow[bestrow] += rcdelta;
				dcol[col] += rcdelta;
				ddiag[bestrow + col] += ddelta;
				drdiag[bestrow + n- col - 1] += ddelta;

				for (int i = 0; i < n; ++i) {
					if (grid[bestrow][i] == 'x') {
						grid[bestrow][i] = NULL;
						mp.erase({ bestrow, i });
						drow[bestrow] -= 1;
						dcol[i] -= 1;
					}

					if (grid[i][col] == 'x') {
						grid[i][col] = NULL;
						mp.erase({ i, col });
						drow[i] -= 1;
						dcol[col] -= 1;
					}

					int nr = bestrow + i, nc = col + i;
					if (nr < n && nc < n && grid[nr][nc] == '+') {
						grid[nr][nc] = NULL;
						mp.erase({ nr, nc });
						ddiag[nr + nc] -= 1;
						drdiag[nr + n - nc - 1] -= 1;
					}

					nr = bestrow - i, nc = col - i;
					if (nr >= 0 && nc >= 0 && grid[nr][nc] == '+') {
						grid[nr][nc] = NULL;
						mp.erase({ nr, nc });
						ddiag[nr + nc] -= 1;
						drdiag[nr + n - nc - 1] -= 1;
					}

					nr = bestrow - i, nc = col + i;
					if (nr >= 0 && nc < n && grid[nr][nc] == '+') {
						grid[nr][nc] = NULL;
						mp.erase({ nr, nc });
						ddiag[nr + nc] -= 1;
						drdiag[nr + n - nc - 1] -= 1;
					}

					nr = bestrow + i, nc = col - i;
					if (nc >= 0 && nr < n && grid[nr][nc] == '+') {
						grid[nr][nc] = NULL;
						mp.erase({ nr, nc });
						ddiag[nr + nc] -= 1;
						drdiag[nr + n - nc - 1] -= 1;
					}


				}

				ans += best;
			} // if best

			if (col == n-1) break;
			col = n-1;
		} // while

		printf("Case #%d: %d %d\n", tc + 1, ans, mp.size());
		for (auto x : mp) {
			printf("%c %d %d\n", x.second, x.first.first+1, x.first.second+1);
		}

		printGrid();


	}

	return 0;
}