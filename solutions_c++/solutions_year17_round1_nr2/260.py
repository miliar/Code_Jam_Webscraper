#define PII pair<int,int>
#include <bits/stdc++.h>

using namespace std;

const int N=1<<6;
const double EPS=1E-10;

vector<PII> v[N];
int T,n,p,x,cas,res,r[N];

int main()
{
	for(cin>>T;T--;)
	{
		cin>>n>>p,res=0;
		for(int i=1;i<=n;i++)
			scanf("%d",r+i),v[i].clear();
		for(int i=1;i<=n;i++)
			for(int j=1;j<=p;j++)
			{
				scanf("%d",&x);
				int L=ceil(double(x)/1.1/r[i]-EPS),R=double(x)/0.9/r[i]+EPS;
				v[i].push_back(PII(L,R));
			}
		for(int i=1;i<=n;i++)
			sort(v[i].begin(),v[i].end());

		for(int u=1<<20;u>0;u--)
			for(bool flag=1;flag;)
			{
				for(int i=1;i<=n;i++)
				{
					for(;!v[i].empty() && u<(*v[i].rbegin()).first;v[i].pop_back());
					if(v[i].empty() || (*v[i].rbegin()).second<u) flag=0;
				}
				if(flag)
				{
					for(int i=1;i<=n;i++)
						v[i].pop_back();
					res++;
				}
			}
		printf("Case #%d: %d\n",++cas,res);
	}
}