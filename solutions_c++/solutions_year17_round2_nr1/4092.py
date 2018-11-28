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

struct DATA
{
    double k,sp;
};

bool comp(DATA A,DATA B)
{
    if(A.k<=B.k)
        return true;
    else
        return false;
}

int main()
{
    freopen("temp.in","r",stdin);
    freopen("output.out","w",stdout);
    fast;
    ll t,n,i,j,z=0;
    s(t);
    while(z!=t)
    {
        z++;
        double d,tm;
        s(d);
        s(n);
        vector<DATA> v;
        for(i=0;i<n;i++)
        {
            DATA temp;
            double ki,spi;
            s(ki);
            s(spi);
            temp.k=ki;
            temp.sp=spi;
            v.pb(temp);
        }

//        pm("printinb");
        sort(v.begin(),v.end(),comp);
        vector<double> ans(n,0);

//        for(i=0;i<n;i++)
//        {
//            p(v[i].k);
//            p(v[i].sp);
//            pn();
//        }

        ans[n-1]=(d-v[n-1].k)/(v[n-1].sp);
//        pmv("ansn-1 ",ans[n-1]);
        for(i=n-2;i>=0;i--)
        {
            ll pos=-1;
//            pmv(" i is ",i);
            for(j=i+1;j<n;j++)
            {
                if(v[i].sp>v[j].sp)
                {
                    double ca=(v[j].k-v[i].k)/(v[i].sp-v[j].sp);
                    double d1=v[j].sp*ca;
                    double d2=v[i].sp*ca;
                    if(d1<(d-v[j].k))
                    {
                        pos=j;
                        break;
                    }
                }
            }
            if(pos==-1)
            {
                ans[i]=(d-v[i].k)/v[i].sp;
            }
            else
            {
                ans[i]=ans[pos];
//                if(ans[i]==(double)0.0)
//                    pc();

            }
        }
//        pc();
        double res=d/ans[0];
//        pmv("ans0 ",ans[0]);
//        if(res==0.0)
//            pc();
        cout<<"Case #"<<setprecision(6)<<fixed<<z<<": "<<res;
        pn();
    }
    return 0;

}













