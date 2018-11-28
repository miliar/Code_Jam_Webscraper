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
#define INPUT_SITUATION SMALL
#define MAKE_OUTFILE
using namespace std;
typedef long long s64;
typedef unsigned long long u64;
int T,C,R,ans;
char grid[52][52];
bool hpos[52][52], vpos[52][52];
int vnext(int i, int j, int d) {
	do i += d; while (grid[i][j] == '.');
	return i;
}
int hnext(int i, int j, int d) {
	do j += d; while (grid[i][j] == '.');
	return j;
}
bool search_blank(int i, int j) {
	int kr = hnext(i,j,1), kl = hnext(i,j,-1);
	int ku = vnext(i,j,-1), kd = vnext(i,j,1);
	if (grid[i][kr] == '-' && grid[i][kl] == '-') {
		hpos[i][kr] = 0;
		hpos[i][kl] = 0;
	}
	if (grid[ku][j] == '-' && grid[kd][j] == '-') {
		vpos[ku][j] = 0;
		vpos[kd][j] = 0;
	}
	switch(0+hpos[i][kr]+hpos[i][kl]+vpos[ku][j]+vpos[kd][j]) {
		case 0: return true;
		case 1: 
			if (hpos[i][kr]) vpos[i][kr] = 0;
			if (hpos[i][kl]) vpos[i][kl] = 0;
			if (vpos[ku][j]) hpos[ku][j] = 0;
			if (vpos[kd][j]) hpos[kd][j] = 0;
			break;
	}
	return false;
}
bool search_thing(int i, int j) {
	int kr = hnext(i,j,1), kl = hnext(i,j,-1);
	int ku = vnext(i,j,-1), kd = vnext(i,j,1);
	if (grid[i][kr] == '-') {
		hpos[i][kr] = 0;
		hpos[i][j] = 0;
	}
	if (grid[i][kl] == '-') {
		hpos[i][kl] = 0;
		hpos[i][j] = 0;
	}
	if (grid[ku][j] == '-') {
		vpos[ku][j] = 0;
		vpos[i][j] = 0;
	}
	if (grid[kd][j] == '-') {
		vpos[kd][j] = 0;
		vpos[i][j] = 0;
	}
	return !(hpos[i][j]||vpos[i][j]);
}
int main() {
	if (INPUT_SITUATION == TEST) 
		freopen("test_input.txt","r",stdin);
	else if (INPUT_SITUATION == SMALL)
		freopen("C-small.in","r",stdin);
	else if (INPUT_SITUATION == LARGE)
		freopen("C-large.in","r",stdin);
	#ifdef MAKE_OUTFILE
	freopen("output.txt","w",stdout);
	#endif
	cin >> T;
	for (int cas=0; cas<T; cas++) {
		cin >> R >> C;
		for (int i=0; i<R+2; ++i)
			for (int j=0; j<C+2; ++j) {
				hpos[i][j] = 0;
				vpos[i][j] = 0;
			}
			
		for (int j=0; j<C+2; ++j)
			grid[0][j] = '#';
		for (int i=1; i<=R; ++i) {
			grid[i][0] = '#';
			for (int j=1; j<=C; ++j) {
				cin >> grid[i][j];
				if (grid[i][j] == '|')
					grid[i][j] = '-';
				if (grid[i][j] == '-') {
					hpos[i][j] = 1;
					vpos[i][j] = 1;
				}
			}
			grid[i][C+1] = '#';
		}
		bool bad = false;
		for (int j=0; j<C+2; ++j)
			grid[R+1][j] = '#';
		for (int i=0; i<R*C+1; ++i) {
			for (int j=1; j<=R; ++j) {
				for (int k=1; k<=C; ++k) {
					if (grid[j][k] == '-')
						bad |= search_thing(j,k);
					else if (grid[j][k] == '.')
						bad |= search_blank(j,k);
				}
			}
			for (int j=1; j<=R; ++j) {
				for (int k=1; k<=C; ++k) {
					if ((grid[j][k] == '-') && !(hpos[j][k] || vpos[j][k])) {
						bad = true;
					}
				}
			}
		}	
	/*	if (!bad) {
			int count = 0;
			for (int j=1; j<=R; ++j) {
				for (int k=1; k<=C; ++k) {
					if (hpos[j][k] && vpos[j][k])
						++count;
				}
			}
			cout << count << '\n';
		} */
		cout << "Case #" << cas+1 << ": ";
		if (bad) {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		cout << "POSSIBLE\n";
		for (int i=1; i<=R; ++i) {
			for (int j=1; j<=C; ++j) {
				if (grid[i][j] == '-' && (!hpos[i][j]))
					grid[i][j] = '|';
				cout << grid[i][j];
			}
			cout << '\n';
		}
	}
	return 0;
}
