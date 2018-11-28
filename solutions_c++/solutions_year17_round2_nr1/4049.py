#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
int t;
cin>>t;
cout<<fixed;
cout<<setprecision(6);
for(int i=1;i<=t;++i)
	{
	cout<<"Case #"<<i<<": ";
	unsigned int d,n;
	cin>>d>>n;
	double temp,n1,n2,max=0;
	for(int j=0;j<n;++j)
		{
		double k,s;
		cin>>k>>s;
		temp=(d-k)/s;
		if(temp>max)
			{
			max=temp;
			n1=k;
			n2=s;
			}
		}	
	cout<<(d*n2)/(d-n1)<<'\n';
	}
	return 0;
}
