#include<bits/stdc++.h>
#include <unistd.h>
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
#define PI 3.141592653589
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
    ll r,h;
};

        ll dp[1001][1001];
        ll pos[1001][1001];


bool comp(DATA A, DATA B)
{
    if(A.r>B.r)
        return true;
    else
        return false;
}

int main()
{
    freopen("1C-Alarge.in","r",stdin);
    freopen("output2.out","w",stdout);
    fast;
    ll t,n,k,i,j,test=0;
    s(t);

    while(test!=t)
    {
        test++;

        s(n);
        s(k);
        vector<DATA> v;



        for(i=0;i<n;i++)
        {
            DATA temp;
            s(temp.r);
            s(temp.h);
            v.pb(temp);
        }

        sort(v.begin(),v.end(),comp);


        vector<ll> save;
        for(i=0;i<n;i++)
        {
            save.pb(2*v[i].r*v[i].h);
        }

        for(i=0;i<k;i++)
        {
            for(j=0;j<n;j++)
            {
                dp[i][j]=0;
                pos[i][j]=-1;
            }
        }
        ll z=1;
        dp[0][0]=v[0].r*v[0].r+save[0];
        pos[0][0]=v[0].r;
        for(j=1;j<n;j++)
        {
            for(i=0;i<=min(k-1,z);i++)
            {
                //current ka cost
                ll cost=v[j].r*v[j].r+save[j];
                ll res_cost=0;
                if(i>0)
                    res_cost=cost+dp[i-1][j-1]-(pos[i-1][j-1]*pos[i-1][j-1])+((pos[i-1][j-1]*pos[i-1][j-1])-(v[j].r*v[j].r));
                else
                    res_cost=cost;

//                cout<<" i "<<i<<" j "<<j<<" cost "<<cost<<" res -cost "<<res_cost<<endl;
                //has to be definately included
                if(dp[i][j-1]==0)
                {
                    dp[i][j]=res_cost;
                    pos[i][j]=v[j].r;
                }
                else
                {
                    //checking for included
                    if(res_cost>=dp[i][j-1])
                    {
                        dp[i][j]=res_cost;
                        pos[i][j]=v[j].r;
                    }
                    else
                    {
                        dp[i][j]=dp[i][j-1];
                        pos[i][j]=pos[i][j-1];
                    }
                }
            }
            z++;
        }

//        pm("print the dp array");
//        for(i=0;i<k;i++)
//        {
//            for(j=0;j<n;j++)
//            {
//                p(dp[i][j]);
//            }
//            pn();
//        }
        double ans=dp[k-1][n-1]*PI;
        cout<<"Case #"<<test<<": "<<setprecision(6)<<fixed<<ans<<endl;
    }
    return 0;
}
