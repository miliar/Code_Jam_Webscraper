// #pragma comment(linker,"/STACK:102400000,102400000")
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

#include <string>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <fstream>
// #include <unordered_set>

using namespace std;

#define FF first
#define SS second
#define MP make_pair
#define PB push_back
#define lson rt << 1, l, mid
#define rson rt << 1 | 1, mid + 1, r
#define FOR(i, n, m) for(int i = n; i <= m; i++)
#define REP(i, n, m) for(int i = n; i >= m; i--)
#define ll long long

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL, LL> PLL;
typedef unsigned long long ULL;

const int maxn = 110;
int N, Q;
int E[maxn], S[maxn];
int dist[maxn][maxn];
LL dend[maxn];
double ans;

void Dfs(int id, int left, int speed, double total){
    if(id == N) {
        ans = min(ans, total);
        return;
    }
    if(left < dist[id][id+1] || (E[id] >= left && S[id] >= speed) || (S[id] > speed && E[id] >= dend[id])) {
        Dfs(id+1, E[id]-dist[id][id+1], S[id], total + 1.0*dist[id][id+1]/S[id]);
    }else{
        Dfs(id+1, left-dist[id][id+1], speed, total + 1.0*dist[id][id+1]/speed);
        Dfs(id+1, E[id]-dist[id][id+1], S[id], total + 1.0*dist[id][id+1]/S[id]);
    }
}

int main(){
        freopen("C-small-attempt2.in", "r", stdin);
        freopen("C-small2.out", "w", stdout);
        int T;
        cin >> T;
        int cas = 0;
        while(T--){
            cas++;
            cin >> N >> Q;
            FOR(i, 1, N) cin >> E[i] >> S[i];
            FOR(i, 1, N){
                FOR(j, 1, N) cin >> dist[i][j];
            }
            dend[N] = 0;
            for(int i = N-1; i >= 1; i --) dend[i] = dend[i+1] + dist[i][i+1];
            int s, t;
            printf("Case #%d: ", cas);
            while(Q--){
                cin >> s >> t;
                ans = dend[1];
                Dfs(2, E[1]-dist[1][2], S[1], dist[1][2]*1.0/S[1]);
                printf("%.8f\n", ans);
            }

            }
        return 0;
        }
