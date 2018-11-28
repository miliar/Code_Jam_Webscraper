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
#define MAXN (55)
#define INF (69696969)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<int, pii> piii;
typedef pair<int, piii> piiii;
typedef pair<ll, ll> pll;
typedef priority_queue<piiii, vector<piiii>, greater<piiii> > PQTYPE;

ld A[MAXN];
ld U;
ld sum;
ld Ans;
int T, N, K;

int main() {
    scanf("%d", &T); for(int t_i = 1; t_i <= T; t_i++) {
        scanf("%d%d", &N, &K);
        scanf("%Lf", &U);
        sum = 0;
        for(int i = 0; i < N; i++) scanf("%Lf", &A[i]);
        for(int i = 0; i < N; i++) sum += A[i];
        sort(A, A+N);
        int i = 0;
        for(i = N-1; i; i--) {
            if(A[i] * (i+1) <= U + sum) break;
            sum -= A[i];
        }
        sum = (U + sum) / (ld)(i+1);
        for(int j = 0; j <= i; j++) A[j] = sum;
        Ans = A[0]; for(int j = 1; j < N; j++) Ans *= A[j];
        printf("Case #%d: %.15Lf\n", t_i, Ans);
    }
    return 0;
}
