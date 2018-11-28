#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define repd(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define ll long long int
#define pi 3.14159265358979

int main()
{
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        long double ans=(long double)1.0,j,u,u1,p[104];
        int i,n,k,ii,ind,ind1;
        cin>>n>>k;
        cin>>u;
        ind=n-1;
        rep(i,0,n-1)
        {
            cin>>p[i];
        }
        sort(p,p+n);
        p[n]=(long double)1.0;
        rep(i,0,n-1)
        {
            j=p[i+1]-p[i];
            if(u>=j*(long double)(i+1))
            {
                u-=j*(long double)(i+1);
                rep(ii,0,i)
                    p[ii]=p[i+1];
            }
            else
            {
                j=u/(long double)(i+1);
                rep(ii,0,i)
                    p[ii]+=j;
                break;
            }
        }
        rep(i,0,n-1)
            ans*=p[i];
        cout<<fixed;
        cout<<setprecision(10);
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
        return 0;
}
