#include <cstdio>
#include <algorithm>
using namespace std;
int main() {
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);
	int t, n, p;
	int left, right;
	bool visited[1000100];
	scanf("%d", &t);
	int i, j, k;
	for(int x = 1;x<=t;++x) {
		scanf("%d %d", &n, &p);
		for(i=1;i<=n;++i)
			visited[i] = false;
		visited[0] = visited[n+1] = true;
		
		for(i=0;i<p;++i) {
			int curInd = 1;
			int curMin = -1;
			int curMax = -1;
			for(j=1;j<=n;++j) {
				if(visited[j])
					continue;
				int cur = 0;
				for(k=j-1;k>=0;--k) {
					if(visited[k])
						break;
					++cur;
				}
				left = cur;
				cur = 0;
				for(k=j+1;j<=n+1;++k) {
					if(visited[k])
						break;
					++cur;
				}
				right = cur;
				if(min(left, right) > curMin) {
					curMin = min(left, right);
					curMax = max(left, right);
					curInd = j;
				} else if(min(left, right) == curMin && max(left, right) > curMax) {
					curMin = min(left, right);
					curMax = max(left, right);
					curInd = j;
				}
			}
			visited[curInd] = true;
			if(i == p-1)
				printf("Case #%d: %d %d\n", x, curMax, curMin);
		}
	}
	return 0;
}
