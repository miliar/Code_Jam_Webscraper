//marico el que lo lea
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;

#define FOR(i,f,t) for(int i=f;i<(int)t; i++)
#define FORR(i,f,t) for(int i=f;i>(int)t; i--)
#define ms(obj, val) memset(obj, val, sizeof(obj))
#define ms2(obj, val, sz) memset(obj, val, sizeof(obj[0])*sz)
#define pb push_back
#define ri(x) scanf("%d",&x)
#define rii(x,y) ri(x), ri(y)

typedef vector<int> vi;
typedef long long ll;

const int INF = 0x3f3f3f3f;

int B, D, Hd;
int calc(int hd, int ad, int hk, int ak, int NB, int NDB){
    int ret = 0;
    while(NDB){
        int nak = max(0, ak-D);
        int nhd = hd - nak;
        if(nhd <= 0){
            if(hd == Hd-ak){
                return INF;
            }else{
                ret++;
                hd=Hd-ak;
            }
        }else{
            NDB--;
            ret++;
            ak = nak;
            hd = nhd;
        }
    }
    while(NB){
        int nad = ad+B;
        int nhd = hd - ak;
        if(nhd <= 0){
            if(hd == Hd-ak){
                return INF;
            }else{
                ret++;
                hd=Hd-ak;
            }
        }else{
            NB--;
            ret++;
            ad = nad;
            hd = nhd;
        }
    }
    while(true){
        int nhk = hk - ad;
        int nhd = hd - ak;
        if(nhk <= 0){
            return ret+1;
        }
        if(nhd <= 0){
            if(hd == Hd-ak){
                return INF;
            }else{
                hd=Hd-ak;
                ret++;
            }
        }else{
            hk = nhk;
            hd = nhd;
            ret++;
        }
    }
}


int main(){
    int TC; ri(TC);
    FOR(tc,1,TC+1){
        int ad, hk, ak;
        rii(Hd, ad); rii(hk, ak); rii(B,D);
        int ans = INF;
        FOR(nbuff,0,120)FOR(ndebuff,0,120){
            ans = min(ans, calc(Hd, ad, hk, ak, nbuff, ndebuff));
        }
        if(ans == INF){
            printf("Case #%d: IMPOSSIBLE\n",tc);
        }else{
            printf("Case #%d: %d\n",tc,ans);
        }
    }
}
