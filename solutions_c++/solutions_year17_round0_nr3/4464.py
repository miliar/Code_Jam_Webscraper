#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		double N,K;
		cin>>N>>K;
		double n1 = log2(K+1);
		int n = n1;
		if(n1==n)
			n = n-1;
		double options = pow(2.0,n);
		long long N1=N,options1=options;
		long long x,y;
		y = (N1+1)%options1;
		x = (N1+1)/(options1) - 1;
		long long alpha = K+1-options1;
		long long min,max;
		if(alpha<=y)
		{
			x = x+1;
		}
		if(x%2==0)
		{
			max = x/2;
			min = max-1;
		}
		else
		{
			min = x/2;
			max = x/2;
		}
		cout<<"Case #"<<i<<": "<<max<<" "<<min<<endl;


	}
}