#include<cstdio>
#include<cassert>
#include<cstring>
#include<map>
#include<set>
#include<time.h>
#include<algorithm>
#include<stack>
#include<queue>
#include<utility>
#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include <limits>

using namespace std;

typedef pair <int, int> ii;
typedef pair <long long, long long> ll;
const long long INF = 1e9 + 7;
const long long INF9 = 1e9 + 9;

long long gcd(long long b, long long s) {
	return (s != 0) ? gcd(s, b%s) : b;
}

long long pw(long long a, long long b, long long c) {
	if (b == 0) return 1;
	else if (b == 1) return a%c;
	else {
		long long A = pw(a, b / 2, c);
		A = (A*A) % c;
		if (b & 1) A = (A*a) % c;
		return A;
	}

}

int p[1002], b[1002], t[1002][1002], s[1002];

bool can(int n, int c, int m, int mi, int &ans) {
	for (int i = 1; i <= c; i++)
		if (mi < s[i]) return 0;
	int pro = 0;
	ans = 0;
	for (int i = n; i >= 1; i--) {
		int su = 0;
		for (int j = 1; j <= c; j++)
			 su += t[j][i];
		if (su > mi) {
			pro += su - mi;
			ans += su - mi;
		}
		else {
			int tt = min(mi - su, pro);
			pro -= tt;
		}
	}
	if (pro > 0) return 0;
	return 1;
}

void solve_small() {
	int n, c, m;
	scanf("%d %d %d", &n, &c, &m);

	for (int i = 0; i < m; i++) {
		scanf("%d %d", p + i, b + i);
		t[b[i]][p[i]] ++;
		s[b[i]]++;
	}

	int le = 1, ri = m, re = 2*m, ans = 0;

	while (le <= ri) {
		int mi = (le + ri) / 2;
		int pro = 0;
		if (can(n, c, m, mi, pro)) {
			ri = mi - 1;
			if (mi < re) {
				re = min(re, mi);
				ans = pro;
			}
		}
		else
			le = mi + 1;
	}

	memset(t, 0, sizeof(t));
	memset(s, 0, sizeof(s));
	printf("%d %d\n", re, ans);

}

void solve() {
	solve_small();


}


int main() {
	//	freopen("in.txt", "r", stdin);
	//	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int R = 1; R <= T; R++) {
		printf("Case #%d: ", R);
		solve();
	}

}