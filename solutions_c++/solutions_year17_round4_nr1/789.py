#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstdlib>

using namespace std;

int TT,n,P,ans,cur;
int cnt[5];

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&TT);
	for (int T=1;T<=TT;++T){
		scanf("%d%d",&n,&P);
		ans = 0;
		memset(cnt,0,sizeof cnt);
		for	(int i=1;i<=n;++i){
			scanf("%d",&cur);
			cnt[cur%P]++;
		}
		ans += cnt[0];
		if	(P == 2)
			ans += (cnt[1] + 1) / 2;
		if	(P == 3){
			int tmp = min(cnt[1], cnt[2]);
			ans += tmp;
			cnt[1] -= tmp;
			cnt[2] -= tmp;
			if	(cnt[1])
				ans += (cnt[1] + 2) / 3;
			else
				ans += (cnt[2] + 2) / 3;
		}
		if	(P == 4){
			int tmp = min(cnt[1], cnt[3]);
			ans += tmp;
			cnt[1] -= tmp;
			cnt[3] -= tmp;
			if	(cnt[2]&1){
				ans += cnt[2] / 2;
				if	(cnt[1])	cnt[1] += 2;
				else	cnt[3] += 2; 
			}
			else
				ans += cnt[2] / 2;
			if	(cnt[1])
				ans += (cnt[1] + 3) / 4;
			else
				ans += (cnt[3] + 3) / 4;
		} 
		printf("Case #%d: %d\n", T, ans);
	}
}
