#include<bits/stdc++.h>
using namespace std;
int main()
{
	int i,j,t,T;
	long long n,a,b;
	cin>>t;
	for(T=0;T<t;++T)
	{
		cin>>n;
		for(i=n;i>=1;--i)
		{
			j=i;
			n=9;
			while(j)
			{
				if(j%10<=n)
					n=j%10;
				else
					break;
				j/=10;
			}
			if(j==0)
			{
				printf("Case #%d: %d\n",T+1,i);
				break;
			}
		}				
	}
	return 0;
}
