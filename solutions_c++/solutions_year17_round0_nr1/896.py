#include <cstdio>
#include <string>
#include <iostream>
using namespace std;
FILE *fi = freopen("A-large.in", "r", stdin);
FILE *fo = freopen("outAL.txt", "w", stdout);
int test, k, cnt;
string str;
int main() {
	int lev = 0;
	scanf("%d", &test); while (test--) {
		cnt = 0; ++lev;
		cin >> str; cin >> k;
		for (int i = 0; i < str.size(); i++) {
			if (str[i] == '+')continue;
			if (i + k >= (int)str.size() + 1) {
				cnt = -1; break;
			}
			++cnt;
			for (int j = i; j < i + k; j++) {
				str[j] = (str[j] == '+' ? '-' : '+');
			}
		}
		printf("Case #%d: ", lev);
		if (cnt == -1) {
			puts("IMPOSSIBLE");
		}
		else {
			printf("%d\n", cnt);
		}
	}
}