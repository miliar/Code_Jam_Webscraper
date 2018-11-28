#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    freopen("1b.in","r",stdin);
    freopen("1b.out","w",stdout);
    ll t,j=1;
    cin>>t;
    while(j<=t)
    {
        ll n,i,k;
        double p,q,r;
        cin>>n>>k;
        double a[k];
        for(i=0;i<k;i++)
        {
            cin>>p>>q;
            r=((double)(n-p))/q;
            a[i]=r;
           //cout<<r<<endl;
        }
        sort(a,a+k);
        reverse(a,a+k);
        double sum=0.0;
        sum=((double)((double)n)/(double)a[0]);
        printf("Case #%d: ",j);
        printf("%.6f\n",sum);
        j++;
    }

}
