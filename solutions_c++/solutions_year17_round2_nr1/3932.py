#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair

typedef long long int ll;
using namespace std;
int k[1005],s[1005];
int main()
{

    freopen("try.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t,kk=0,d,n;
    cin>>t;
    while(t--)
    {

        kk++;
        cout<<"Case #"<<kk<<": ";
        cin>>d>>n;
        double prec=1e-6,lo=0.0,hi=1e13,sol=-1e10;
        double maxx=-1e10;
        for(int i=0; i<n; i++)
        {
            cin>>k[i]>>s[i];
        }
        for(int i=0; i<n; i++)
        {
            double t=double(d-k[i])/double(s[i]);
            if(t>maxx)maxx=t;
        }
        while(hi-lo>=prec&&lo<=hi)
        {
            double mid=(hi+lo)/(double)2;
            double t=double(d)/double(mid);
            if(t>=maxx)
            {
                lo=mid+(1e-6);
                sol=max(sol,mid);
            }
            else
            {
                hi=mid-(1e-6);
            }
        }
        printf("%.7lf\n",sol);
    }
    return 0;
}
