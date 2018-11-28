#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
	long long int n,v,d,x;
	double mini=(double)(1e18);
	scanf("%lld%lld",&d,&n);
	for(int j=0;j<n;j++)
	{
	    scanf("%lld%lld",&x,&v);
	    double ans=(double)((double)(v*d)/(double)(d-x));
	    mini=min(ans,mini);
	}
	printf("Case #%d: %.6f\n",i+1,mini);
    }
    return 0;
}
