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
#define MAXN (1445)
#define INF (69696969)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<int, pii> piii;
typedef pair<int, piii> piiii;
typedef pair<ll, ll> pll;
typedef priority_queue<piiii, vector<piiii>, greater<piiii> > PQTYPE;
const ld pi = (ld)3.141592653589793238;

PQTYPE Q;
int d[MAXN>>1][2][MAXN];
bool A[MAXN], B[MAXN];
int T, N, M, Ans;

inline void ang(const int& sex) {
    for(; !Q.empty();) {
        const int t = Q.top().first, at = Q.top().second.first;
        const int y = Q.top().second.second.first, x = Q.top().second.second.second;
        Q.pop();
        if(1440 == x) { upmin(Ans, t + (y != sex)); continue; }
        if(0 == y) {
            if(A[x]) continue;
            if(at == 720) continue;
            if(t + 1 < d[at+1][1][x+1]) {
                d[at+1][1][x+1] = t+1;
                Q.push((piiii){t+1, {at+1, {1, x+1}}});
            }
            if(t < d[at+1][0][x+1]) {
                d[at+1][0][x+1] = t;
                Q.push((piiii){t, {at+1, {0, x+1}}});
            }
        } else {
            if(B[x]) continue;
            if(x-at == 720) continue;
            if(t < d[at][1][x+1]) {
                d[at][1][x+1] = t;
                Q.push((piiii){t, {at, {1, x+1}}});
            }
            if(t + 1 < d[at][0][x+1]) {
                d[at][0][x+1] = t + 1;
                Q.push((piiii){t+1, {at, {0, x+1}}});
            }
        }
    }
}
int main() {
    scanf("%d", &T); for(int t_i = 1; t_i <= T; t_i++) {
        scanf("%d%d", &N, &M);
        fill(A, A+MAXN, false); fill(B, B+MAXN, false);
        for(int a, b; N--;) {
            scanf("%d%d", &a, &b);
            for(int i = a; i < b; i++) A[i] = true;
        }
        for(int a, b; M--;) {
            scanf("%d%d", &a, &b);
            for(int i = a; i < b; i++) B[i] = true;
        }
        Ans = INF;
        PQTYPE().swap(Q);
        Q.push((piiii){0, {0, {0, 0}}});
        for(int i = 0; i < (MAXN>>1); i++) for(int j = 0; j < 2; j++) fill(d[i][j], d[i][j]+MAXN, INF);
        d[0][0][0] = 0;
        ang(0);

        PQTYPE().swap(Q);
        Q.push((piiii){0, {0, {1, 0}}});
        for(int i = 0; i < (MAXN>>1); i++) for(int j = 0; j < 2; j++) fill(d[i][j], d[i][j]+MAXN, INF);
        d[0][1][0] = 0;
        ang(1);

        printf("Case #%d: %d\n", t_i, Ans);
    }
    return 0;
}
