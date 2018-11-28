#include <bits/stdc++.h>
using namespace std;

#define sd(x) 		scanf("%d",&x)
#define su(x) 		scanf("%u",&x)
#define slld(x) 	scanf("%lld",&x)
#define sc(x) 		scanf("%c",&x)
#define ss(x) 		scanf("%s",x)
#define sf(x) 		scanf("%f",&x)
#define slf(x)		scanf("%lf",&x)
#define ll 			long long int
#define mod(x,n) 	(x+n)%n
#define pb          push_back
#define mp          make_pair
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define sz(x)       (int)x.size()
#define Mod         1000000007

char S[100][100];

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	int i,j,k,l,m,n,x,y,z,c,t,a,b,r,tno;	char temp;
	// ll i,j,k,l,m,n,x,y,z,a,b,r;

	sd(t);	tno=1;
	while(tno<=t)
	{

		sd(r);	sd(c);

		for(i=0;i<r;i++)
			ss(S[i]);


		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(S[i][j]!='?')
				{
					for(k=i-1;k>=0;k--)
						if(S[k][j]=='?')
							S[k][j] = S[i][j];
						else
							break;
					for(k=i+1;k<r;k++)
						if(S[k][j]=='?')
							S[k][j] = S[i][j];
						else
							break;
				}
			}
		}

		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(S[i][j]!='?')
				{
					for(k=j-1;k>=0;k--)
						if(S[i][k]=='?')
							S[i][k] = S[i][j];
						else
							break;
					for(k=j+1;k<c;k++)
						if(S[i][k]=='?')
							S[i][k] = S[i][j];
						else
							break;
				}
			}
		}		

		printf("Case #%d:\n", tno );

		for(i=0;i<r;i++)
			printf("%s\n", S[i] );

		tno++;
	}

	
	return 0;
}