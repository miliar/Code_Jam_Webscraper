#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("c-large.out", "w", stdout);
    ll t;
    cin>>t;
    for(ll loop=1;loop<=t;++loop)
    {
        ll n,k,ansmax,ansmin;
        cin>>n>>k;
        ll ncopy=n;
        ll rmin=1,rmax=1;
        ll range=1;
        ll a,b,c,d;
        if(n%2==0)
        {
            a=n/2;
            b=n/2-1;
            c=1;
            d=1;
        }
        else
        {
            a=n/2;
            b=n/2;
            c=1;
            d=1;
        }
        if(k==1)
        {
           cout<<"Case #"<<loop<<": "<<a<<" "<<b<<endl;
           continue;
        }
        while(rmax+2*range<k)
        {
            rmin=rmax+1;
            range*=2;
            rmax=rmin+range-1;

            if(a==b)
            {
                if(a%2==0)
                {
                    a=a/2;
                    b=max(a-1,0LL);
                }
                else
                {
                    a=a/2;
                    b=a;
                }
                c=2*c;
                d=2*d;
            }
            else{
            if(a%2==0)
            {
                a=a/2;
                b=max(a-1,0LL);
                d=2*d+c;
            }
            else
            {
                a=a/2;
                b=max(a-1,0LL);
                c=c*2+d;
            }
            }
        }
        ll togo=k-rmax;
        //cout<<a<<" "<<b<<" "<<c<<" "<<d<<endl;
        if(togo-c<=0)
        {
            if(a%2==0)
            {
                ansmax=a/2;
                ansmin=max(0LL,a/2-1);
            }
            else
            {
                ansmax=a/2;
                ansmin=a/2;
            }
        }
        else
        {
            if(b%2==0)
            {
                ansmax=b/2;
                ansmin=max(0LL,b/2-1);
            }
            else
            {
                ansmax=b/2;
                ansmin=b/2;
            }
        }
        cout<<"Case #"<<loop<<": "<<ansmax<<" "<<ansmin<<endl;

    }
    return 0;
}
