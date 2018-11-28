#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <cstdio>
#include <set>
#include <cstring>
using namespace std;


char a[102][102];
int s[102][102];
int R, C;

int cnt(int r1, int r2, int c1, int c2) {
	int ans = 0;
	for (int r = r1; r <= r2; ++r )
		for (int c = c1; c <= c2; ++ c)
			ans += (a[r][c]!='?'); 
	return ans;
}

int uni(int r1, int r2, int c1, int c2) {
	for (int r = r1; r <= r2; ++r )
		for (int c = c1; c <= c2; ++ c)
			if (a[r][c]!='?') return a[r][c]; 
	return ' ';
}

void fil(int r1, int r2, int c1, int c2) {
	char ch = uni(r1,r2,c1,c2);
	for (int r = r1; r <= r2; ++r )
		for (int c = c1; c <= c2; ++ c)
			a[r][c] = ch;
}

void aaa(int r1, int r2, int c1, int c2) {
	int n = cnt(r1,r2,c1,c2);
	if (n==1) {
		fil(r1,r2,c1,c2);
		return;
	}
	for (int r = r1; r < r2; ++r ) {
		int m = cnt(r1, r, c1, c2);
		if (m!=0 && m!=n) {
			aaa(r1, r, c1, c2);
			aaa(r+1, r2, c1, c2);
			return;
		}
	}
	for (int c = c1; c < c2; ++c ) {
		int m = cnt(r1, r2, c1, c);
		if (m!=0 && m!=n) {
			aaa(r1, r2, c1, c);
			aaa(r1, r2, c+1, c2);
			return;
		}
	}
}

void solve() {
	cin >> R >> C;
	for (int r = 1; r <= R; ++r)
		for (int c = 1; c <= C; ++c) cin >> a[r][c];
	aaa(1, R, 1, C);
	for (int r = 1; r <= R; ++r) {
		for (int c = 1; c <= C; ++c) cout << a[r][c];
		cout << endl;
	}
}

int main(int argc, char *argv[]) {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int testNum;
	cin >> testNum;
	for (int testid = 0; testid < testNum; ++testid ) {
		cout << "Case #" << testid+1 << ": ";
		cout << endl;
		solve();
		
	}
}