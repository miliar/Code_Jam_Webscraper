#define LOCAL
#include<iostream>
using namespace std; 

int main()
{
	#ifdef LOCAL
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	#endif
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		int n,d;
		cin>>d>>n;
		int ki[n],si[n];
		// float meetD[n];
		float maxmeet=0.0;
		for(int iter=0;iter<n;iter++){
			cin>>ki[iter]>>si[iter];
			// meetD[iter]=float(d-ki)/si;
			if((float(d-ki[iter]))/si[iter]>maxmeet)maxmeet=float(d-ki[iter])/si[iter];
			// cout<<maxmeet<<endl;
		}
		printf("%.6f\n",d/maxmeet);
		// cout<<setprecision(2)<<d/maxmeet<<endl;
	}
	return 0;
}
