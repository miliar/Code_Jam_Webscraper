#include<bits/stdc++.h>
using namespace std;
int n, k, cnt[5];

void solve (int tc) {
	printf("Case #%d: ",tc);
	scanf("%d%d",&n,&k);
	for(int i=0;i<k;i++) cnt[i] = 0;
	for(int i=1;i<=n;i++) {
		int T;
		scanf("%d",&T);
		cnt[T%k]++;
	}
	if(k == 2) printf("%d\n", cnt[0] + (cnt[1]+1)/2);
	if(k == 3) printf("%d\n", cnt[0] + min(cnt[1], cnt[2]) + (max(cnt[1], cnt[2]) - min(cnt[1], cnt[2]) + 2)/3);
	if(k == 4) {
		if(cnt[1] > cnt[3]) swap(cnt[1], cnt[3]);
		cnt[2] += (cnt[3] - cnt[1]) / 2;
		cnt[3] = (cnt[3] - cnt[1]) % 2;
		printf("%d\n",cnt[0] + cnt[1] + cnt[2]/2 + (cnt[3]+cnt[2]%2 ? 1 : 0));
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tc;
	scanf("%d",&tc);
	for(int i=1;i<=tc;i++) solve(i);
}
