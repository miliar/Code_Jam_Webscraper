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

int n, red, ora, yel, gre, blu, vio;

void init() {
	
}

void output(int cred, int cyel, int cblu) {
	int sz = cred + cyel + cblu;
	char ans[sz + 1];
	SET(ans, 0);
	
	if (cred > cyel && cred > cblu) {
		int j = 0;
		FOR(i, 0, cred) {
			while (ans[j] != 0) j = (j + 1) % sz;
			ans[j] = 'R';
			j = (j + 2) % sz;
		}
		FOR(i, 0, cyel) {
			while (ans[j] != 0) j = (j + 1) % sz;
			ans[j] = 'Y';
			j = (j + 2) % sz;
		}
		FOR(i, 0, cblu) {
			while (ans[j] != 0) j = (j + 1) % sz;
			ans[j] = 'B';
			j = (j + 2) % sz;
		}
	} else
	if (cyel > cblu) {
		int j = 0;
		FOR(i, 0, cyel) {
			while (ans[j] != 0) j = (j + 1) % sz;
			ans[j] = 'Y';
			j = (j + 2) % sz;
		}
		FOR(i, 0, cblu) {
			while (ans[j] != 0) j = (j + 1) % sz;
			ans[j] = 'B';
			j = (j + 2) % sz;
		}
		FOR(i, 0, cred) {
			while (ans[j] != 0) j = (j + 1) % sz;
			ans[j] = 'R';
			j = (j + 2) % sz;
		}
	} else {
		int j = 0;
		FOR(i, 0, cblu) {
			while (ans[j] != 0) j = (j + 1) % sz;
			ans[j] = 'B';
			j = (j + 2) % sz;
		}
		FOR(i, 0, cred) {
			while (ans[j] != 0) j = (j + 1) % sz;
			ans[j] = 'R';
			j = (j + 2) % sz;
		}
		FOR(i, 0, cyel) {
			while (ans[j] != 0) j = (j + 1) % sz;
			ans[j] = 'Y';
			j = (j + 2) % sz;
		}
	}
	
	FOR(i, 0, sz) {
		fprintf(OUT, "%c", ans[i]);
		if (ans[i] == 'R') {
			if (gre)
				while (gre--) {
					fprintf(OUT, "GR");
				}
		} else
		if (ans[i] == 'Y') {
			if (vio)
				while (vio--) {
					fprintf(OUT, "VY");
				}
		} else
		if (ans[i] == 'B') {
			if (ora)
				while (ora--) {
					fprintf(OUT, "OB");
				}
		}
	}
}

void solve() {
	scanf("%d%d%d%d%d%d%d", &n, &red, &ora, &yel, &gre, &blu, &vio);
	
	if (red == gre && yel == 0 && blu == 0 && vio == 0 && ora == 0) {
		FOR(i, 0, red)
			fprintf(OUT, "RG");
		return;
	} else
	if (yel == vio && red == 0 && blu == 0 && gre == 0 && ora == 0) {
		FOR(i, 0, yel)
			fprintf(OUT, "YV");
		return;
	} else
	if (blu == ora && red == 0 && yel == 0 && gre == 0 && vio == 0) {
		FOR(i, 0, blu)
			fprintf(OUT, "BO");
		return;
	}
	
	if (red + 1 < gre) {
		fprintf(OUT, "IMPOSSIBLE");
		return;
	}
	if (yel + 1 < vio) {
		fprintf(OUT, "IMPOSSIBLE");
		return;
	}
	if (blu + 1 < ora) {
		fprintf(OUT, "IMPOSSIBLE");
		return;
	}
	
	int cred = red - gre;
	int cyel = yel - vio;
	int cblu = blu - ora;
	
	if (cred + cyel >= cblu && cyel + cblu >= cred && cblu + cred >= cyel) {
		output(cred, cyel, cblu);
		return;
	}
	
	fprintf(OUT, "IMPOSSIBLE");
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
