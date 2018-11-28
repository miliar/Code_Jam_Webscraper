#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define pp pair<double,double>
#define mp make_pair
#define pb push_back
#define S second
#define F first
const int MAX=1e3+2;
pp a[MAX];
vector < pp > s[MAX];
bool comp(pp x,pp y)
{
	if(x.F!=y.F) return x.F>y.F;
	return x.S<y.S;
}
int main()
{
	int t,no=0,i,j,n;
	double px,ps,tt,xx,mt,ans,end,d,q;
	scanf("%d",&t);
	while(t--)
	{
		no++;
		scanf("%lf %d",&d,&n);
		for(i=0;i<=n;i++) s[i].clear();
		for(i=0;i<n;i++)
			scanf("%lf %lf",&a[i].F,&a[i].S);
		sort(a,a+n,comp);
		ans=(d-a[0].F)/a[0].S;
		s[0].pb(mp(a[0].F,ans));
		for(i=1;i<n;i++)
		{
			px=a[i].F;
			ps=a[i].S;
			ans=0;
			for(j=0;j<s[i-1].size();j++)
			{
				tt=s[i-1][j].S;
				xx=s[i-1][j].F;
				end=(j+1==s[i-1].size())?d:s[i-1][j+1].F;
				q=(end-xx)/tt;
				//cout<<q<<endl;
				mt=(xx-px)/abs(ps-q);
				if(mt>=tt||(ps<q))
					s[i].pb(mp(px,tt)),px+=tt*ps,ans+=tt;
				else
				{
					s[i].pb(mp(px,mt));
					px+=mt*ps;
					ans+=mt;
					//cout<<mt<<endl;
					s[i].pb(mp(px,(end-s[i-1][j].F)/s[i-1][j].S));
					ans+=(end-px)/((end-s[i-1][j].F)/s[i-1][j].S);
					ps=(end-px)/((end-s[i-1][j].F)/s[i-1][j].S);
					px=end;
				}
			}
			//if(!s[i].size()) s[i].pb(mp(a[i].F,(d-a[i].F)/a[i].S));
		}
		if(px!=d&&n>1) ans+=(d-px)/ps;
		/*ans=0;
		for(j=0;j<s[n-1].size();j++)
		{
			end=(j+1==s[n-1].size())?d:s[n-1][j+1].F;
			//q=(end-s[n-1][j].F)/((end-s[i-1][j].F)/s[i-1][j].S);
			//if(end==d) 
			ans+=s[n-1][j].S;
		}*/
		//if(end!=d) ans+=(d-s[n-1][j-1].F)/s[n-1][j-1].S;
		ans=d/ans;
		printf("Case #%d: %lf\n",no,ans);
	}
	return 0;
}