#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <string>
#include  <cstring>
#include <cstdlib>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int test = 1; test<=t; test++) {
		int n, m;
		scanf("%d %d", &n, &m);
		int left1 = 720, left2 = 720;
		vector<pair<pair<int, int>, int> > events;
		for(int i = 0; i<n; i++) {
			int c, d;
			scanf("%d %d", &c, &d);
			left1 -= d-c;
			events.push_back({{c, d}, 1});
		}
		for(int i=0; i<m; i++) {
			int c, d;
			scanf("%d %d", &c, &d);
			left2 -= d-c;
			events.push_back({{c, d}, 2});
		}
		int ans = 0;
		sort(events.begin(), events.end());
		vector<int> difs1, difs2;
		for(int i = 0; i<events.size(); i++) {
			if(events[i].second == events[(i+1)%events.size()].second) {
				int dif = events[(i+1)%events.size()].first.first-events[i].first.second;
				dif += 1440;
				dif %= 1440;
				if(events[i].second == 1) difs1.push_back(dif);
				else difs2.push_back(dif);
				ans += 2;
			} else {
				ans++;
			}
		}
		//printf("ans: %d\n", ans);
		sort(difs1.begin(), difs1.end());
		sort(difs2.begin(), difs2.end());
		for(int i = 0; i<difs1.size(); i++) {
			//printf("-> %d\n", difs1[i]);
			if(left1 >= difs1[i]) {
				left1 -= difs1[i];
				ans-=2;
			}
		}
		for(int i = 0; i<difs2.size(); i++) {
			if(left2 >= difs2[i]) {
				left2 -= difs2[i];
				ans-=2;
			}
		}
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}
