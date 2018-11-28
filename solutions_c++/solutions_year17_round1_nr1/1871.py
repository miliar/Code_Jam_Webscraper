#define _CRT_SECURE_NO_DEPRECATE
#include <functional>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <bitset>
#include <queue>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
/*--------------------------------*/
#define pb push_back
#define INT_MIN (1 << 31)
#define INT_MAX ~(1 << 31)
#define LL_MIN -9223372036854775808
#define LL_MAX  9223372036854775807
#define lower(c) char(32 | c)
#define upper(c) char(~32 & c)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define RFOR(i, a, b) for (int i = a; i >= b; i--)
#define FORIT(i, a, b) for (auto i = a; i != b; i++)
#define READ freopen("input.txt", "r", stdin);
#define WRITE freopen("output.txt", "w", stdout);
#define MOD ll(1000000007)
#define PI acos(-1)
/*-------------------------------------------------------------*/
int n, m;
char grid[26][26];


void left(int x, int y, char c){
	if (y < 0 || y >= m || grid[x][y] != '?')return;
	grid[x][y] = c;
	left(x, y - 1, c);
}

void right(int x, int y, char c){
	if (y < 0 || y >= m || grid[x][y] != '?')return;
	grid[x][y] = c;
	right(x, y + 1, c);
}


void up(int x, int y, char c){
	if (x < 0 || x >= n || grid[x][y] != '?')return;
	grid[x][y] = c;
	up(x - 1, y, c);
}

void down(int x, int y, char c){
	if (x < 0 || x >= n || grid[x][y] != '?')return;
	grid[x][y] = c;
	down(x + 1, y, c);
}


int main() {


	int T;
	scanf("%d", &T);
	FOR(t, 1, T){
		scanf("%d %d", &n, &m);

		FOR(i, 0, n - 1)scanf("%s\n", &grid[i]);

		FOR(i, 0, n - 1){
			FOR(j, 0, m - 1){
				if (grid[i][j] != '?'){
					left(i, j - 1, grid[i][j]);
					right(i, j + 1, grid[i][j]);
				}
			}
		}

		FOR(i, 0, n - 1){
			FOR(j, 0, m - 1){
				if (grid[i][j] != '?'){
					up(i - 1, j, grid[i][j]);
					down(i + 1, j, grid[i][j]);
				}
			}
		}

		printf("Case #%d:\n", t);

		FOR(i, 0, n - 1)printf("%s\n", grid[i]);

	}



	return 0;
}