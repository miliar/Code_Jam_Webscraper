#include<cstdio>
#include<cstring>

char a[123];

void solve() {
	int N = strlen(a);
	for(int i=0; i<N; ++i) {
		if(i && a[i] < a[i-1]) {
			if(a[i-1] == '1') {
				for(int j=0; j<N-1; ++j) putchar('9');
				puts("");
			} else {
				int k = i-1;
				while(k && a[k]==a[k-1]) --k;
				for(int j=0; j<k; ++j) putchar(a[j]);
				putchar(a[k] - 1);
				for(int j=k+1; j<N; ++j) putchar('9');
				puts("");
			}
			return;
		}
	}
	
	puts(a);
}

int main() {
	#ifdef LOCAL
		freopen("inB", "r", stdin);
		freopen("outB", "w", stdout);
	#endif
	
	int Cases; scanf("%d", &Cases);
	for(int Case=1; Case<=Cases; ++Case) {
		printf("Case #%d: ", Case);
		scanf("%s", a);
		solve();
	}
	
	return 0;
}
