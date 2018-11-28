#include <iostream>
#include <iomanip>

using namespace std;

int t;
long double d, n;
long double s;
long double k;
long double tim;
long double tim_m;

int main()
{
	cout<<setprecision(100);
	cin>>t;
	for(int i=1; i<=t; i++)
	{
		cin>>d>>n;
		
		for(int j=0; j<n; j++)
		{
			cin>>k>>s;
			tim = ((d-k)/s);
			tim_m = max(tim,tim_m);
		}
		cout<<"Case #"<<i<<": "<<(d/tim_m)<<endl;
		tim_m = 0;
	}
}
