#include<bits/stdc++.h>
#define fast ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define FOR(i,a,b) for(i=a;i<b;++i)
#define FORD(i,a,b) for(i=a;i>=b;--i)
#define FORIT(it,a,b) for(it=a;it!=b;it++)
#define tpI(i,a,b,v) for(i=a;i<b;i++) { p(v[i]);} pn();
#define tpL(i,a,b,v) for(i=a;i<b;i++) { pl(v[i]);} pn();
#define ll long long
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define infi 1000000007
#define PI 3.14159265
#define s(x) cin>>x
#define fi first
#define se second
#define p(x) cout<<x<<" "
#define pn() cout<<endl
#define pc() cout<<"testing "<<endl
#define pm(m) cout<<m<<endl
#define pmv(m,x) cout<<m<<" "<<x<<endl
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);

    fast
    ll t,n,i,j,l,cnt=0;
    s(t);
    while(cnt!=t)
    {
        cnt++;
        s(n);
        vector<ll> v;
        ll temp=n;
        while(n!=0)
        {
            v.pb(n%10);
            n=n/10;
        }
        reverse(v.begin(),v.end());
//        for(i=0;i<v.size();i++)
//            p(v[i]);
//        pn();

        l=v.size();
        while(true)
        {
            bool found=false;
            //find first index where the val is greater than next
            for(i=0;i<l-1;i++)
            {
                if(v[i]>v[i+1])
                {
                    found=true;
                    break;
                }
            }

            if(found==true)
            {
                for(j=i+1;j<l;j++)
                {
                    v[j]=9;
                }
                if(v[i]==0)
                    v[i]=9;
                else
                    v[i]--;
            }
            else
                break;

//            for(i=0;i<l;i++)
//                p(v[i]);
//            pn();
        }
//
//        pm("final ");

        for(i=0;i<l;i++)
        {
            if(v[i]!=0)
                break;
        }
        cout<<"Case #"<<cnt<<": ";
        for(i;i<l;i++)
        {
            cout<<v[i];
        }
        pn();
    }
    return 0;
}










