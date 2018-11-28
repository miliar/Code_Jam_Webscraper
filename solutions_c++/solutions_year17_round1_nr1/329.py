#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;


vector<vector<char>> board;
vector<vector<int>> sum;

int get(int y, int x) {
	if (y < 0 || x < 0) return 0;
	return sum[y][x];
};


int count(int lowy, int lowx, int highy, int highx) {
	return get(highy, highx)-get(lowy-1,highx)-get(highy,lowx-1)+get(lowy-1,lowx-1);
};

bool check(int lowy, int lowx, int highy, int highx) {
	return (count(lowy,lowx,highy,highx) > 0);
}

void divide(int lowy, int lowx, int highy, int highx) {
	if (lowx == highx && lowy == highy) return;

	if (count(lowy,lowx,highy,highx) == 1) {
		char ch;

		for (int i=lowy; i <= highy; ++i)
			for (int j = lowx; j <= highx; ++j)
				if (board[i][j] != '?') {
					ch = board[i][j];
				};

		for (int i=lowy; i <= highy; ++i)
			for (int j = lowx; j <= highx; ++j)
				board[i][j] = ch;
		return;
	};

	if (lowy != highy) {
		for (int i=lowy; i< highy; ++i) {
			if (check(lowy, lowx, i, highx) && check(i+1, lowx, highy, highx)) {
				divide(lowy, lowx, i, highx);
				divide(i+1, lowx, highy, highx);
				return;
			}
		};
	}

	if (lowx != highx) {
		for (int i=lowx; i < highx; ++i) {
			if (check(lowy, lowx, highy, i) && check(lowy, i+1, highy, highx)) {
				divide(lowy, lowx, highy, i);
				divide(lowy, i+1, highy, highx);
				return;
			};			
		};
	};
};


void solve(int i0) {
	int n, m;
	cin >> n >> m;
	board.resize(n);
	sum.resize(n);
	for (int i = 0; i < n; ++i) {
		board[i].resize(m);
		sum[i].resize(m);
		for (int j = 0 ; j < m; ++j)
			cin >> board[i][j];
	};

	for (int i = 0; i < n; ++i) 
		for (int j = 0; j < m; ++j) {
			int d = (board[i][j] != '?') ? 1 : 0;
			sum[i][j] = get(i-1,j)+get(i,j-1)+d-get(i-1,j-1);
		};

	divide(0,0,n-1,m-1);

	cout << "Case #" << i0 << ":" << endl;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j)
			cout << board[i][j];
		cout <<endl;
	}
};



int main() {
	//freopen("A.in", "r", stdin);
//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);


	int t;
	cin >> t;
	for (int i0=1; i0<=t; ++i0) {
		solve(i0);
	};


}