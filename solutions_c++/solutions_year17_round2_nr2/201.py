#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
using namespace std;

typedef pair <int, int> ii;

const int Maxn = 7;
const int MaxN = 2 + Maxn + Maxn;
const int Inf = 1000000000;

int T;
int n, has[Maxn];
int R[MaxN][MaxN];
int flow[MaxN], par[MaxN];

int getNum(char ch)
{
	if (ch == 'R') return 4;
	if (ch == 'Y') return 2;
	if (ch == 'B') return 1;
	if (ch == 'O') return 6;
	if (ch == 'G') return 3;
	if (ch == 'V') return 5;
}

int getChar(int num)
{
	if (num == 1) return 'B';
	if (num == 2) return 'Y';
	if (num == 3) return 'G';
	if (num == 4) return 'R';
	if (num == 5) return 'V';
	if (num == 6) return 'O';
}

void Set(int a, int b, int cap)
{
	R[a][b] = cap; R[b][a] = 0;
}

int getFlow()
{
	fill(flow, flow + MaxN, 0); flow[0] = Inf;
	priority_queue <ii> Q; Q.push(ii(flow[0], 0));
	while (!Q.empty()) {
		int f = Q.top().first, v = Q.top().second; Q.pop();
		printf("v = %d, f = %d", v, f); cout << endl;
		if (f != flow[v]) continue;
		if (v == MaxN - 1) break;
		for (int i = 0; i < MaxN; i++)
			if (min(f, R[v][i]) > flow[i]) {
				flow[i] = min(f, R[v][i]); par[i] = v;
				Q.push(ii(flow[i], i));
			}
	}
	if (flow[MaxN - 1] == 0) return 0;
	int v = MaxN - 1;
	int res = flow[v];
	cout << "res = " << res << endl;
	while (v) {
		int u = par[v];
		R[u][v] -= res; R[v][u] += res;
		v = u;
	}
	return res;
}

int main()
{
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d %d %d %d %d %d %d", &n, &has[getNum('R')], &has[getNum('O')], &has[getNum('Y')], 
										  &has[getNum('G')], &has[getNum('B')], &has[getNum('V')]);
		printf("Case #%d: ", tc);
		int i = 0;
		while (i < 3 && !(has[1 << i] + has[7 ^ 1 << i] == n && has[1 << i] == has[7 ^ 1 << i])) i++;
		if (i < 3) {
			string s;
			while (has[1 << i]--)
				s += string(1, getChar(1 << i)) + string(1, getChar(7 ^ 1 << i));
			printf("%s\n", s.c_str());
			continue;
		}
		bool ok = true;
		for (int i = 0; i < 3 && ok; i++)
			if (has[7 ^ 1 << i] > 0 && has[1 << i] <= has[7 ^ 1 << i]) ok = false;
			else has[1 << i] -= has[7 ^ 1 << i];
		if (!ok) { printf("IMPOSSIBLE\n"); continue; }
		n = has[1] + has[2] + has[4];
		int cur = 0;
		for (int i = 0; i < 3; i++)
			if (has[1 << i] > has[1 << cur]) cur = i;
		if (has[1 << cur] > n / 2) { printf("IMPOSSIBLE\n"); continue; }
		vector <int> V(n);
		int iter[] = {cur, ((cur == 0)? 1: 0), 3 - cur - ((cur == 0)? 1: 0)};
		int pnt = 0;
		for (int i = 0; i < n; i += 2) {
			while (has[1 << iter[pnt]] == 0) pnt++;
			V[i] = iter[pnt]; has[1 << iter[pnt]]--;
		}
		for (int i = 1; i < n; i += 2) {
			while (has[1 << iter[pnt]] == 0) pnt++;
			V[i] = iter[pnt]; has[1 << iter[pnt]]--;
		}
		string s;
		for (int i = 0; i < n; i++) {
			s += string(1, getChar(1 << V[i]));
			while (has[7 ^ 1 << V[i]] > 0) {
				s += string(1, getChar(7 ^ 1 << V[i])) + string(1, getChar(1 << V[i]));
				has[7 ^ 1 << V[i]]--;
			}
		}
		printf("%s\n", s.c_str());
	}
	return 0;
}