#include <bits/stdc++.h>

using namespace std;

priority_queue<int> mq;
int t, st, n;

int main() {
	freopen ("inn","r",stdin);
	freopen ("myfile.txt","w",stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%d%d", &st, &n);
		while (!mq.empty()) {
			mq.pop();
		}
		mq.push(st);
		n--;
		while (n--) {
			if (mq.top() % 2 == 0) {
				mq.push(mq.top() / 2);
				mq.push((mq.top() / 2) - 1);
			} else {
				mq.push(mq.top() / 2);
				mq.push((mq.top() / 2));
			}
			mq.pop();
		}
		if (mq.top() % 2 == 0)
			printf("Case #%d: %d %d\n", i, mq.top() / 2, mq.top() / 2 - 1);
		else
			printf("Case #%d: %d %d\n", i, mq.top() / 2, mq.top() / 2);
	}

	return 0;
}
