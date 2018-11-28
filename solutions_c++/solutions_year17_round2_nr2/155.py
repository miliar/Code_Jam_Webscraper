#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

char out[2000];

struct node{
	int a;
	int n;
	node(int x = 0, int y = 0) {
		a = x;
		n = y;
	}
};

node mid1[2000], mid2[2000];

int main() {
	int T;
	scanf("%d", &T);
	for(int cc = 1; cc <= T; ++cc) {
		int n;
		scanf("%d", &n);
		int r, o, y, g, b, v, ok = 1;
		scanf("%d%d%d%d%d%d", &r, &o, &y, &g, &b, &v);
		if (b == o && b + o == n) {
			for(int i = 0; i < b; ++i) {
				out[i * 2] = 'B';
				out[i * 2 + 1] = 'O';
			}
			out[n] = '\0';
			printf("Case #%d: %s\n", cc, out);
			continue;
		}
		if (g == r && g + r == n) {
			for(int i = 0; i < g; ++i) {
				out[i * 2] = 'G';
				out[i * 2 + 1] = 'R';
			}
			out[n] = '\0';
			printf("Case #%d: %s\n", cc, out);
			continue;
		}
		if (v == y && v + y == n) {
			for(int i = 0; i < v; ++i) {
				out[i * 2] = 'V';
				out[i * 2 + 1] = 'Y';
			}
			out[n] = '\0';
			printf("Case #%d: %s\n", cc, out);
			continue;
		}
		if (o && o + 1 > b) {
			ok = 0;
		} else {
			b -= o;
		}
		if (g && g + 1 > r) {
			ok = 0;
		} else {
			r -= g;
		}
		if (v && v + 1 > y) {
			ok = 0;
		} else {
			y -= v;
		}
		int up = b + r + y;
		int maxx = (b + r + y) / 2;
		if (b > maxx || r > maxx || y > maxx) ok = 0;
		if (ok == 0) {
			printf("Case #%d: IMPOSSIBLE\n", cc);
		} else {
			int f = 0;
			if (b >= r && b >= y) {
				if (b) mid1[f++] = node(1, o);
				for(int i = 1; i < b; ++i) {
					mid1[f++] = node(1, 0);
				}
				if (r) mid1[f++] = node(2, g);
				for(int i = 1; i < r; ++i){
					mid1[f++] = node(2, 0);
				}
				if (y) mid1[f++] = node(3, v);
				for(int i = 1; i < y; ++i) {
					mid1[f++] = node(3, 0);
				}
			} else if (r >= b && r >= y) {
				if (r) mid1[f++] = node(2, g);
				for(int i = 1; i < r; ++i){
					mid1[f++] = node(2, 0);
				}
				if (b) mid1[f++] = node(1, o);
				for(int i = 1; i < b; ++i) {
					mid1[f++] = node(1, 0);
				}
				if (y) mid1[f++] = node(3, v);
				for(int i = 1; i < y; ++i) {
					mid1[f++] = node(3, 0);
				}
			} else {
				if (y) mid1[f++] = node(3, v);
				for(int i = 1; i < y; ++i) {
					mid1[f++] = node(3, 0);
				}
				if (b) mid1[f++] = node(1, o);
				for(int i = 1; i < b; ++i) {
					mid1[f++] = node(1, 0);
				}
				if (r) mid1[f++] = node(2, g);
				for(int i = 1; i < r; ++i){
					mid1[f++] = node(2, 0);
				}
			}
			f = 0;
			for(int i = 0; i < up; i += 2){
				mid2[i] = mid1[f++];
			}
			for(int i = 1; i < up; i += 2){
				mid2[i] = mid1[f++];
			}
			f = 0;
			for(int i = 0; i < up; ++i) {
				if(mid2[i].a == 1) {
					out[f++] = 'B';
					for(int j = 0; j < mid2[i].n; ++j) {
						out[f++] = 'O';
						out[f++] = 'B';
					}
				}
				if(mid2[i].a == 2) {
					out[f++] = 'R';
					for(int j = 0; j < mid2[i].n; ++j) {
						out[f++] = 'G';
						out[f++] = 'R';
					}
				}
				if(mid2[i].a == 3) {
					out[f++] = 'Y';
					for(int j = 0; j < mid2[i].n; ++j) {
						out[f++] = 'V';
						out[f++] = 'Y';
					}
				}
			}
			out[n] = '\0';
			printf("Case #%d: %s\n", cc, out);
		}
	}
	return 0;
}

