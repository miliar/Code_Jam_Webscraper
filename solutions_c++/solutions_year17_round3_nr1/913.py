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
struct st{
    ll r,h,side,sur;
}s[1004];
bool comp(struct st a,struct st b)
{
    return a.side>b.side;
}
int main()
{
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        ll ans=0,n,j,k,ma=0;
        cin>>n>>k;
        int i;
        rep(i,0,n-1)
        {
            cin>>s[i].r>>s[i].h;
            s[i].side=2*s[i].r*s[i].h;
            s[i].sur=s[i].r*s[i].r;
            ma=max(ma,s[i].sur);
        }

        sort(s,s+n,comp);

        ll tma=0,mas=0;
        rep(i,0,k-2)
        {
            ans+=s[i].side;
            tma=max(tma,s[i].sur);
        }
        if(tma==ma)
        {
            ans+=s[k-1].side;
            ans+=ma;
        }
        else{

            rep(i,k-1,n-1)
            {
                if(s[i].sur+s[i].side>=mas)
                {
                    mas=s[i].side+s[i].sur;
                }
                if(s[i].side+tma>=mas)
                {
                    mas=s[i].side+tma;
                }
            }
            ans+=mas;
        }
        long double ans1=ans;
        ans1*=pi;
        cout<<fixed;
        cout<<setprecision(10);
        cout<<"Case #"<<tt<<": "<<ans1<<endl;
    }
        return 0;
}
