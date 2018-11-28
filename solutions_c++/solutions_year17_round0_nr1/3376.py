#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>

using namespace std;

const int MAXN = 1111;

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;t++) {
		string s;
		int K, N, ans = 0;
		cin >> s >> K;
		N = s.length();
		for (int i=0;i<=N-K;i++) {
			if (s[i] == '-') {
				ans ++;
				for (int j=0;j<K;j++) {
					if (s[i+j] == '-') s[i+j] = '+';
					else s[i+j] = '-';
				}
			}
		}
		for (int i=0;i<N;i++) if (s[i] == '-') ans = -1;
		if (ans == -1) printf("Case #%d: IMPOSSIBLE\n", t);
		else printf("Case #%d: %d\n", t, ans);
	}
}