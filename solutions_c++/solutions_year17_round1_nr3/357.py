#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>
#define pb push_back
#define mp make_pair
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const double PI = acos(-1.0);
const double eps = 1e-6;
const int INF = 0x3f3f3f3f;
template <typename T>
inline bool scan_d (T &ret) {
    char c;
    int sgn;
    if (c = getchar(), c == EOF) return 0; //EOF
    while (c != '-' && (c < '0' || c > '9') ) c = getchar();
    sgn = (c == '-') ? -1 : 1;
    ret = (c == '-') ? 0 : (c - '0');
    while (c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + (c - '0');
    ret *= sgn;
    return 1;
}

int hd,ad,hk,ak,b,d;

int ans = INF;

void dfs(int cntd, int cntb)
{
    int tmphd = hd;
    int tmpad = ad;
    int tmphk = hk;
    int tmpak = ak;
    int cur = 0;
    bool dead = false;
    while(!dead)
    {
        ++cur;
        if(cur >= ans) break;
        if(cur <= cntd)
        {
            if(tmpak-d >= tmphd)
            {
                tmphd = hd;
                cntd++;
            }
            else
            {
                tmpak = max(tmpak-d,0);
            }
            tmphd -= tmpak;
        }
        else if(cur <= cntd+cntb)
        {
            if(tmpak >= tmphd)
            {
                tmphd = hd;
                cntb++;
            }
            else
            {
                tmpad += b;
            }
            tmphd -= tmpak;
        }
        else
        {
            if(tmpad >= tmphk)
            {
                tmphk = 0;
                break;
            }
            else if(tmpak >= tmphd)
            {
                tmphd = hd;
            }
            else
            {
                tmphk -= tmpad;
            }
            tmphd -= tmpak;

        }
        if(tmphd <= 0)
        {
            dead = true;
            break;
        }
    }
    if(!dead && ans > cur) ans = cur;
}

int main()
{
    //freopen("data.in","r",stdin);
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1; cas<=T; cas++)
    {
        scanf("%d%d%d%d%d%d",&hd,&ad,&hk,&ak,&b,&d);
        ans = 10000;
        if(d && b){
            for(int curd = 0; curd <= (ak/d)+1; curd++)
            {
                for(int curb = 0; curb <= (hk-ad)/b+1; curb++)
                {
                    dfs(curd,curb);
                }
            }
        }
        else if(d)
        {
            for(int curd = 0; curd <= (ak/d)+1; curd++)
            {
                dfs(curd,0);
            }
        }
        else if(b)
        {
            for(int curb = 0; curb <= (hk-ad)/b+1; curb++)
            {
                dfs(0,curb);
            }
        }
        else
        {
            dfs(0,0);
        }
        printf("Case #%d: ",cas);
        if(ans == 10000) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    return 0;
}
