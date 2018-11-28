#include <stdio.h>
#include <functional>
#include <vector>
#include <algorithm>
#include <string.h>
#include <assert.h>
#include <limits.h>
#include <queue>
#include <string>
#include <iostream>
#include <cmath>

using namespace std;
typedef long long ll;


struct intervals {
	int from, to, type;
	bool operator< (const struct intervals &other) {
		if (from == other.from) {
			return to < other.to;
		}
		else {
			return from < other.from;
		}
	}
};
int prvIdx(int idx, int N) {
	idx--;
	if (idx < 0) idx += N;
	return idx;
}
int getDiff(int src, int dst) {
	int ans = dst - src;
	if (ans < 0) ans += 1440;
	return ans;
}
int getChanges(const vector<intervals> &T) {
	int res = 0;
	for (int i = 0; i < T.size(); i++) {
		if (T[prvIdx(i, T.size())].type != T[i].type) {
			res++;
		}
	}
	return res;
}
int solve() {
	vector<int> AtoA, BtoB; vector<intervals> T;
	int N, M; scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		int from, to; scanf("%d %d", &from, &to);

		T.push_back({ from, to, 0 });
	}
	for (int i = 0; i < M; i++) {
		int from, to; scanf("%d %d", &from, &to);

		T.push_back({ from, to, 1 });
	}

	sort(T.begin(), T.end());
	int changes = getChanges(T);
	int A_total = 0, B_total = 0, interA = 0, interB = 0;

	int prvType = -1;
	vector<int> changingPeriods; int changingSum = 0;
	for (int i = 0; i < N + M; i++) {
		if (T[i].type == 0) {
			A_total += T[i].to - T[i].from;
		}
		else {
			B_total += T[i].to - T[i].from;
		}
		int diff = getDiff(T[prvIdx(i, N+M)].to, T[i].from);
		if (T[prvIdx(i, N+M)].type == T[i].type) {
			if (T[i].type == 0) {
				interA += diff;
				AtoA.push_back(diff);
			}
			else {
				interB += diff;
				BtoB.push_back(diff);
			}
		}
		else {
			changingPeriods.push_back(diff);
			changingSum += diff;
		}
	}
	sort(changingPeriods.begin(), changingPeriods.end());
	sort(AtoA.begin(), AtoA.end());
	sort(BtoB.begin(), BtoB.end());
	int expectedA = A_total + interA, expectedB = B_total + interB;

	if (expectedA + changingSum >= 720 && expectedB + changingSum >= 720) {
		return changes;
	}
	if (expectedA + changingSum < 720) {
		int sum = 0;
		for (int j = BtoB.size() - 1; j >= 0; j--) {
			sum += BtoB[j];
			if (sum + expectedA + changingSum >= 720) {
				return changes + 2* (BtoB.size() - j);
			}
		}
	}
	else {
		int sum = 0;
		for (int j = AtoA.size() - 1; j >= 0; j--) {
			sum += AtoA[j];
			if (sum + expectedB + changingSum >= 720) {
				return changes + 2 * (AtoA.size() - j);
			}
		}
	}
	return -1;
}

int main(void) {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T; scanf("%d\n", &T);
	
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		

		printf("%d\n", solve());
	}

}