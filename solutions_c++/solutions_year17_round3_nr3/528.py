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

const int maxn=60;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;

int n,K;
double U,p[maxn];

void init(){
	scanf("%d%d%lf",&n,&K,&U);
	fou(i,1,n) scanf("%lf",&p[i]);
}

void solve(){
	double sum,now,ave,ans;
	int id;
	bool flag;
	sort(p+1,p+n+1);
	sum=U;id=0;
	fou(i,1,n){
		now=(sum+p[i])/i;
		flag=true;
		fou(j,1,i)
			if (p[j]>now){
				flag=false;
				break;
			}
		if (flag){
			sum+=p[i];
			id=i;
		}else break;
	}
	ave=sum/id;
	ans=1;
	fou(i,1,id) ans*=ave;
	fou(i,id+1,n) ans*=p[i];
	printf("%.9f\n",ans);
}

int main(){
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-small-1-attempt0.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	fou(i,1,T){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
