#include<bits/stdc++.h>
using namespace std;
const int maxn=1001;
long long d;
long long k[maxn],s[maxn];
int n;
const double eps=1e-8;
int main()
{
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;++cas)
	{
		scanf("%I64d%d",&d,&n);
		//if(cas==53)printf("%I64d %d\n",d,n);
		double l=0,r=1e20;
		for(int i=0;i<n;++i)
		{
			scanf("%I64d%I64d",&k[i],&s[i]);
			//if(cas==53)printf("%I64d %I64d\n",k[i],s[i]);
		}
		for(int i=0;i<2000;++i)
		{
			double mid=(l+r)/2;
			bool flag=true;
			for(int j=0;j<n;++j)
			{
				double len=k[j]/(mid-s[j])*mid;
				//cout <<len<<" "<<mid<<" "<<s[j]<<" "<<k[j]<<endl;
				if(0<len&&len<d)flag=false;
			}
			if(flag)l=mid;
			else r=mid;
		}
		printf("Case #%d: %.6f\n",cas,r);
	}
	return 0;
}
