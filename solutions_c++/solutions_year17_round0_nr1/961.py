#include <bits/stdc++.h>
#define LL long long
#define INF 0x3f3f3f3f
using namespace std;

template<class T> inline
void read(T& x) {
	int f = 1; x = 0;
	char ch = getchar();
	while (ch < '0' || ch > '9')   {if (ch == '-') f = -1; ch = getchar();}
	while (ch >= '0' && ch <= '9') {x = x * 10 + ch - '0'; ch = getchar();}
	x *= f;
}

/*============ Header Template ============*/

const int N = 1000 + 5;

int n, m;
int a[N];
char s[N];

int main() {
	int T;
	read(T);
	for (int KAS = 1; KAS <= T; KAS++) {
		scanf("%s%d", s + 1, &m); n = strlen(s + 1);
		for (int i = 1; i <= n; i++) a[i] = (s[i] == '+');
		int ans = 0;
		for (int i = 1; i <= n - m + 1; i++) {
			if (!a[i]) {
				ans++;
				for (int j = i; j < i + m && j <= n; j++) a[j] ^= 1;
			}
		}
		int flag = 0;
		for (int i = 1; i <= n; i++) if (!a[i]) flag = 1;
		if (!flag) printf("Case #%d: %d\n", KAS, ans);
		else printf("Case #%d: IMPOSSIBLE\n", KAS);
	}
	return 0;
}