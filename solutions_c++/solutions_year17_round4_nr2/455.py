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
        return d < o.d;
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

const int maxn = 1010;
int B[maxn],P[maxn],cnt[maxn];
vector<int> G[maxn];
priority_queue<HeapNode> Q;

int main()
{
    //freopen("data2.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T, N, M, C;
    scan_d<int>(T);
    for(int cas=1; cas<=T; cas++)
    {
        scanf("%d%d%d",&N,&C,&M);
        memset(cnt,0,sizeof(cnt));
        while(!Q.empty()) Q.pop();
        for(int i=1; i<=N; i++) G[i].clear();
        for(int i=0; i<M; i++)
        {
            scanf("%d%d",&P[i],&B[i]);
            G[P[i]].pb(B[i]);
        }
        int s = 0, mx = 0;
        int ans1 = 0;
        for(int i=1; i<=N; i++)
        {
            int siz = G[i].size();
            for(int j=0; j<siz; j++)
            {
                s++;
                cnt[G[i][j]]++;
                mx = max(mx,cnt[G[i][j]]);
            }
            int tmp = s/i;
            if(i*tmp != s) tmp++;
            ans1 = max(ans1,tmp);
            ans1 = max(ans1,mx);
        }
        int ans2 = 0;
        for(int i=1; i<=N; i++)
        {
            int siz = G[i].size();
            s = 0;
            for(int j=0; j<siz; j++)
            {
                s++;
            }
            if(s > ans1) ans2 += s-ans1;
        }
        printf("Case #%d: %d %d\n",cas,ans1,ans2);
    }
    return 0;
}
//g++ A.cpp -o A.o
