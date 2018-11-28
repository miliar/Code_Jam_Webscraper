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

int a[102], t[5];

void solve() {
	int n, p;
	scanf("%d %d", &n, &p);

	for (int i = 0; i <= p; i++)
		t[i] = 0;

	for (int i = 0; i < n; i++) {
		scanf("%d", a + i);
		a[i] %= p;
		t[a[i]]++;
	}

	if (p == 2) {
		printf("%d\n", t[0] + (t[1] / 2) + t[1] % 2);
	}
	else if( p == 3 ) {
		int mi = min(t[1], t[2]);
		int ans = t[0] + mi + ((t[1] - mi) / 3) + ((t[2] - mi) / 3);
		 
		
		if (((t[1] - mi) % 3 > 0) || ((t[2] - mi) % 3 > 0)) ++ans;
		
		printf("%d\n", ans);
	}
	else {
		int ans = t[0];
		int mi = min(t[1], t[3]);
		t[1] -= mi;
		t[3] -= mi;

		t[1] += t[3];
		ans += t[2] / 2 + mi;

		if (t[2] % 2 > 0 && t[1] >= 2) {
			t[1] -= 2;
			ans++;
			ans += t[1] / 4;
			if (t[1] % 4 > 0) ++ans;
		}
		else {
			ans += t[1] / 4;
			if (t[2] % 2 > 0 || t[1] % 4 > 0)
				++ans;
		}
		
		printf("%d\n", ans);
	}
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