#include <bits/stdc++.h>
using namespace std;

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef pair<int, int> ii;

char S[1005];

int main() {
	freopen("/Users/vlwk/Documents/Victor Folder/repo/C++/GCJ 2017/Qualification/A-large.in", "r", stdin);
	freopen("/Users/vlwk/Documents/Victor Folder/repo/C++/GCJ 2017/Qualification/A.out", "w", stdout);
	int T, K;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		scanf("%s %d", S, &K);
		int cnt = 0;
		for (int j = 0; j <= (int)strlen(S) - K; j++) {
			if (S[j] == '-') {
				cnt++;
				for (int k = j; k < j + K; k++) {
					if (S[k] == '-') S[k] = '+';
					else S[k] = '-';
				}
			}
		}
		bool lb = true;
		for (int j = 0; j < (int)strlen(S); j++) {
			if (S[j] == '-') {
				lb = false;
			}
		}
		if (lb) {
			printf("%d\n", cnt);
		} else printf("IMPOSSIBLE\n");
	}
}