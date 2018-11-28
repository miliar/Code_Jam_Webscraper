#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
int T,n,c,m;
typedef pair<int,int> ii;
#define fi first
#define se second
#define maxn 1010
int cnt[maxn];
ii a[maxn];
int ans;
int S[maxn];
bool test(int x){
	int sum=0;ans=0;
	for (int i=n;i;i--) {
		int now=S[i],r=x;
		int t=min(x,now);
		now-=t;
		r-=t;
		ans+=now;
		t=min(sum,r);
		r-=t;
		sum-=t;
		sum+=now;
	}
	return sum==0;
}
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for (int _=1;_<=T;_++) {
		memset(cnt,0,sizeof(cnt));
		memset(S,0,sizeof(S));
		scanf("%d%d%d",&n,&c,&m);
		for (int i=1;i<=m;i++) {
			scanf("%d%d",&a[i].fi,&a[i].se);
			cnt[a[i].se]++;
			S[a[i].fi]++;
		}
		sort(a+1,a+1+m);
		int mn=0;
		for (int i=1;i<=c;i++) mn=max(mn,cnt[i]);
		for (int i=mn;;i++) {
			if (test(i)) {
				printf("Case #%d: %d %d\n",_,i,ans);
				break;
			}
		}
	}
}
