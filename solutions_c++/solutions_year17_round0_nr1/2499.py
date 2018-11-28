#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i, x, n) for (int i = x; i < (int)(n); ++i)

char s[1001];

int main(){
	freopen("main.in", "r", stdin);
	freopen("main.out", "w", stdout);
	int t;
	scanf("%d", &t);
	f(tc, 1, t + 1){
		int k;
		scanf("%s%d", s, &k);
		int an = 0, n = strlen(s);
		f(i, 0, n - k + 1)if (s[i] == '-'){
			++an;
			f(j, i, i + k)if (s[j] == '-')s[j] = '+'; else s[j] = '-';
		}
		bool ok = true;
		f(i, n - k + 1, n)if (s[i] == '-') { ok = false; break; }
		printf("Case #%d: ", tc);
		if (ok)printf("%d\n", an);
		else printf("IMPOSSIBLE\n");
	}
}
