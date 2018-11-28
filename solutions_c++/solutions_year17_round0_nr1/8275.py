#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

string s;
bool val[1005];
int T, K;

int main() {
	scanf("%d", &T);
	for (int it = 1; it <= T; it++) {
		cin >> s >> K;
		for (int i = 0; i < s.size(); i++) {
			val[i] = (s[i] == '+');
		}
		int cnt = 0;
		for (int i = 0; i + K - 1 < s.size(); i++) if (!val[i]) {
			cnt++;
			for (int j = 0; j < K; j++) {
				val[i + j] ^= 1;
			}
		}
		for (int i = 0; i < s.size(); i++) {
			if (!val[i]) {
				cnt = -1;
			}
		}
		printf("Case #%d: ", it);
		if (cnt < 0) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", cnt);
		}
	}
	return 0;
}