#include <stdio.h>  
#include <algorithm>  
#include <assert.h>  
#include <cmath>  
#include <complex>  
#include <deque>  
#include <functional>  
#include <iostream>  
#include <limits.h>  
#include <map>  
#include <math.h>  
#include <queue>  
#include <set>  
#include <stdlib.h>  
#include <string.h>  
#include <string>  
#include <time.h>  
#include <unordered_map>  
#include <unordered_set>  
#include <vector>  

#pragma warning(disable:4996)  
#pragma comment(linker, "/STACK:336777216")  
using namespace std;

#define mp make_pair  
#define Fi first  
#define Se second  
#define pb(x) push_back(x)  
#define szz(x) ((int)(x).size())  
#define rep(i, n) for(int i=0;i<n;i++)  
#define all(x) (x).begin(), (x).end()  
#define ldb ldouble  

typedef tuple<int, int, int> t3;
typedef long long ll;
typedef unsigned long long ull;
typedef double db;
typedef long double ldb;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <ll, int> pli;
typedef pair <db, db> pdd;

int IT_MAX = 1 << 18;
const ll MOD = 1000000007;
const int INF = 0x3f3f3f3f;
const ll LL_INF = 0x3f3f3f3f3f3f3f3f;
const db PI = acos(-1);
const db ERR = 1E-11;

int bc;
char in[105][105];
int ch[105][105];
int rch[10050][2];

vector <int> conn[20050];
vector <int> rconn[20050];
int nch(int x) {
	if (x < 0) return -x + bc;
	else return x;
}
void epush(int x, int y) {
	conn[nch(-x)].push_back(nch(y));
	conn[nch(-y)].push_back(nch(x));
	rconn[nch(x)].push_back(nch(-y));
	rconn[nch(y)].push_back(nch(-x));
}

vector <int> Vs;

int G[20050];
vector <int> glist[20050];
int chk[20050];

bool dchk[20050];
void DFS1(int n) {
	dchk[n] = true;
	for (auto it : conn[n]) if (!dchk[it]) DFS1(it);
	Vs.push_back(n);
}
void DFS2(int n, int g) {
	G[n] = g;
	glist[g].push_back(n);
	for (auto it : rconn[n]) if (G[it] == 0) DFS2(it, g);
}
void DFS3(int);
void DFS4(int);

inline int getrev(int x) {
	if (x > bc) return x - bc;
	else return x + bc;
}
void DFS3(int n) {
	chk[n] = 1;
	if (chk[getrev(n)] != -1) DFS4(getrev(n));
	for (auto it : conn[n]) if (!chk[it]) DFS3(it);
}
void DFS4(int n) {
	chk[n] = -1;
	if (chk[getrev(n)] != 1) DFS3(getrev(n));
	for (auto it : rconn[n]) if (!chk[it]) DFS4(it);
}

void init() {
	memset(in, 0, sizeof(in));
	memset(ch, 0, sizeof(ch));
	memset(rch, 0, sizeof(rch));
	memset(G, 0, sizeof(G));
	memset(dchk, 0, sizeof(dchk));
	memset(chk, 0, sizeof(chk));
	Vs.clear();
	for (int i = 0; i < 20050; i++) {
		conn[i].clear();
		rconn[i].clear();
		glist[i].clear();
	}
}

int P[4][2] = { { 0,1 },{ 1,0 },{ 0,-1 },{ -1,0 } };
void gogo(int x, int y, int d, vector<int>& Vu, int R, int C) {
	bool c = false;
	for (int i = 1; i <= 5100; i++) {
		x += P[d][0];
		y += P[d][1];
		if (x < 0 || x >= R || y < 0 || y >= C || in[x][y] == '#') return;
		if (in[x][y] == '\\') {
			d ^= 1;
			c = !c;
		}
		if (in[x][y] == '/') {
			d ^= 3;
			c = !c;
		}
		if (in[x][y] == '-' || in[x][y] == '|') {
			if (c) Vu.push_back(-ch[x][y]);
			else Vu.push_back(ch[x][y]);
		}
	}
}
int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		init();
		int R, C, i, j, k, l;
		scanf("%d %d", &R, &C);

		bc = 0;
		for (i = 0; i < R; i++) {
			scanf("%s", in[i]);
			for (j = 0; j < C; j++) {
				if (in[i][j] == '|' || in[i][j] == '-') {
					ch[i][j] = ++bc;
					rch[bc][0] = i, rch[bc][1] = j;
				}
			}
		}

		for (i = 0; i < R; i++) {
			for (j = 0; j < C; j++) {
				if (in[i][j] != '-' && in[i][j] != '|' && in[i][j] != '.') continue;
				vector <int> Vu1;
				vector <int> Vu2;
				gogo(i, j, 0, Vu1, R, C);
				gogo(i, j, 2, Vu1, R, C);
				gogo(i, j, 1, Vu2, R, C);
				gogo(i, j, 3, Vu2, R, C);
				if (in[i][j] == '.') {
					if (Vu1.size() != 1 && Vu2.size() != 1) break;
					if (Vu1.size() != 1) epush(-Vu2[0], -Vu2[0]);
					else if (Vu2.size() != 1) epush(Vu1[0], Vu1[0]);
					else epush(Vu1[0], -Vu2[0]);
				}
				else {
					if (Vu1.size() != 0 && Vu2.size() != 0) break;
					if (Vu1.size() != 0) epush(-ch[i][j], -ch[i][j]);
					if (Vu2.size() != 0) epush(ch[i][j], ch[i][j]);
				}
			}
			if (j < C) break;
		}
		if (i < R) {
			printf("Case #%d: IMPOSSIBLE\n", tc);
			continue;
		}

		for (i = 1; i <= 2 * bc; i++) if (!dchk[i]) DFS1(i);
		int gc = 0;
		reverse(all(Vs));
		for (auto it : Vs) if (!G[it]) DFS2(it, ++gc);
		for (i = 1; i <= bc; i++) if (G[i] == G[i + bc]) break;
		if (i <= bc) {
			printf("Case #%d: IMPOSSIBLE\n", tc);
			continue;
		}

		printf("Case #%d: POSSIBLE\n", tc);
		for (auto it : Vs) {
			if (chk[it] != 0) continue;
			DFS4(it);
		}
		for (i = 1; i <= bc; i++) {
			if (chk[i] == 1) in[rch[i][0]][rch[i][1]] = '-';
			else in[rch[i][0]][rch[i][1]] = '|';
		}
		for (i = 0; i < R; i++) {
			printf("%s\n", in[i]);
		}
	}
	return 0;
}