#include <iostream>
#include <string.h>
#include <cstdio>
#include <set>
#include <vector>
#include <map>
using namespace std;

char S[2000];

void solve(int tst) {	
	int N, R, O, Y, G, B, V;
	cin >> N >> R >> O >> Y >> G >> B >> V;
	for (int i = 0; i <= N; ++i) {
		S[i] = 0;
	}

	pair<int, char> a[3];
	a[0] = make_pair(R, 'R');
	a[1] = make_pair(Y, 'Y');
	a[2] = make_pair(B, 'B');
	sort(a, a + 3);
	reverse(a, a + 3);
	if (a[0].first > a[1].first + a[2].first) {
		printf("Case #%d: IMPOSSIBLE\n", tst);
		return;	
	}
	int cnt0 = a[0].first;
	int cnt1 = a[1].first;
	int cnt2 = a[2].first;
	for (int i = 0; i < cnt0; ++i) {
		S[i * 2] = a[0].second;
	}
	
	for (int j = 0; j < N; j++) {
		if (S[j]) continue;
		if (cnt1 > cnt2) {
			cnt1--;
			S[j] = a[1].second;
		} else {
			break;
		}
	}

	int prev = 2;
	for (int j = 0; j < N; j++) {
		if (S[j]) continue;
		if (prev == 1) {
			S[j] = a[1].second;
		} else {
			S[j] = a[2].second;
		}
		prev = 3 - prev;
	}

	printf("Case #%d: %s\n", tst, S);	
	for (int i = 0; i < N - 1; ++i) {
		if (S[i] == S[i + 1]) {
			printf("qulinxao\n");
			return;
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) {
		solve(i);
	}
	return 0;
}
