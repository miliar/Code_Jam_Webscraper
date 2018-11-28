#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <set>

#define LL long long int
#define FOR(i, s, e) for (int i=(s); i<(e); i++)
#define FOE(i, s, e) for (int i=(s); i<=(e); i++)
#define FOD(i, s, e) for (int i=(s)-1; i>=(e); i--)
#define CLR(x, a) memset(x, a, sizeof(x))

using namespace std;

int test, d[20], siz;
LL n, pw[20];

void digit(LL x, int d[], int *siz) {
	*siz = 0;
	while (x) {
		d[*siz] = x % 10;
		x /= 10;
		(*siz)++;
	}
}

int check(int d[], int siz) {
	FOR(i, 0, siz - 1)
		if (d[i] < d[i + 1]) return 1;
	return 0;
}

void solve(int test) {
	scanf("%I64d", &n);
	pw[0] = 1LL;
	FOR(i, 1, 18) pw[i] = pw[i - 1] * (10LL);
	
	int p = 0;
	
	do {
		digit(n, d, &siz);
		//FOD(i, siz, 0) printf("%d", d[i]);
		//printf("\n");
		if (check(d, siz) == 0) break;
		n = n - (1 + d[p]) * pw[p];
		p++;
	} while (1);
	printf("Case #%d: %I64d\n", test, n); 
}

int main(){
	scanf("%d", &test);
	FOR(i, 0, test) solve(i + 1);
	return 0;
}
