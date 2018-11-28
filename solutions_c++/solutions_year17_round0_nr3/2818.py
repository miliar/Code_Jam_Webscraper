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

int test;
LL l, r, n, m, na, nb;

void solve(int test) {
	scanf("%I64d%I64d", &n, &m);
	int p = 0;
	LL cnt = 0, a = 1, b = 0;
	while (cnt + (1LL << p) < m) {
		if (n % 2 == 0) {
			n = n/2 - 1;
			na = a;
			nb = a + b + b;
		}
		else {
			n = (n - 1)/2;
			na = a + a + b;
			nb = b;
		}
		a = na;
		b = nb;
		cnt += (1LL << p);
		p++;
	}
	
	if (m - cnt <= b) {
		if ((n + 1) % 2 == 0) l = (n + 1)/2, r = n - (n + 1)/2;
		else l = r = (n+1)/2;
	}
	else {
		if (n % 2 == 0) l = n/2, r = n - n/2 - 1;
		else l = r = n / 2;
	}
	
	printf("Case #%d: %I64d %I64d\n", test, l, r);
	
}

int main(){
	scanf("%d", &test);
	FOR(i, 0, test) solve(i + 1);
	return 0;
}
