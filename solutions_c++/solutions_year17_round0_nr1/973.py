#include<cstdio>
#include<cstring>

const int MAX_N = 1234;
int N, K;
char a[MAX_N];

void flip(char &c) {
	if(c=='+') c = '-'; else c = '+';
}
bool ok() {
	for(int i=0; i<N; ++i) if(a[i] != '+') return false;
	return true;
}

int main() {
	#ifdef LOCAL
		freopen("inA", "r", stdin);
		freopen("outA", "w", stdout);
	#endif
	
	int Cases; scanf("%d", &Cases);
	for(int Case=1; Case<=Cases; ++Case) {
		printf("Case #%d: ", Case);
		scanf("%s%d", a, &K);
		N = strlen(a);
		
		int ans = 0;
		for(int i=0; i<N-K+1; ++i) {
			if(a[i] == '+') continue;
			for(int j=i; j<i+K; ++j) flip(a[j]);
			++ans;
		}
		
		if(ok()) printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	}
	
	return 0;
}
