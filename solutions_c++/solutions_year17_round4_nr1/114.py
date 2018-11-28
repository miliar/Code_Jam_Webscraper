#include <stdio.h>
#define min(a,b)((a)<(b)?(a):(b))
#define max(a,b)((a)>(b)?(a):(b))

int left[5];

int main(){
	int jcase;
	int N, K;
	
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	
	scanf("%d", &jcase);
	for(int icase=0; icase<jcase; icase++){
		scanf("%d %d", &N, &K);
		for(int i=0; i<5; i++) left[i] = 0;
		
		for(int i=0; i<N; i++){
			int n;
			scanf("%d", &n);
			left[n%K]++;
		}
		
		int ans = 0;
		if(K == 2){
			ans = left[0];
			ans += (left[1]+1)/2;
		}
		else if(K == 3){
			ans = left[0];
			int r = min(left[1], left[2]);
			int r2 = max(left[1], left[2]);
			ans += r;
			ans += (r2-r+2)/3;
		}
		
		printf("Case #%d: %d\n", icase+1, ans);
		
		//fprintf(stderr, "case %d/%d\n", icase+1, jcase);
	}
	return 0;
}
