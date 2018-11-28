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
#define maxn 10005
#define sqrtn 317
#define maxm 1000005
#define minv(a,b,c) min(a,min(b,c))
#define pii pair<int,int>
#define pll pair<ll,ll>
#define eps 1e-9
#define mod 1000000007
#define psi pair < string,ll>
#define mp make_pair
#define BLOCK 450
using namespace std;
char s[maxn];

int main()
{
	int t;
	si(t);
	for(int i=1;i<=t;i++)
	{
		int k;
		printf("Case #%d: ",i);
		ss(s);
		si(k);
		int n=strlen(s);
		int flag=1;
		int steps=0;
		for(int i=0;i<n;i++)
		{
			if(s[i]=='-')
			{
				if(i>n-k)
				{
					flag=0;
				}
				else
				{
					steps++;
					for(int j=i;j<i+k;j++)
					{
						if(s[j]=='+')
						{
							s[j]='-';
						}
						else
						{
							s[j]='+';
						}
					}
				}
			}
		}
		if(flag==0)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n",steps);
		}
	}
}