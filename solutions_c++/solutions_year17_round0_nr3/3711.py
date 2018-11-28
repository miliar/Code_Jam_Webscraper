#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <queue>
#include <map>

using namespace std;


map < long long, long long > cnt;
priority_queue < long long > q;
int n, k;


void echo_ans(int c, int testN) {
	if (c % 2 == 0) {
		printf("Case #%d: %d %d\n", testN, c / 2, c / 2 - 1);
	} else {
		printf("Case #%d: %d %d\n", testN, c / 2, c / 2);
	}
}

void produce(int c) {
	if (c % 2 == 0) {
		int a = c / 2;
		int b = c / 2 - 1;

		if (cnt.count(a) == 0) {
			q.push(a);
			cnt[a] = 0;
		}
		cnt[a] += cnt[c];
		if (cnt.count(b) == 0) {
			q.push(b);
			cnt[b] = 0;
		}
		cnt[b] += cnt[c];
	} else {
		int a = c / 2;

		if (cnt.count(a) == 0) {
			q.push(a);
			cnt[a] = 0;
		}
		cnt[a] += 2 * cnt[c];
	}
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int testC;
    cin >> testC;

    for (int testN = 1; testN <= testC; testN++) {
        cin >> n >> k;
		q.push(n);
		cnt[n] = 1;

		while (!q.empty()) {
			int c = q.top();
			q.pop();

			if (cnt[c] >= k) {
				echo_ans(c, testN);
				break;
			} else {
				k -= cnt[c];
			}
			produce(c);
		}

		while (!q.empty()) {
			q.pop();
		}
		cnt.clear();
    }

    return 0;
}