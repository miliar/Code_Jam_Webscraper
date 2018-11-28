#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<array>
#include<vector>
#include<map>
#include<utility>
#include<bitset>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<utility>
using namespace std;
typedef long long ll;
typedef long double ld;
#define mod 1000000007
#define vec vector<long long>
#define arl(n) array<long long,n>
#define ard(n) array<double,n>
#define sc(n) scanf("%lld",&n)
#define prn(n) printf("%lld\n",n)
#define prs(n) printf("%lld ",n)
#define pr() printf("\n")
#define pb push_back
#define mp make_pair
int main()
{
    ll t;
    sc(t);
    for(ll ii=1;ii<=t;ii++)
    {
        ll n,m;
        sc(n),sc(m);
        vec v;
        ll tp;
        for(ll i=0;i<n;i++)
        {
            sc(tp);
            v.pb(tp);
        }
        const ll mxn = 1e6+7;
        array<multiset<ll>,mxn> va[n];
        for(ll i=0;i<n;i++)
        {
            for(ll j=0;j<m;j++)
            {
                sc(tp);
                ll tp1 = tp;
                ll low = 0,high = 1e6;
                ll min1 = -1,min2 = -1;
                while(low<=high)
                {
                    ll mid = (low+high)/2;
                    ll m1 = v[i]*mid*(0.9);
                    ll m2 = v[i]*mid*(1.1);
                    if(m2>=tp && m1<=tp)
                    {
                        high = mid-1;
                        min1 = mid;
                    }
                    else if(m1>tp)
                    high = mid-1;
                    else
                    low = mid+1;
                }
                if(min1 != -1)
                {
                    low = 0,high = 1e6;
                    while(low<=high)
                    {
                        ll mid = (low+high)/2;
                        ll m1 = v[i]*mid*(0.9);
                        ll m2 = v[i]*mid*(1.1);
                        if(m2>=tp && m1<=tp)
                        {
                            low = mid+1;
                            min2 = mid;
                        }
                        else if(m1>tp)
                        high = mid-1;
                        else
                        low = mid+1;
                    }
                    //cout<<tp<<" "<<min1<<" "<<min2<<endl;
                    for(ll k=min1;k<=min2;k++)
                    va[i][k].insert(tp1);
                }
            }
        }
        ll ans=0;
        for(ll i=1;i<=(1e6);i++)
        {
            while(va[0][i].size()>0)
            {
                bool b=0;
                if(n>1)
                {
                    for(ll j=1;j<n;j++)
                    {
                        if(va[j][i].size()==0)
                        {
                            b=1;
                            break;
                        }
                    }
                }
                if(!b)
                {
                    ans++;
                    for(ll j=0;j<n;j++)
                    {
                        auto it = va[j][i].begin();
                        tp = *it;
                        for(ll k = i;k<(1e6+7);k++)
                        {
                            auto it1 = va[j][k].find(tp);
                            if(it1 == va[j][k].end())
                            break;
                            else
                            va[j][k].erase(it1);
                        }
                    }
                }
                else
                break;
            }
        }
        printf("Case #%lld: %lld\n",ii,ans);
    }
    return 0;
}