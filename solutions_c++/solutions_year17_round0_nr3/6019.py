#include<cstdio>
#include<queue>
#include<utility>

int n, a, k;
std::priority_queue<std::pair<int, std::pair<int, int>>> q;

int main() {
	freopen("C-small-2-attempt1.in", "r", stdin);
	freopen("C-small-2-attempt1.out", "w", stdout);
	scanf("%d", &n);
	while (n --> 0) {
		int x; 
		scanf("%d %d", &x, &k);
		q.push({x-1, {1, x}});
		while (k --> 1) {
			int x = q.top().first;
			int y = q.top().second.first;
			int z = q.top().second.second;
			q.pop();
			int a = y, b = (y+z)>>1;
			--b;
			q.push({b-a, {a, b}});
			a = b + 2;
			b = z;
			q.push({b-a, {a, b}});
		}
		x = q.top().first;
		printf("Case #%d: %d %d\n", ++a, (x+1)>>1, x>>1);
		q = std::priority_queue<std::pair<int, std::pair<int, int>>>();
	}
}
