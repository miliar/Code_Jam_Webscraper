#include<bits/stdc++.h>
using namespace std;
int find_least(double need,double have)
{
	int lb=0,ub=2e9;
	while(ub-lb>1)
	{
		int mid=(ub+lb)>>1;
		if(have>=0.9*need*(double)mid&&have<=1.1*need*(double)mid) ub=mid;
		else if(have<0.9*need*(double)mid) ub=mid;
		else lb=mid;
	}
	if(have>=0.9*need*(double)ub&&have<=1.1*need*(double)ub) return ub;
	return 0;
}
int find_max(double need,double have)
{
	int lb=0,ub=2e9;
	while(ub-lb>1)
	{
		int mid=(ub+lb)>>1;
		if(have>=0.9*need*(double)mid&&have<=1.1*need*(double)mid) lb=mid;
		else if(have<0.9*need*(double)mid) ub=mid;
		else lb=mid;
	}
	if(have>=0.9*need*(double)lb&&have<=1.1*need*(double)lb) return lb;
	return 0;
}
int main()
{
	freopen("in.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int T,cas=1;
	scanf("%d",&T);
	while(T--)
	{
		int kit=0;
		vector<double> V[55],req;
		bool used[55][55];
		for(int i=0;i<55;i++)
			for(int j=0;j<55;j++)
				used[i][j]=0;
		int n,p;
		scanf("%d %d",&n,&p);
		for(int i=1;i<=n;i++)
		{
			double tmp;
			scanf("%lf",&tmp);
			req.push_back(tmp);
		}
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=p;j++)
			{
				double tmp;
				scanf("%lf",&tmp);
				V[i].push_back(tmp);
			}
			sort(V[i].begin(),V[i].end());
		}
		for(int i=0;i<p;i++)
		{
			int mi=find_least(req[0],V[1][i]),ma=find_max(req[0],V[1][i]);
			if(mi==0||ma==0) continue;
			for(double servings=mi;servings<=ma;servings++)
			{
				vector<int> found;
				found.push_back(i);
				for(int j=2;j<=n;j++)
				{
					for(int k=0;k<p;k++)
					{
						if(used[j][k]) continue;
						int lb=find_least(req[j-1],V[j][k]),ub=find_max(req[j-1],V[j][k]);
						if(servings>=lb&&servings<=ub)
						{
							found.push_back(k);
							break;
						}
					}
					if(found.size()<j) break;
				}
				if(found.size()==n)
				{
					kit++;
					for(int j=0;j<n;j++) used[j+1][found[j]]=1;
					break;
				}
			}
		}
		printf("Case #%d: %d\n",cas++,kit);
	}
}
