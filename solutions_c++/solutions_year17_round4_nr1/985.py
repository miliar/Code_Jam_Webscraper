#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iomanip>
#include<sstream>
#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<bitset>
#define fou(i,j,k) for (int i=j;i<=k;i++)
#define fod(i,j,k) for (int i=j;i>=k;i--)
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> Pii;

const int maxn=110;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;

int n,P,a[maxn],cnt[10];

void init(){
	scanf("%d%d",&n,&P);
	fou(i,1,n) scanf("%d",&a[i]);
}

void solve(){
	int ans,now;
	memset(cnt,0,sizeof(cnt));
	fou(i,1,n) cnt[a[i]%P]++;
	ans=cnt[0];
	if (P==2) ans+=(cnt[1]+1)/2; else
	if (P==3){
		if (cnt[1]<cnt[2]){
			ans+=cnt[1];
			cnt[2]-=cnt[1];
			ans+=(cnt[2]+2)/3;
		}else
		{
			ans+=cnt[2];
			cnt[1]-=cnt[2];
			ans+=(cnt[1]+2)/3;
		}
	}else
	if (P==4){
		now=min(cnt[1],cnt[3]);
		ans+=now;cnt[1]-=now;cnt[3]-=now;
		ans+=cnt[2]/2;cnt[2]%=2;
		if (cnt[2]==1 && cnt[1]>=2){
			ans++;
			cnt[2]=0;cnt[1]-=2;
		}
		if (cnt[2]==1 && cnt[3]>=2){
			ans++;
			cnt[2]=0;cnt[3]-=2;
		}
		ans+=cnt[1]/4;cnt[1]%=4;
		ans+=cnt[3]/4;cnt[3]%=4;
		if (cnt[1]>0 || cnt[2]>0 || cnt[3]>0) ans++;
	}
	printf("%d\n",ans);
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	fou(i,1,T){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
