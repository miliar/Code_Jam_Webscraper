#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <string.h>
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
typedef priority_queue<int, vector<int>, greater<int>> PQTYPE;

vector<pii> V; // {idx, costomer}
int fckingCosLine[MAXN];
int Lcnt[MAXN];
int T, N, C, M, LN, Ans;

inline int getLine() {
    int S = *max_element(fckingCosLine+1, fckingCosLine+C+1), E = MAXN;
    PQTYPE Q;
    for(int mid; S < E;) {
        mid = (S+E)>>1; PQTYPE().swap(Q);
        for(int i = 0; i < mid; i++) Q.push(1);
        bool flag = false;
        for(const pii& v : V) {
            const int t = Q.top();
            if(t <= v.first) {
                Q.pop(); Q.push(t+1);
            } else {
                flag = true; break;
            }
        }
        if(flag) S = mid+1;
        else E = mid;
    }
    return S;
}
int main() {
    scanf("%d", &T); for(int t_i = 1; t_i <= T; t_i++) {
        vector<pii>().swap(V); fill(fckingCosLine, fckingCosLine+MAXN, 0);
        fill(Lcnt, Lcnt+MAXN, 0);
        for(scanf("%d%d%d", &N, &C, &M); M--;) {
            int a, b; scanf("%d%d", &a, &b);
            V.pb({a, b});
            fckingCosLine[b]++; Lcnt[a]++;
        }
        sort(allv(V));
        LN = getLine();

        Ans = 0;
        for(int i = 1; i <= N; i++) {
            if(Lcnt[i] <= LN) continue;
            Ans += Lcnt[i] - LN;
        }
        
        printf("Case #%d: %d %d\n", t_i, LN, Ans);
    }
    return 0;
}
