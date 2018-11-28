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
#define sz(x)       (int)x.size()
#define Mod         1000000007
#define F           first
#define S           second

int D[107][107];
double Mat[107][107];
int Query[107][2];
int E[107];
int Sp[107];

priority_queue< pair<ll,int> , vector< pair<ll,int> >, greater< pair<ll,int> > > PQ;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	pair<ll,int> temp;
	int i,j,k,l,m,n,x,y,z,a,b,r,o,g,u,v,tno,t,q;
	// ll i,j,k,l,m,n,x,y,z,a,b,r;
	double time,dist;
	sd(t);	tno = 1;
	while(tno<=t)
	{
		sd(n);	sd(q);

		for(i=1;i<=n;i++)
		{
			sd(E[i]);	sd(Sp[i]);
		}

		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
			{
				sd(D[i][j]);
				Mat[i][j] = DBL_MAX;
			}
		}

		for(i=1;i<=q;i++)
		{
			sd(Query[i][0]);	sd(Query[i][1]);
		}


		for(i=1;i<=n;i++)
		{
			while(!PQ.empty())
				PQ.pop();

			PQ.push(mp(0,i));

			while(!PQ.empty())
			{
				temp = PQ.top();	PQ.pop();
				if(Mat[i][temp.S]!=DBL_MAX)
					continue;
				Mat[i][temp.S] = temp.F;	
				for(j=1;j<=n;j++)
				{
					if(Mat[i][j]==DBL_MAX && D[temp.S][j]!=-1 && temp.F+D[temp.S][j]<=E[i])
						PQ.push( mp(temp.F+D[temp.S][j],j) );
				}
			}

			for(j=1;j<=n;j++)
			{
				if(Mat[i][j]!=DBL_MAX)
					Mat[i][j] = Mat[i][j]/Sp[i];
			}	
		}

		for(k=1;k<=n;k++)
		{
			for(i=1;i<=n;i++)
			{
				for(j=1;j<=n;j++)
				{
					if( Mat[i][k]!=DBL_MAX && Mat[k][j]!=DBL_MAX && Mat[i][j] > Mat[i][k]+Mat[k][j] )
					{
						Mat[i][j] = Mat[i][k]+Mat[k][j];
					}
				}	
			}
		}		

		printf("Case #%d:",tno);
		for(i=1;i<=q;i++)
		{
			printf(" %0.8lf", Mat[Query[i][0]][Query[i][1]] );
		}
		printf("\n");	
		tno++;
	}	
	
	return 0;
}