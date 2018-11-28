#include<iostream>
using namespace std;
int main()
{
	double k[1000],d;
	int s1[1000],s,T,n,i;
	double t=0.00,x;
	cin>>T;
	for(s=0;s<=T-1;s++)
	{
		cin>>d>>n;
		t=0.00;
		for(i=0;i<=n-1;i++)
		{
			cin>>k[i]>>s1[i];
			if(t<((d-k[i])/(double)s1[i]))
			t=((d-k[i])/(double)s1[i]);
			//cout<<((d-k[i])/s1[i]);
		}
		//cout<<t;
		x=(double)d/t;
	    cout.setf(ios::fixed,ios::floatfield);
        cout.precision(6);
		cout<<"Case #" << s+1 << ": " <<x<<"\n";
	}
}

