#include <bits/stdc++.h>
using namespace std;

vector<pair<long long,long double> >v;

int main() 
{
    int t;
    long long k[1001],d;
    long long s[1001],i,j,n,K=1;
    long double ftime[1001],ans,x;
    cin>>t;
    while(t>0)
    {
        v.clear();
        cout<<"Case #"<<K<<": ";
        ++K;
        cin>>d>>n;
        for(i=n-1;i>=0;--i)
        cin>>k[i]>>s[i];
        
        ftime[n-1]=(d-k[n-1])/s[n-1];
        v.push_back({s[n-1],ftime[n-1]});
        for(i=n-2;i>=0;--i)
        {
            x=(long double)(k[n-1]-k[n-2])/(s[n-2]-s[n-1]);
            if(x>ftime[n-1] || x<0)
            ftime[i]=1.0*(d-k[n-2])/s[n-2];
            else
            ftime[i]=x+1.0*(d-(k[n-2]+s[n-2]*x))/s[n-1];
        }
        ans=d/ftime[0];
        printf("%.6Lf\n",ans);
        --t;
    }
	return 0;
}

