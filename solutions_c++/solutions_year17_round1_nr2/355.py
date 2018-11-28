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

const int maxn = 60;
int Q[maxn][maxn];
int N,P;
int R[maxn];
ll curR[maxn];
int a[maxn];

int main()
{
    //freopen("data.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1; cas<=T; cas++)
    {
        int mx = 0;
        scanf("%d%d",&N,&P);
        for(int i=1; i<=N; i++) scanf("%d",&R[i]);
        for(int i=1; i<=N; i++)
        {
            for(int j=1; j<=P; j++)
            {
                scanf("%d",&Q[i][j]);
                mx = max(Q[i][j]/R[i]+1,mx);
            }
            sort(Q[i]+1,Q[i]+P+1);
            a[i] = 1;
        }
        memset(curR,0,sizeof(curR));
        int ans = 0;
        for(int i=1; i<=mx; i++)
        {
            bool flag = true;
            for(int j=1; j<=N; j++)
            {
                if(a[j] > P)
                {
                    flag = false;
                    break;
                }
            }
            if(!flag) break;
            for(int j=1; j<=N; j++) curR[j] = 1LL*i*R[j];
            for(int j=1; j<=N; j++)
            {
                while(a[j] <= P && curR[j] * 0.9 > Q[j][a[j]])
                {
                    a[j]++;
                }
            }
            for(int j=1; j<=N; j++)
            {
                if(a[j] <= P && curR[j] * 0.9 <= 1.0*Q[j][a[j]] && curR[j] * 1.1 >= 1.0*Q[j][a[j]])
                {
                    ;
                }
                else{
                    flag = false;
                }
            }
            if(flag)
            {
                ans++;
                for(int j=1; j<=N; j++) a[j]++;
                --i;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
