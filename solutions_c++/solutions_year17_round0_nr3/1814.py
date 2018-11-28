#include<cstdio>
typedef long long llt;
int T;
llt N, K, F[64], space, bigCnt, maxLR, minLR, x;

void calcX() {
	F[0] = 1;
	for(int i = 1; i < 64; i++) F[i] = F[i-1] + (1LL << i);
}

int main() {
	//freopen("a.in", "r", stdin);
	scanf("%d", &T);
	calcX();
	for(int t = 1; t <= T; t++) {
		scanf("%lld%lld", &N, &K);
		
		for(x = 0; F[x] < K; x++); 
		x--;
		space = (N - F[x]) / (1LL << (x+1));
		bigCnt = (N - F[x]) % (1LL << (x+1));
		if(K-F[x] <= bigCnt) space++;
		
		minLR = maxLR = (space-1) / 2;
		if((space & 1) == 0) maxLR++;
		
		printf("Case #%d: %lld %lld\n", t, maxLR, minLR);
	}
	return 0;
}
