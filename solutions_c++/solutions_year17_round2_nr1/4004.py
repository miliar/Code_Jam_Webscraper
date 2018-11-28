#include<bits/stdc++.h>
using namespace std;
bool pcomp(const pair<double,double> a,const pair<double,double> b)
{
	return a.first>b.first;	
}
double when(pair<double,double> a,pair<double,double> b)
{
	double tmp=(double)(a.first-b.first)/(double)(b.second-a.second);
	if(tmp<0)return -1;
	else return tmp;
}
int main()
{
	int T,K=1,D,N,k,s;
	vector<pair<double,double> >H;
	scanf("%d",&T);
	while(T--)
	{
		H.clear();
		scanf("%d%d",&D,&N);
		for(int i=0;i<N;i++)
		{
			scanf("%d%d",&k,&s);
			H.push_back(make_pair(k,s));
		}
		sort(H.begin(),H.end(),pcomp);
		double n;
		int cur=N-1;
		for(int i=N-1;i>0;i--)
		{
			n=when(H[i],H[i-1]);
			if(n!=-1)
			{
				if(H[i].first+(n*H[i].second)<D)
				{
					H[i].first=H[i-1].first;
					H[i].second=H[i-1].second;
					cur=i-1;
				}
			}
		}
		
		printf("Case #%d: %.6f\n",K,D/((D-H[cur].first)/(H[cur].second)));
		K++;
	}
	return 0;
}