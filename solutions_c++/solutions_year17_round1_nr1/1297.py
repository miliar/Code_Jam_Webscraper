#include <bits/stdc++.h>
#define si(n) scanf("%d",&n);
#define pi(n) printf("%d\n",n);
#define pl(n) printf("%lld\n",n);
#define sl(n) scanf("%lld",&n);
#define sd(n) scanf("%lf",&n);
#define pd(n) printf("%lf\n",n);
#define ss(s) scanf("%s",s);
#define ps(s) printf("%s\n",s);
#define pb push_back
#define ll long long int
#define maxn 35
#define sqrtn 317
#define maxm 1000005
#define minv(a,b,c) min(a,min(b,c))
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pli pair<ll,int>
#define eps 1e-9
#define mod 1000000007
#define psi pair < string,ll>
#define mp make_pair
#define BLOCK 450
using namespace std;

char s[maxn][maxn];

int main()
{
	int t;
	si(t);
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: \n",i);
		int r,c;
		si(r);si(c);

		for(int i=0;i<r;i++){
			ss(s[i]);
		}

		int fill=0;
		char c1,c2;
		for(int i=0;i<r;i++)
		{
			int lfill=0;
			for(int j=0;j<c;j++)
			{
				if(s[i][j]!='?')
				{
					c1=s[i][j];
					if(lfill==0)
					{
						c2=c1;
						fill=1;
					}
					lfill=1;
				}
				else if(lfill!=0)
				{
					s[i][j]=c1;
				}
			}

			if(lfill!=0)
			{
				for(int j=0;j<c;j++)
				{
					if(s[i][j]=='?')
					{
						s[i][j]=c2;
					}
					else
					{
						break;
					}
				}
			}

			if(lfill==0 && fill!=0)
			{
				for(int j=0;j<c;j++)
				{
					s[i][j]=s[i-1][j];
				}
			}
		}

		for(int i=r-1;i>=0;i--)
		{
			for(int j=0;j<c;j++)
			{
				if(s[i][j]=='?')
				{
					s[i][j]=s[i+1][j];
				}
			}
		}

		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				printf("%c",s[i][j] );
			}
			ps("");
		}
	}

}