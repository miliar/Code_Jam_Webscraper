//OUM HARI OUM, OUM TATSAT
// OUM NAMA VAGABATE BASUDEBAY
// OUM NAMA MA SWARASATI OUM NAMA

#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<stdlib.h>
#include<iostream>
#include<algorithm>

#define sc1(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d %d",&a,&b)
#define sc3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define scd1(a) scanf("%lf",&a)
#define scd2(a,b) scanf("%lf %lf",&a,&b)
#define scd3(a,b,c) scanf("%lf %lf %lf",&a,&b,&c)
#define scl1(a) scanf("%lld",&a)
#define scl2(a,b) scanf("%lld %lld",&a,&b)
#define scl3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
//#define scl1(a) scanf("%I64d",&a)
//#define scl2(a,b) scanf("%I64d %I64d",&a,&b)
//#define scl3(a,b,c) scanf("%I64d %I64d %I64d",&a,&b,&c)


#define cl(vctr) vctr.clear()
#define ms(v, ar) memset(ar, v, sizeof(ar))

const double pi=(double)(2.0 * acos( 0.0 ));
const int inf=1 << 30;
const double eps=1E-9;
const double e = exp(1.0);
const int sz=10000000 + 5;

using namespace std;
typedef long long int ll;
const ll mod=1000000000 + 7;

ll ar[sz], cnt[sz], ar1[3], cnt1[3];

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("out.in", "w", stdout);

    ll t, T;
    ll N, K;
    ll a, b, n=0, c;
    map<ll, ll> mp;
    map<ll, ll> :: iterator it;

    scl1(t); T=t;
    while(t--)
    {
        scl2(N, K);

        ms(0, cnt);

        ar[1] = N; cnt[1] = 1; c = n = 1;
        while(1)
        {
            mp.clear();
            if(c==2)
            {
                a = (ar[n-1]&1) ? ar[n-1]/2 : (ar[n-1]-1)/2;
                b = ar[n-1]/2;
                mp[a]+=cnt[n - 1];
                mp[b]+=cnt[n - 1];
            }
            a = (ar[n]&1) ? ar[n]/2 : (ar[n]-1)/2;
            b = ar[n]/2;
            mp[a]+=cnt[n];
            mp[b]+=cnt[n];

            c=0;
            for(it=mp.begin(); it!=mp.end(); it++)
            {
                a = it->first;
                b = it->second;
                if(a<=0ll)
                    continue;
                ar1[c] = a, cnt1[c++] = b;
            }

            for(ll i=c-1; i>=0; i--)
            {
                ar[++n] = ar1[i], cnt[n] = cnt1[i];
            }

            if(c==0ll)
                break;
        }

        cnt[0] = 0;
        for(ll i=1; i<=n; i++)
        {
            //printf("-----%lld %lld\n", ar[i], cnt[i]);
            cnt[i] += cnt[i - 1];
            if(K<=cnt[i])
            {
                c = ar[i];
                break;
            }
        }

        a = (c&1) ? c/2 : (c-1)/2;
        b = c/2;

        printf("Case #%lld: %lld %lld\n", T-t, max(a, b), min(a, b));
    }

    return 0;
}

























