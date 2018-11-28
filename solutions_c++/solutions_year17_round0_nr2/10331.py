#include <iostream>
using namespace std;

int main() {
	long long int k,t;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		long long int n,m,i,d,d1;
		cin>>n;
		for(i=n;i>=0;i--)
		{
			m=i;
			int f=0;
			while(m!=0)
			{
				d=m%10;
				m=m/10;
				d1=m%10;
				if(d<d1)
				{
					f=1;
					break;
				}
			}
			if(f==0)
			{
				cout<<"Case #"<<k<<": "<<i<<endl;;
				break;
			}
		}
	}
	return 0;
}
