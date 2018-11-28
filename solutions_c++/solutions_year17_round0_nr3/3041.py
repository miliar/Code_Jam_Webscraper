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
    ll tt=1;
    ll cnt = 1e19;
    while(t--)
    {
        ll n,k;
        sc(n);
        sc(k);
        map<ll,ll> m;
        set<ll> s;
        m[n]=1;
        s.insert(cnt-n);
        ll tp,tp1,tp2;
        while(1)
        {
            auto it = s.begin();
            tp = cnt-(*it);
            s.erase(it);
            if(tp==0)
            break;
            tp1 = (tp-1)/2;
            tp2 = (tp-1)-tp1;
            if(tp1 == tp2)
            {
                m[tp1]+=(2*m[tp]);
                s.insert(cnt-tp1);
            }
            else
            {
                m[tp1]+=m[tp];
                m[tp2]+=m[tp];
                s.insert(cnt-tp1);
                s.insert(cnt-tp2);
            }
        }
        n = m.size();
        ll ar1[n],ar2[n];
        ll i = 1;
        for(auto it = m.begin();it!=m.end();it++)
        {
            ar1[n-i]= it->first;
            ar2[n-i]= it->second;
            i++;
        }
        for(ll i=0;i<n;i++)
        {
            k-=ar2[i];
            if(k<=0)
            {
                tp1 = (ar1[i]-1)/2;
                tp2 = (ar1[i]-1)-tp1;
                break;
            }
        }
        if(tp1<tp2)
        {
            tp = tp1;
            tp1 = tp2;
            tp2 = tp;
        }
        printf("Case #%lld: %lld %lld\n",tt,tp1,tp2);
        tt++;
    }
    return 0;
}