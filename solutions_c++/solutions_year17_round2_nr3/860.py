#include <iostream>
#include <cstdio>
#include <stack>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <set>

#define INF 20000000000000000

using namespace std;

struct edge {
	long long to;
	long long dist;
};
struct horse {
	long long d;
	long long v;
};

struct state {
	int index;
	double time;
	horse ho;
};

int n, q;
horse h[100];
bool used[100];
bool passed[100];

int main() {
	int testCnt;
	cin >> testCnt;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum << ": ";
		vector<edge> g[100];
		cin >> n >> q;
		for (int i = 0; i < n; i++) 
			cin >> h[i].d >> h[i].v;
		for (int i = 0; i < n; i++) {
			used[i] = false;
			for (int j = 0; j < n; j++) {
				edge e;
				cin >> e.dist;
				e.to = j;
				if (e.dist != -1)  {
					g[i].push_back(e);
				}
			}
		}
		double tt[100];
		while (q--) {
			for (int i = 0; i < n; i++) {
				tt[i] = INF;
			}
			int start, end;
			cin >> start >> end;
			start--;
			end--;
			tt[start] = 0;
			for (int i = start; i < end; i++) {
				horse cur = h[i];
				int index = i;
				double curTime = 0;
				while (index < end && cur.d >= g[index][0].dist) {
					cur.d -= g[index][0].dist;
					curTime += g[index][0].dist / (double)cur.v;
					tt[index + 1] = min(tt[index + 1], tt[i] + curTime);
					index++;
				}
			}
			printf("%.9lf\n", tt[end]);
		}
	}
	return 0;
}