#include <iostream>
#include <fstream>
#include <sstream>
#include <string.h>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <set>

#define for0(i,n) for (int i=0; i<n; i++)
#define forr(i,n) for (int i=n-1; i>=0; i--)
#define fori(i,a,b) for (int i=a; i<=b; i++)
#define iter(c,x) for(x::iterator it=c.begin(); it!=c.end(); it++)
#define vec(x) vector< x >
#define pb push_back
#define ms(a,z) memset(a,z,sizeof(a));
#define mp make_pair
#define nl cout<<"\n";
#define pr(x) cout<<(x)<<" ";
#define prl(x) cout<<#x " = "<<x<<endl;
#define prp(x) cout<<"("<<(x).first<<" "<<(x).second<<") ";
#define printv(v) {for(int _=0; _<size(v); _++) cout<<v[_]<<" "; cout<<"\n";}
#define printa(a,s) {for (int _=0; _<s; _++) cout<<a[_]<<" "; cout<<"\n";}
#define print2D(a,m,n) {for (int _=0; _<m; _++) {for (int __=0; __<n; __++) cout<<a[_][__]<<" "; cout<<"\n";} cout<<"\n";}
#define debug cout<<"ok at line "<<__LINE__<<endl;
#define X first
#define Y second
#define sqr(x) 1LL*(x)*(x)
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define all(a) a.begin(),a.end()
#define size(x) (int)(x).size()
#define read(x) int x; scanf("%d",&x);

using namespace std;

typedef long long ll;

const int INF = 999999999;
const long long INFL = 99999999999999999LL;
const double EPSILON = 0.00000001;
const long long MOD = 1000000007;

int mem[110][110][110][110];

int Hd, Ad, Hk, Ak, B, D;

int solve(short hd, short ad, short hk, short ak) {
    if (hk <= 0)
        return 0; //win
    else if (hd <= 0)
        return INF; //lose
    else if (mem[hd][ad][hk][ak] >= 0) {
        return mem[hd][ad][hk][ak];
    }

    assert(hd <= 100 && ad <= 100 && hk <= 100 && ak <= 100);
    short next_hd, next_ad, next_hk, next_ak;
    int best=INF, res;
    mem[hd][ad][hk][ak] = INF; //state being explored - don't return to it

    //attack
    res = solve(hd-ak, ad, hk-ad, ak)+1;
    best = min(best,res);

    //buff
    if (ad < hk) {
        next_ad = min(hk, ad+B);
        res = solve(hd-ak, next_ad, hk, ak)+1;
        best = min(best,res);
    }

    //cure
    if (hd < Hd) {
        res = solve(Hd-ak, ad, hk, ak)+1;
        best = min(best,res);
    }

    //debuff
    if (ak > 0) {
        next_ak = max(0,ak-D);
        res = solve(hd-next_ak, ad, hk, next_ak)+1;
        best = min(best,res);
    }

    mem[hd][ad][hk][ak] = best;
    return best;
}

int main()
{
    freopen("C_small_2.in","r",stdin);
    freopen("C.out","w",stdout);


    int cases;
    scanf("%d",&cases);
    for (int casen=0; casen<cases; casen++){
        printf("Case #%d: ",casen+1);
        cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
        ms(mem,-1);
        /*for0(a,110)
            for0(b,110)
                for0(c,110)
                    for0(d,110)*/
        int res = solve(Hd, Ad, Hk, Ak);
        if (res < INF)
            cout<<res<<endl;
        else
            cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
