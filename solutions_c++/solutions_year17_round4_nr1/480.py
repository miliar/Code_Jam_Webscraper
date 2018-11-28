#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <limits.h>
#define pb push_back
#define mp make_pair
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const int inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3fLL;

struct HeapNode{
    int id,d;
    HeapNode(){}
    HeapNode(int id,int d):id(id),d(d){}
    bool operator < (const HeapNode &o) const
    {
        return d > o.d;
    }
};

template <class T>
inline bool scan_d(T &ret)
{
    char c;
    int sgn;
    if (c = getchar(), c == EOF)
    {
        return 0; //EOF
    }
    while (c != '-' && (c < '0' || c > '9'))
    {
        c = getchar();
    }
    sgn = (c == '-') ? -1 : 1;
    ret = (c == '-') ? 0 : (c - '0');
    while (c = getchar(), c >= '0' && c <= '9')
    {
        ret = ret * 10 + (c - '0');
    }
    ret *= sgn;
    return 1;
}

const int maxn = 110;
int vis[4];

int main()
{
    //freopen("data.in","r",stdin);
    //freopen("data.out","w",stdout);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T, N, P;
    scan_d<int>(T);
    for(int cas=1; cas<=T; cas++)
    {
        scan_d(N);
        scan_d(P);
        for(int i=0; i<P; i++) vis[i] = 0;
        for(int i=0, x; i<N; i++)
        {
            scan_d(x);
            x %= P;
            vis[x]++;
        }
        int ans = vis[0];
        if(P == 2)
        {
            ans += vis[1]/2;
            if(vis[1]&1) ans++;
        }
        else if(P == 3)
        {
            if(vis[1] < vis[2]) swap(vis[1],vis[2]);
            ans += vis[2];
            vis[1] -= vis[2];
            ans += vis[1]/3;
            if(vis[1]%3 != 0) ans++;
        }
        else
        {
            //cout<<vis[0]<<" "<<vis[1]<<" "<<vis[2]<<" "<<vis[3]<<endl;
            ans += vis[2]/2;
            if(vis[2]&1)
            {
                if(vis[1]==vis[3]) ans++, vis[2] = 0;
                else if(vis[1] > vis[3])
                {
                    vis[1]--, vis[3]++, vis[2] = 0;
                }
                else
                {
                    vis[3]--, vis[1]++, vis[2] = 0;
                }
            }
            if(vis[1] < vis[3])
            {
                swap(vis[1],vis[3]);
            }
            ans += vis[3];
            vis[1] -= vis[3];
            ans += vis[1]/4;
            if(vis[1]%4 != 0) ans++;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
//g++ A.cpp -o A.o
