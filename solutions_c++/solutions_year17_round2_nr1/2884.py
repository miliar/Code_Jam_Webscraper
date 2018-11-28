#include<bits/stdc++.h>
using namespace std;
int main()
{
	int k,i,j,t,T,m,n,d;
	long long p,l;
	long long  s=0LL,q,w;
	cin>>t;
	for(T=0;T<t;++T)
	{
		s=0LL;
		cin>>d>>n;
		for(i=0;i<n;++i)
		{
			cin>>j>>k;
			l=(long long)(d-j)*100000000LL;		
			l/=(long long)k;
			if(l>s)
				s=l;
			
		}
		p=(long long)d*100000000LL;
		double ee=(double)p/(double)(s);
		printf("Case #%d: %0.6lf\n",T+1,ee);		
	}
	return 0;
}
