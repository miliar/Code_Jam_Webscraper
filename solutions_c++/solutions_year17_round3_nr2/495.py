#include <cstdio>
#include <algorithm>
#include <utility>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int, int> pii;
typedef pair<pii, bool> evt;

vector<evt> e;
int n, m, a;

void sol() {
	a = 0;
	//memset(dp, -1, sizeof dp);
	e.clear();
	scanf("%d%d", &n, &m);
	for(int i = 0;i < n + m;i++) {
		int st, ed; scanf("%d%d", &st, &ed);
		e.push_back(evt(pii(st, ed), i < n));	
	}
	sort(e.begin(), e.end());
	int offset = e[0].first.first;
	for(int i = 0;i < n + m;i++) e[i].first.first -= offset, e[i].first.second -= offset;
	e.push_back(e[0]);
	e[n + m].first.first += 1440, e[n + m].first.second += 1440;
	//for(auto c: e) printf("%d - %d %d\n", c.first.first, c.first.second, c.second);
	//printf("%d\n", f(0, 720, 720, e[0].second));
	int s[2] = {0};
	priority_queue<int> tr[2];
	for(int i = 0;i < n + m;i++) {
		if(e[i].second == e[i + 1].second) 
			tr[e[i].second].push(-e[i + 1].first.first + e[i].first.second);
		else a++;
		s[e[i].second] += e[i].first.second - e[i].first.first;
	}
	for(int k = 0;k < 2;k++) {
		while(tr[k].size() > 0) {
			int x = -tr[k].top(); tr[k].pop();
			if(x + s[k] <= 720) s[k] += x;
			else a += 2;
		}
	}
	printf("%d\n", a);
}

int main() {
	int t; scanf("%d", &t);
	for(int i = 1;i <= t;i++) {
		printf("Case #%d: ", i);
		sol();
	}
}
