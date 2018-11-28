#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:167772160000")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
#include <list>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <iomanip>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <sstream>
#include <assert.h>
#include <functional>
#include <climits>
#include <cstring>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
//typedef uint64_t ull;
//typedef std::pair<long double,long double> pdd;
#define for8(i) for( i = 1; i<=8; i++)
#define fori(N)          for(int i = 0; i<(N); i++)
#define forj(N)         for(int j = 0; j<(N); j++)
#define fork(N)         for(int k = 0; k<(N); k++)
#define forl(N)         for(int l = 0; l<(N); l++)
#define ford(N)         for(int d = 0; d<(N); d++)
#define fori1(N)          for(int i = 1; i<=(N); i++)
#define forj1(N)         for(int j = 1; j<=(N); j++)
#define fork1(N)         for(int k = 1; k<=(N); k++)
#define ford1(N)         for(int d = 1; d<=(N); d++)
#define forl1(N)         for(int l = 1; l<=(N); l++)
#define PI (2*asin(1))
#define print(n) printf("%d ", (n))
#define printll(n) printf("%I64d ", (n))
#define printline() printf("\n")
#define read(n) scanf("%d", &n);
#define read2(n, m) scanf("%d%d", &n, &m);
#define readll(n) scanf("%I64d", &n);
#define mp make_pair
template <typename T>
using min_heap = std::priority_queue<T, std::vector<T>, std::greater<T> >;
template <typename T>
using max_heap = std::priority_queue<T, std::vector<T>, std::less<T> >;

char grid[100][100];

set<pii>currentTiles;
bool currentFail;
void src(pii coord, pii dir) {
	char c = grid[coord.first][coord.second];
	if (c == '#')return;
	if (c == '-' || c == '|') {
		currentFail = true;
		return;
	}
	if (c == '.') {
		currentTiles.insert(coord);
	}
	if (c == '/') {
		dir = pii(-dir.second, -dir.first);
	}
	if (c == '\\'){
		dir = pii(dir.second, dir.first);
	}
	src(pii(coord.first + dir.first, coord.second + dir.second), dir);
}
vector<pii>pointingTo[120][120];
pii lasers[120];
int lasersCount;
bool available[120][2];
set<pii> options[120][2];
bool totalFail;
set<int> hasPointed[120][120];

vector<pii>lacking;
int position[120];
bool used[120];
stack<pair<int,pii> >inserts;
bool tryThis(int a, int op) {
	if (used[a])return false;
	vector<pii>prevL = lacking;
	if (!available[a][op])return false;
	used[a] = true;
	position[a] = op;
	inserts.push(mp(a, pii(0,0)));
	for (auto x : options[a][op]) {
		hasPointed[x.first][x.second].insert(a);
		inserts.push(mp(a, x));

	}
	for (auto x : options[a][1 - op]) {
		if (hasPointed[x.first][x.second].empty())
			lacking.push_back(x);
	}
	bool haveFailed = false;
	while(!lacking.empty()) {
		pii x = lacking.back();
		
		lacking.pop_back();
		if (hasPointed[x.first][x.second].size() > 0)continue;
		bool ok = false;
		for (auto cur : pointingTo[x.first][x.second]) {
			if (tryThis(cur.first, cur.second)) {
				ok = true;
				break;
			}
			
		}
		if (!ok) {
			haveFailed = true;
			break;
		}
	}

	if (haveFailed) {
		while (true) {
			pair<int, pii> cur= inserts.top();
			inserts.pop();
			if (cur.second == pii(0, 0))used[cur.first] = false;
			else
				hasPointed[cur.second.first][cur.second.second].erase(cur.first);
			if (cur == mp(a, pii(0, 0)))break;
		}
		lacking = prevL;
		return false;
	}
	else return true;
}

int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
#endif
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//ios::sync_with_stdio(false); cin.tie(0);
	
	int casesNum; cin >> casesNum;
	for (int currentCase = 1; currentCase <= casesNum; currentCase++) {


		totalFail = false;
		lasersCount = 0;
		fori(120)forj(2)options[i][j].clear();
		fori(120)forj(120) {
			hasPointed[i][j].clear();
			pointingTo[i][j].clear();
		}
		lacking.clear();
		while(!inserts.empty())inserts.pop();
		fori(120)used[i] = false;
		printf("Case #%d: ", currentCase);
		int R, C; cin >> R >> C;
		fori(R + 3)forj(C + 3)grid[i][j] = '#';
		fori1(R)forj1(C) {
			cin >> grid[i][j];
			if (grid[i][j] == '-' || grid[i][j] == '|')lasers[lasersCount++] = pii(i, j);
		}
		fori(lasersCount) {
			if (totalFail)break;
			currentTiles.clear();
			currentFail = false;
			int x = lasers[i].first;
			int y = lasers[i].second;
			src(pii(x, y + 1), pii(0, 1));
			src(pii(x, y - 1), pii(0, -1));
			available[i][0] = !currentFail;
			if (!currentFail)options[i][0] = currentTiles;

			currentFail = false;
			currentTiles.clear();
			src(pii(x + 1, y), pii(1, 0));
			src(pii(x - 1, y), pii(-1, 0));
			available[i][1] = !currentFail;
			if (!currentFail)options[i][1] = currentTiles;
			if (!available[i][0] && !available[i][1])totalFail = true;

		}
		fori(120)forj(120)pointingTo[i][j].clear();
		if (totalFail) {
			cout << "IMPOSSIBLE"<<endl;
			continue;
		}
		fori(lasersCount)forj(2) {
			for (auto p : options[i][j]) {
				pointingTo[p.first][p.second].push_back(pii(i, j));
			}
		}
		fori1(R)forj1(C) {
			if (grid[i][j] != '.')continue;
			if (pointingTo[i][j].empty())totalFail = true;
			if (pointingTo[i][j].size() > 2) {
				int asfawgfasdf = 13545;
			}
		}
		if (totalFail) {
			cout << "IMPOSSIBLE"<<endl;
			continue;
		}


		fori(lasersCount) {
			while (!inserts.empty())inserts.pop();
			if (used[i])continue;
			if (tryThis(i, 0))continue;
			while (!inserts.empty())inserts.pop();
			if (!tryThis(i, 1)) {
				totalFail = true;
				break;
			}

		}
		if (totalFail) {
			cout << "IMPOSSIBLE"<<endl;
			continue;
		}
		fori(lasersCount) {
			if (position[i] == 0)
				grid[lasers[i].first][lasers[i].second] = '-';
			else
				grid[lasers[i].first][lasers[i].second] = '|';
		}
		cout << "POSSIBLE" << endl;
		fori1(R) {
			forj1(C)
				cout << grid[i][j];
			cout << endl;
		}
	}
	
	return 0;
}