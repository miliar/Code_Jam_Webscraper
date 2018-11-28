#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i, x, n) for(int i = x; i < (int)(n); ++i)

char s[1001];

int main(){
	freopen("main.in", "r", stdin);
	freopen("main.out", "w", stdout);
	int t;
	scanf("%d", &t);
	f(tc, 1, t + 1){
		printf("Case #%d: ", tc);
		int x[8] = { 0 }, n;
		scanf("%d%d%d%d%d%d%d", &n, x + 1, x + 3, x + 2, x + 6, x + 4, x + 5);
		pair<int, char> z[3] = { make_pair(x[1], 'R'), make_pair(x[2], 'Y'), make_pair(x[4], 'B') };
		sort(z, z + 3);
		if (z[2].first > n >> 1) { printf("IMPOSSIBLE\n"); continue; }
		int j = 2, i = 0;
		while (j > 0 && z[j].first == 0)--j;
		while (j >= 0){
			s[i] = z[j].second;
			i += 2;
			if (i >= n){
				if (n & 1)i -= n;
				else i -= n - 1;
			}
			--z[j].first;
			while (j >= 0 && z[j].first == 0)--j;
		}
		s[n] = 0;
		printf("%s\n", s);
	}
}