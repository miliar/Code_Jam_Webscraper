#include <bits/stdc++.h>
using namespace std;

#define MAXN 103

int T, N, P;
int A[MAXN];

int main()
{
	for (scanf("%d", &T);T--;){
		scanf("%d%d", &N, &P);
		int cnt[4] = {0,};
		for (int i=1;i<=N;i++){
			scanf("%d", A+i); A[i] %= P;
			cnt[A[i]]++;
		}
		int ans = -1;
		if (P == 2){
			ans = cnt[0] + ((cnt[1]+1) >> 1);
		}else if (P == 3){
			ans = cnt[0];
			if (cnt[1] > cnt[2]){
				int d = cnt[1] - cnt[2];
				ans += cnt[2];
				ans += (d-1)/3+1;
			}else{
				int d = cnt[2]-cnt[1];
				ans += cnt[1];
				if (d) ans += ((d*2-1)/3+1 -1)/2+1;
			}
		}
		static int ts = 0;
		printf("Case #%d: %d\n", ++ts, ans);
	}
}