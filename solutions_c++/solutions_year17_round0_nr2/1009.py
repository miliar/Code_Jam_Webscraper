#include <bits/stdc++.h>
using namespace std;

#define sd(x) scanf("%d",&x)
#define su(x) scanf("%u",&x)
#define slld(x) scanf("%lld",&x)
#define sc(x) scanf("%c",&x)
#define ss(x) scanf("%s",x)
#define sf(x) scanf("%f",&x)
#define slf(x) scanf("%lf",&x)
#define ll long long int
#define mod(x,n) (x+n)%n

char S[27];

void process(char S[],int n)
{
	if(n==1)
		return;
	int i,j,k,l;

	for(i=1;i<n;i++)
	{
		if(S[i-1]>S[i])
		{
			if(S[i-1]=='1')
			{
				for(j=0;j<n-1;j++)
					S[j]='9';
				S[n-1]='\0';
			}
			else
			{
				for(j=i-1;j!=0 && S[j]==S[j-1];j--);
					S[j]--;
				for(j++;j<n;j++)
				{
					S[j]='9';
				}
			}
			return;
		}
	}

}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	ll i,j,k,l,m,n,t,tno;

	slld(t);	tno=1;
	while(tno<=t)
	{
		ss(S);

		process(S,strlen(S));

		printf("Case #%lld: %s\n", tno,	S );
		tno++;
	}
	
	return 0;
}