#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<iomanip>
#include<vector>
#include<set>
#include<map>
#include<queue>

using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

#define rep(i,k,n) for(int i=(k);i<=(n);i++)
#define rep0(i,n) for(int i=0;i<(n);i++)
#define red(i,k,n) for(int i=(k);i>=(n);i--)
#define sqr(x) ((x)*(x))
#define clr(x,y) memset((x),(y),sizeof(x))
#define pb push_back
#define mod 1000000007


LL n,k;

int main()
{
	freopen("C:\\tmpcode\\gcj\\2017\\qround\\c\\C-large.in", "r", stdin);
	freopen("C:\\tmpcode\\gcj\\2017\\qround\\c\\mylargeoutput.txt", "w", stdout);
	int T;scanf("%d",&T);
	rep(ii,1,T)
	{
		scanf("%I64d%I64d",&n,&k);
		LL cur=1,ans1,ans2;
		LL val[2]={-1,-1},cnt[3]={0};
		val[0]=(n-1)/2;
		if(val[0]!=(n-1)-val[0])
		{
			val[1]=(n-1)-val[0];
			swap(val[0],val[1]);
			cnt[1]=1;
		}
		else cnt[0]=1;
		
		while((cur<<1)-1<k)
		{
			cur<<=1;
			LL tv[2]={-1,-1};
			LL tc[3]={0};
			rep(i,0,1)if(val[i]!=-1)
			{
				LL tt=(val[i]-1)/2;
				if(tv[0]==-1)tv[0]=tt;
				else if(tt!=tv[0] && tv[1]==-1)tv[1]=tt;
				tt=val[i]-1-tt;
				if(tv[0]==-1)tv[0]=tt;
				else if(tt!=tv[0] && tv[1]==-1)tv[1]=tt;
			}
			if(tv[1]!=-1 && tv[0]<tv[1])swap(tv[0],tv[1]);
			LL nxt[2][3]={0};
			rep(i,0,1)
			{
				LL mi=(val[i]-1)/2;
				LL mx=val[i]-1-mi;
				if(mi!=mx)nxt[i][1]++;
				else if(mi==tv[0])nxt[i][0]++;
				else nxt[i][2]++;
			}
			rep(i,0,2)tc[i]+=cnt[0]*2*nxt[0][i];
			rep(i,0,2)tc[i]+=cnt[1]*(nxt[0][i]+nxt[1][i]);
			rep(i,0,2)tc[i]+=cnt[2]*2*nxt[1][i];
			
			rep(i,0,1)val[i]=tv[i];
			rep(i,0,2)cnt[i]=tc[i];
		}
		k-=cur-1;
		rep(i,0,2)
		{
			if(k<=cnt[i])
			{
				int a=0,b=0;
				if(i==1)b=1;
				else if(i==2)a=b=1;
				ans1=val[a];
				ans2=val[b];
				break;
			}
			k-=cnt[i];
		}
		
		printf("Case #%d: %I64d %I64d\n",ii,ans1,ans2);
	}
	
	
	return 0;
}
