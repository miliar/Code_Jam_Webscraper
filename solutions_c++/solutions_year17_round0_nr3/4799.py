#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;

int main() {
	int ntc; scanf("%d", &ntc);

	for (int tc = 0; tc < ntc; tc++) {
		int n, k; scanf("%d%d", &n, &k);

		priority_queue<ii> pq;
		pq.push(make_pair(n, 0));

		for (int i = 0; i < k; ++i) {
			ii top = pq.top(); pq.pop();
			int len = top.first;
			int sid = -top.second;

			int mid = sid + (len+1)/2 - 1;
			ii left = make_pair((len-1)/2, -sid);
			ii right = make_pair(len-left.first-1, -(mid+1));

			// printf("top=(%d, %d) mid=%d, l=(%d, %d), r=(%d, %d)\n", top.first, top.second, mid+1, left.first, left.second, right.first, right.second);

			if (i == k-1) { // last person
				int ma = max(left.first, right.first);
				int mi = min(left.first, right.first);
				printf("Case #%d: %d %d\n", tc+1, ma, mi);
				break;
			}

			pq.push(left);
			pq.push(right);
		}
	}

	return 0;	
}