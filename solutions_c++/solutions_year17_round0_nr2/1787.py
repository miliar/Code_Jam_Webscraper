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
const double eps=1E-9;
const double e = exp(1.0);
const int sz=100000 + 5;

using namespace std;
typedef long long int ll;
const ll mod=1000000000 + 7;
const ll inf=1ll << 60;

char N[23];
ll N1[23], ln, dp[23][11][3], pw[23];

ll rec(ll pos, ll prv, bool se)
{
    if(pos>ln)
        return -inf;
    if(!se && N1[pos]<prv)
        return -inf;

    ll &res = dp[pos][prv][se], tmp;
    if(res!=-1ll)
        return res;

    res = -inf;
    ll upto = !se ? N1[pos] : 9ll;
    for(ll dgt = prv; dgt<=upto; dgt++)
    {
        tmp = rec(pos+1, dgt, se|(dgt<N1[pos]));
        if(pos<ln)
            tmp = pw[pos]*dgt + tmp;
        else
            tmp = dgt;
        res = max(res, tmp);
    }

    return res;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.in", "w", stdout);

    int t, T;
    sc1(t); T=t;
    while(t--)
    {
        scanf("%s", &N);
        ln = strlen(N);

        for(ll i=ln, p=1ll; i>0; i--, p*=10ll)
        {
            N1[i] = N[i - 1] - '0';
            pw[i] = p;
        }

        ms(-1, dp);
        ll res = -inf;
        for(ll dgt=0ll; dgt<=N1[1]; dgt++)
        {
            ll tmp = rec(2, dgt, dgt<N1[1]);
            if(ln>1)
                tmp = pw[1]*dgt + tmp;
            else
                tmp = dgt;
            res = max(res, tmp);
        }

        printf("Case #%d: %lld\n", T - t, res);
    }

    return 0;
}

























