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

string Temp[1007];
pair< int, char > A[7];

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	int i,j,k,l,m,n,x,y,z,a,b,r,o,g,v,tno,t;
	// ll i,j,k,l,m,n,x,y,z,a,b,r;

	sd(t);	tno = 1;
	while(tno<=t)
	{

		sd(n);	sd(r);	sd(o);	sd(y);	sd(g);	sd(b);	sd(v);

		A[0] = mp(r,'R');
		A[1] = mp(y,'Y');
		A[2] = mp(b,'B');

		if( r>b+y || b>r+y || y>b+r )
		{
			printf("Case #%d: IMPOSSIBLE\n", tno );
		}	
		else
		{
			sort(A,A+3);
			l = 0;	j=0;
			for(i=2;i>=0;i--)
			{
				if(i==2)
				{
					while(A[i].F > 0)
					{
						Temp[l++].pb(A[i].S);
						(A[i].F)--;
					}
				}
				else
				{
					while(A[i].F > 0)
					{
						Temp[j].pb(A[i].S);
						j = (j+1)%l;
						(A[i].F)--;
					}
				}
			}
			printf("Case #%d: ",tno);
			for(i=0;i<l;i++)
			{
				cout<<Temp[i];
				Temp[i].clear();
			}
			printf("\n");

		}
		tno++;
	}	
	
	return 0;
}