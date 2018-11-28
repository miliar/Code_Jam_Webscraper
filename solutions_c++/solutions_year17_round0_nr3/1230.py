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

LL n, k;

void init() {
	
}

void solve() {
	scanf("%lld%lld", &n, &k);
	
	map<LL, LL> cnt;
	priority_queue<LL> q;
	
	q.push(n);
	cnt[n] = 1;
	
	while (!q.empty()) {
		LL T = q.top(); q.pop();
		LL num = cnt[T];
		
		T--;
		
		if (k > num) {
			k -= num;
			LL tox = T / 2;
			LL toy = T - tox;
			if (cnt[tox] == 0) 
				q.push(tox);
			cnt[tox] += num;
			
			if (cnt[toy] == 0)
				q.push(toy);			
			cnt[toy] += num;
		} else {
			fprintf(OUT, "%lld %lld", T - T / 2, T / 2);
			return;
		}
	}
	
}

int main () {
	
	scanf("%d", &TC);
	
	OUT = fopen("c.out", "w");
	
	FOE(ttc, 1, TC) {
		
		printf("Processing on Case #%d...\n", ttc);
		
		init();
		
		fprintf(OUT, "Case #%d: ", ttc);
		
		solve();
		
		fprintf(OUT, "\n");
		
	}
	
	return 0;
	
}
