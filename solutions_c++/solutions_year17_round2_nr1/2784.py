#include <bits/stdc++.h>
#define pb push_back
using namespace std;
typedef long long int ll;

int main(int argc, char const *argv[])
{
	int t,c=1;
	cin>>t;
	// ofstream ofile;
	// ofile.open("out.txt",ios::out);
	FILE *f = fopen("out.txt", "w");
	while(t--)
	{
		ll n,d;

		cin>>d>>n;
		double time=(double)INT_MIN;

		for(ll i=0;i<n;i++)
		{
			ll a,b;
			cin>>a>>b;
			double t = (double)(d-a)/(double)b;
			time = max(t,time);
		}

		double d1 = (double)(d)/time;

		// ofile<<"Case #"<<c<<": "<<std::setprecision(6)<<d1<<endl;
		fprintf(f, "Case #%d: %0.6f\n", c,d1);
		c++;

	}
	return 0;
}