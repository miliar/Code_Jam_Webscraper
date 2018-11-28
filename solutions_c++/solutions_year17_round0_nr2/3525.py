#include <iostream>
#include <string.h>
#include <cstdio>
#include <set>
using namespace std;


char S[1000];
int L;
char A[1000];

int rec(int k, int prev, int was) {
	if (k == L) {
		return 1;
	}
	for (int i = 9; i >= 0; --i) {
		if (k > 0 && prev > i) {
		//	printf("%d\n", i);
			continue;
		}
		char ch = '0' + i;
		if (!was && ch > S[k]) {
			continue;
		} 
		int nwas = was;
		if (ch < S[k]) nwas = 1;
		if (rec(k + 1, i, nwas)) {
			A[k] = ch;
			return 1;
		}
	}
	return 0;
}

void solve(int tst) {	
	cin >> S;
	L = strlen(S);
	A[L] = 0;
	int res = rec(0, 0, 0);
	char *p = A;
	while (*p == '0') ++p;
	printf("Case #%d: %s\n", tst, p);	
}

int main() {
	freopen("input.txt", "r", stdin);
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) {
		solve(i);
	}
	return 0;
}