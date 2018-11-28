#include<bits/stdc++.h>
#define ll long long int
using namespace std;
FILE *in=freopen("in.txt","r",stdin);
FILE *out=freopen("out.txt","w",stdout);

int main()
{
	int t;
	cin>>t;
    for(int m=1;m<=t;m++)
    {
    	double d;
    	int n;
    	cin>>d>>n;
    	double k[n],s[n];
    	double time=0.000000;
    	for(int i=0;i<n;i++)
    		{
			cin>>k[i]>>s[i];
            time=max(time,(d-k[i])/s[i]);
			}
		double ans;
		ans=d/time;
		cout<<"Case #"<<m<<": "<<setprecision(6)<<ans<<fixed<<endl;
	}
	return 0;
}
