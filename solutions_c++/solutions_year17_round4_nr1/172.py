#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
template<class T> inline bool ten(T &x,const T &y){return y<x?x=y,1:0;}
template<class T> inline bool rel(T &x,const T &y){return x<y?x=y,1:0;}
int n,p;
int s[5];
int f[105][105][105];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T=0;cin>>T;
	for(int qi=1;qi<=T;qi++)
	{
		printf("Case #%d: ",qi);
		scanf("%d%d",&n,&p);
		for(int i=0;i<p;i++)s[i]=0;
		int sum=0;
		for(int t,i=1;i<=n;i++)
			scanf("%d",&t),sum+=t,s[t%p]++;
		int ans=1;
		if(sum%p==0)ans=0;
		ans+=s[0];
		if(p==2)
		{
			ans+=s[1]/2;
		}
		else if(p==3)
		{
			ans+=min(s[1],s[2])+(max(s[1],s[2])-min(s[1],s[2]))/3;
		}
		else if(p==4)
		{
			/*
			1+3
			2+2
			1+1+2
			2+3+3
			1+1+1+1
			3+3+3+3
			*/
			for(int i=0;i<=s[1];i++)
				for(int j=0;j<=s[2];j++)
					for(int k=0;k<=s[3];k++)
					{
						f[i][j][k]=0;
						if(i>=1&&k>=1)rel(f[i][j][k],f[i-1][j][k-1]+1);
						if(j>=2)rel(f[i][j][k],f[i][j-2][k]+1);
						if(i>=2&&j>=1)rel(f[i][j][k],f[i-2][j-1][k]+1);
						if(j>=1&&k>=2)rel(f[i][j][k],f[i][j-1][k-2]+1);
						if(i>=4)rel(f[i][j][k],f[i-4][j][k]+1);
						if(k>=4)rel(f[i][j][k],f[i][j][k-4]+1);
					}
			ans+=f[s[1]][s[2]][s[3]];
		}
		printf("%d\n",ans);
	}
	return 0;
}

