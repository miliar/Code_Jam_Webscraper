#include<bits/stdc++.h>
using namespace std;

int d,n;
vector<pair<int,int> > mat;
vector<double> ti;
int main()
{
	int t;
	scanf("%d",&t);
	for(int it=1;it<=t;it++)
	{
		scanf("%d %d",&d,&n);
		mat.clear();
		mat.resize(n);
		for(int i=0;i<n;i++)
			scanf("%d %d",&(mat[i].first),&(mat[i].second));
		sort(mat.begin(), mat.end());
		ti.clear();
		ti.resize(n);
		for(int i=0;i<n;i++)
		{
			ti[i]=(d*1.0-mat[i].first)/((mat[i].second)*1.0);
		}
		for(int i=n-2;i>=0;i--)
		{
			if(ti[i]<ti[i+1])
			{
				double d1=mat[i+1].first-mat[i].first;
				double s1=mat[i].second-mat[i+1].second;
				double t1=d1/s1;
				double d2=(mat[i].second)*t1;
				double t2=(d-d2-mat[i].first)/(mat[i+1].second);
				ti[i]=t1+t2;
			}
		}
		double ans=d/ti[0];
		printf("Case #%d: %lf\n",it,ans);
		/*
		for(int i=0;i<n;i++)
		{
			printf("%lf ",d/ti[i]);
		}
		printf("\n");*/
	}
	return 0;
}