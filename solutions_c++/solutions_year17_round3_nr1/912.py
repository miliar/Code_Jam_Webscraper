#include<bits/stdc++.h>
#define PI acos(-1.0)
#define X first
#define Y second
#define mp make_pair
using namespace std;
vector<double> v;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A_large.txt","w",stdout);
	int a,b,c,num,T,N,K;
	double ans,sum,area,mc;
	pair<double,double> m[1010];
	scanf("%d",&T);
	for(a=0;a<T;a++)
	{
		scanf("%d %d",&N,&K);
		for(b=0;b<N;b++)
		{
			scanf("%lf %lf",&m[b].X,&m[b].Y);
		}
		sort(m,m+N);
		ans=0.0;
		sum=0.0;
		v.clear();
		for(c=0;c<N;c++)
		{
			ans=max(ans,PI*m[c].X*m[c].X+2*PI*m[c].X*m[c].Y);
		}
		for(b=0;b<N;b++)
		{
			area=2*PI*m[b].X*m[b].Y;
			sum+=area;
			v.push_back(-area);
			sort(v.begin(),v.end());
			if(v.size()>K-1)
			{
				sum+=v.back();
				v.pop_back();
			}
			mc=0.0;
			for(c=b+1;c<N;c++)
			{
				mc=max(mc,PI*m[c].X*m[c].X+2*PI*m[c].X*m[c].Y);
			}
			ans=max(ans,mc+sum);
		}
		printf("Case #%d: %lf\n",a+1,ans);
	}
}
