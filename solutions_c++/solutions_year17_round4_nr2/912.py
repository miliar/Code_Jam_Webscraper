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

const int maxn=2010;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;

int n,m,C,ans1;
bool chw[maxn];
int match[maxn],cnt[maxn];
int ma[maxn][maxn],q[maxn][maxn];
bool v[maxn][maxn];

void init(){
	int x,y;
	scanf("%d%d%d",&n,&C,&m);
	memset(q,0,sizeof(q));
	memset(cnt,0,sizeof(cnt));
	fou(i,1,m){
		scanf("%d%d",&x,&y);
		cnt[y]++;
		q[y][cnt[y]]=x;
	}
}

bool find(int k)
{
	int j;
	fou(i,1,ma[k][0]){
		j=ma[k][i];
		if (!chw[j]){
			chw[j]=true;
			if (match[j]==0 || find(match[j])){
				match[j]=k;
				return true;
			}
		}
	}
	return false;
}

void getmatch()
{
	memset(match,0,sizeof(match));
	fou(i,1,cnt[1]){
		memset(chw,false,sizeof(chw));
		if (find(i)) ans1++;
	}
}

void solve(){
	int c1,c2,ans2,val;
	fou(i,1,C) sort(q[i]+1,q[i]+cnt[i]+1);
	memset(ma,0,sizeof(ma));
	fou(i,1,cnt[1])
		fou(j,1,cnt[2])
			if (q[1][i]!=q[2][j]) ma[i][++ma[i][0]]=j;
	ans1=0;
	getmatch();
	
	memset(v,false,sizeof(v));
	fou(i,1,cnt[2]){
		if (match[i]!=0) v[2][i]=v[1][match[i]]=true;
	}
	val=0;
	c1=0;
	fou(i,1,cnt[1])
		if (!v[1][i]){
			val=q[1][i];
			c1++;
		}
	c2=0;
	fou(i,1,cnt[2])
		if (!v[2][i]){
			val=q[2][i];
			c2++;
		}
	
	if (val==1){
		ans1+=c1+c2;
		ans2=0;
	}else
	{
		ans1+=max(c1,c2);
		ans2=min(c1,c2);
	}
	printf("%d %d\n",ans1,ans2);
}

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	fou(i,1,T){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
