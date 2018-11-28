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

int n, d;
PDD a[1055];
LD ans;

void init() {
}

void solve() {
	scanf("%d%d", &d, &n);
	
	ans = 1e18;
	
	FOR(i, 0, n) scanf("%Lf%Lf", &a[i].x, &a[i].y);
	
	sort(a, a + n);
	reverse(a, a + n);
	
	LD ttod = (d - a[0].x) / a[0].y;
	ans = min(ans, d / ttod);
	
	FOR(i, 1, n) {
		if (a[i].y < a[i - 1].y) {
			LD ttome = (a[i - 1].x - a[i].x) / a[i].y;
			ans = min(ans, a[i - 1].x / ttome);
		}
		ttod = (d - a[i].x) / a[i].y;
		ans = min(ans, d / ttod);
	}
	
	fprintf(OUT, "%.10Lf", ans);
	
}

int main () {
	
	scanf("%d", &TC);
	
	OUT = fopen("a.out", "w");
	
	FOE(ttc, 1, TC) {
		
		printf("Processing on Case #%d...\n", ttc);
		
		init();
		
		fprintf(OUT, "Case #%d: ", ttc);
		
		solve();
		
		fprintf(OUT, "\n");
		
	}
	
	return 0;
	
}
