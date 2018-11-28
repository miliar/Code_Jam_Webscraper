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
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);

    fast
    ll t,i,j,k,cnt=0;
    s(t);

    while(cnt!=t)
    {
        cnt++;
        string data;
        s(data);
        s(k);

        ll l=data.length(),ans=0;
        for(i=0;i<=(l-k);i++)
        {
            if(data[i]=='-')
            {
                ans++;
                for(j=i;j<=i+k-1;j++)
                {
                    if(data[j]=='+')
                        data[j]='-';
                    else
                        data[j]='+';
                }
            }
        }
//        pmv("ans",ans);
        for(i=0;i<l;i++)
        {
            if(data[i]=='-')
                break;
        }
        if(i==l)
        {
            cout<<"Case #"<<cnt<<": "<<ans;
        }
        else
            cout<<"Case #"<<cnt<<": "<<"IMPOSSIBLE";
        pn();
    }
    return 0;
}













