#include <stdio.h>
#include <string.h>
#include <deque>
#include <algorithm>
using namespace std;
#define MAX_N 1004
char happy[MAX_N];
deque<int> dq;

int main() {
	int T;
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	setbuf(stdout, NULL);
	for (int t = 1; t <= T; t++) {
		int N, K;
		scanf("%s", happy);
		N = strlen(happy);
		scanf("%d", &K);
		bool isFlip = false;
		int cntFlip = 0;
		dq.clear();
		for (int i = 0; i <= N - K; i++) {
			if (!dq.empty() && dq[0] == i - K) {
				dq.pop_front();
				isFlip = !isFlip;
			}
			if ( (happy[i] == '+' && !isFlip) 
				|| (happy[i] == '-' && isFlip)) {
				// OK
			}
			else {
				cntFlip++;
				isFlip = !isFlip;
				dq.push_back(i);
			}
		}
		bool isOk = true;
		for (int i = N - K + 1; i < N; i++) {
			if (!dq.empty() && dq[0] == i - K) {
				dq.pop_front();
				isFlip = !isFlip;
			}
			if ((happy[i] == '+' && !isFlip)
				|| (happy[i] == '-' && isFlip)) {
				// OK
			}
			else {
				isOk = false;
				break;
			}
		}
		if (isOk) printf("Case #%d: %d\n", t, cntFlip);
		else printf("Case #%d: IMPOSSIBLE\n", t);
	}
}