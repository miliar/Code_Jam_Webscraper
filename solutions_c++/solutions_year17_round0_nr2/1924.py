#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

long long b[22], l;

long long d[22][12][3];

long long go(int dep, int prev, bool same) {
	if (dep == l) return 1;
	if (d[dep][prev][same] != -1)
		return d[dep][prev][same];
	long long s = 0;
	if (same) {
		for (int i = prev; i <= b[dep]; i++) {
			if (i < b[dep])
				s += go(dep + 1, i, 0);
			else
				s += go(dep + 1, i, 1);
		}
	}
	else {
		for (int i = prev; i <= 9; i++) 
			s += go(dep + 1, i, 0);
	}
	return d[dep][prev][same] = s;
}

void back(int dep, int prev, bool same) {
	if (dep == l) return;
	
	if (same) {
		for (int i = b[dep]; i >= prev; i--) {
			if (i < b[dep]) {
				if (go(dep + 1, i, 0)) {
					printf("%d", i);
					back(dep + 1, i, 0);
					break;
				}
			}
			else {
				if (go(dep + 1, i, 1)) {
					printf("%d", i);
					back(dep + 1, i, 1);
					break;
				}
			}
		}
	}
	else {
		for (int i = 9; i >= prev; i--)
			if (go(dep + 1, i, 0)) {
				printf("%d", i);
				back(dep + 1, i, 0);
				break;
			}
	}
}

void solve() {
	long long n;
	scanf("%lld", &n);

	l = 0;
	while (n) {
		b[l++] = n % 10;
		n /= 10;
	}
	
	reverse(b, b + l);
	memset(d, -1, sizeof(d));
	long long s = go(0, 1, 1);

	if (s == 0) {
		for (int i = 0; i < l - 1; i++)
			printf("9");
	}
	else
		back(0, 1, 1);
	puts("");



}

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int R=1; R<=T; R++){
		printf("Case #%d: ", R);
		solve();
	}

}