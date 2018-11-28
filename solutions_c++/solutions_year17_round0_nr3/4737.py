#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
	int T;
	int n, k;
	scanf("%d", &T);
	for (int it = 1; it <= T; ++it) {
		scanf("%d%d", &n, &k);
		priority_queue<int, vector<int> > q;
		q.push(n);
		for (int i = 1; i < k; ++i) {
			int top = q.top();
			q.pop();
			q.push(top / 2);
			if (top & 1) {
				q.push(top / 2);
			} else {
				q.push(top / 2 - 1);
			}
		}
		int top = q.top();
		if (top & 1) printf("Case #%d: %d %d\n", it, top/2, top/2);
		else printf("Case #%d: %d %d\n", it, top/2, (top-1)/2);
	}
}
