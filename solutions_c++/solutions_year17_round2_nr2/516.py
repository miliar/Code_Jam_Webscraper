#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second
#define mp make_pair
#define REP(i,j,k)  for(int i=(j);i<=(k);++i)
#define REPD(i,j,k) for(int i=(j);i>=(k);--i)

const int maxn = 10;

int e[maxn][maxn];
int a[maxn];
int n;

void init()
{
	REP(i,1,3)
		REP(j,1,3)
			if(i!=j)
				e[i][j]=1;
	REP(i,1,3)
		e[i][i%3+4]=e[i%3+4][i]=1;
}
void prt(int p)
{
	if(p==1) printf("R");
	if(p==2) printf("Y");
	if(p==3) printf("B");
	if(p==4) printf("O");
	if(p==5) printf("G");
	if(p==6) printf("V");
}
void tt(int p)
{
	if(a[p])
	{
		--a[p];
		prt(p);
	if(a[p]==0)
	{
		if(p==1) REP(i,1,a[5]) prt(5),prt(1);
		if(p==2) REP(i,1,a[6]) prt(6),prt(2);
		if(p==3) REP(i,1,a[4]) prt(4),prt(3);
	}
	}

}
int solve()
{
	scanf("%d%d%d%d%d%d%d",&n,a+1,a+4,a+2,a+5,a+3,a+6);
	/*
	if(n==2)
	{
		int t1=0,t2=0;
		REP(i,1,6)
			if(a[i])
			{
				if(t1) t2=i;
				else t1=i;
			}
		if(t2==0) return 0;
		if(e[t1][t2]==0) return 0;
		prt(t1);prt(t2);
		return 1;
	}
	*/
	if(a[4] > a[3] || a[5] > a[1] || a[6] > a[2]) return 0;
	if(a[4]==a[3] && a[4]+a[3]==n) {REP(i,1,n/2) prt(3),prt(4);return 1;}
	if(a[5]==a[1] && a[5]+a[1]==n) {REP(i,1,n/2) prt(5),prt(1);return 1;}
	if(a[6]==a[2] && a[6]+a[2]==n) {REP(i,1,n/2) prt(6),prt(2);return 1;}
	
	a[1]-=a[5];a[2]-=a[6];a[3]-=a[4];
	int t1=1,t2=2,t3=3;
	if(a[t1] < a[t2]) swap(t1,t2);
	if(a[t2] < a[t3]) swap(t2,t3);
	if(a[t1] < a[t2]) swap(t1,t2);
	if(a[t1] > a[t2]+a[t3] ) return 0;
	while(a[t2]>a[t3])
	{
		tt(t1);
		tt(t2);
	}
	while(a[t1])
	{
		tt(t1);
		tt(t2);
		if(a[t1])
		{
			tt(t1);
			tt(t3);
		}
	}
	if(a[t2]==a[t3])
	{
	while(a[t2]+a[t3])
	{
		tt(t2);
		tt(t3);
	}
	}else
	{
	while(a[t2]+a[t3])
	{
		tt(t3);
		tt(t2);
	}
	}
	return 1;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	init();
	int T;
	scanf("%d",&T);
	REP(i,1,T)
	{
		printf("Case #%d: ",i);
		if(solve()) puts("");
		else puts("IMPOSSIBLE");
	}
	return 0;
}
