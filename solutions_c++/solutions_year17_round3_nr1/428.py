#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#define pb push_back
#define sz(V) ((int)(V).size())
#define allv(V) ((V).begin()),((V).end())
#define befv(V) ((V)[(sz(V)-2)])
#define upmin(ans,ansx) (ans)=min((ans),(ansx))
#define upmax(ans,ansx) (ans)=max((ans),(ansx))
#define MAXN (1005)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
const ld pi = (ld)3.141592653589793238;
struct Node { ll r, h; void init() { scanf("%lld%lld", &r, &h); } };

ll d[MAXN][MAXN];
Node nodes[MAXN];
set<ll> Q;
ll Ans;
int T, N, K;

int main() {
    scanf("%d", &T); for(int t_i = 1; t_i <= T; t_i++) {
        scanf("%d%d", &N, &K);
        for(int i = 1; i <= N; i++) nodes[i].init();
        sort(nodes+1, nodes+N+1, [&](const Node& a, const Node& b) -> bool {
            return a.r > b.r;
        });
        for(int i = 1; i <= N; i++) d[i][1] = nodes[i].r * nodes[i].r + 2ll*nodes[i].r*nodes[i].h;
        for(int j = 2; j <= K; j++) {
            set<ll>().swap(Q);
            for(int i = j; i <= N; i++) {
                Q.insert(d[i-1][j-1]);
                auto sex = Q.end(); sex--;
                d[i][j] = (*sex) + 2ll*nodes[i].r*nodes[i].h;
            }
        }
        Ans = 0;
        for(int i = K; i <= N; i++) upmax(Ans, d[i][K]);
        printf("Case #%d: %.15Lf\n", t_i, (ld)Ans * pi);
    }
    return 0;
}
