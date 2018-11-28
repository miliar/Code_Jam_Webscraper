#include<bits/stdc++.h>
using namespace std;
#define FOR(i,s,e) for (int i=s;i<e;i++)
#define FOE(i,s,e) for (int i=s;i<=e;i++)
#define FOD(i,s,e) for (int i=s;i>=e;i--)
#define SET(a,e) memset(a,e,sizeof(a))
#define LL long long
#define LD long double
#define pb push_back
#define x first
#define y second
#define PII pair<int,int>
#define PLI pair<LL,int>
#define PIL pair<int,LL>
#define PLL pair<LL,LL>
#define PDD pair<LD,LD>
#define eps 1e-9
#define HH1 402653189
#define HH2 1610612741

int TC;
FILE *OUT;

LL n;
int m, a[30];

void init() {
	m = 0;
}

void solve() {
	scanf("%lld", &n);
	
	while (n) {
		a[m++] = n % 10;
		n /= 10;
	}
	
	reverse(a, a + m);
	
	a[m] = 10;
	
	FOR(i, 0, m) {
		if (a[i] > a[i + 1]) {
			int j = i;
			while (j > 0 && a[j - 1] == a[i]) j--;
			FOR(k, 0, j) fprintf(OUT, "%d", a[k]);
			if (j != 0 || a[j] != 1) fprintf(OUT, "%d", a[j] - 1);
			FOR(k, j + 1, m) fprintf(OUT, "9");
			return;
		}
	}
	
	FOR(i, 0, m) fprintf(OUT, "%d", a[i]);
}

int main () {
	
	scanf("%d", &TC);
	
	OUT = fopen("b.out", "w");
	
	FOE(ttc, 1, TC) {
		
		printf("Processing on Case #%d...\n", ttc);
		
		init();
		
		fprintf(OUT, "Case #%d: ", ttc);
		
		solve();
		
		fprintf(OUT, "\n");
		
	}
	
	return 0;
	
}
