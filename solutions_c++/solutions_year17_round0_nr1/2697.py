#include <bits/stdc++.h>

#define FOR(i, start, end) for (int i = start; i < end; ++i)
#define RFOR(i, start, end) for (int i = end - 1; i >= start; --i)

using namespace std;

typedef long long ll;

int T, K;
string S;

void flip(int start) {
	FOR(i, 0, K) {
		S[start + i] = S[start + i] == '+' ? '-' : '+';
	}
}

bool finished() {
	FOR(i, 0, S.size()) {
		if (S[i] == '-') return false;
	}
	return true;
}

int main()
{
	// freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("qr_a.out", "w", stdout);
	scanf("%d", &T);
	FOR(t, 1, T + 1) {
		cin >> S;
		scanf("%d", &K);
		int l = S.size() - K + 1;
		int count = 0;
		FOR(i, 0, l) {
			if (S[i] == '-') {
				flip(i);
				count++;
			}
		}
		
		printf("Case #%d: ", t);
		if (finished()) printf("%d", count);
		else printf("IMPOSSIBLE");
		printf("\n");
	}
	return 0;
}
