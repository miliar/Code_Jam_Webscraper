#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define repd(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define ll long long int

int main()
{
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {

        ll i,j,n,d,k,s,ck,cs;
        cin>>d>>n;
        cin>>ck>>cs;
        ck=d-ck;
        for(i=1;i<n;i++)
        {
            cin>>k>>s;
            k=d-k;
            if(k*cs>ck*s)
            {
                ck=k;
                cs=s;
            }
        }
        long double ans=cs*d;
        ans=ans/(long double)ck;
        cout<<fixed;
        cout<<setprecision(9);
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
        return 0;
}
