#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pi;
const int MAXN = 60;
int TC, N, P;
int R[MAXN];
priority_queue<int, vector<int>, greater<int> > pq[MAXN];
int main() {
    scanf("%d", &TC);
    for (int Txn = 1; Txn <= TC; ++Txn) {
        scanf("%d%d", &N, &P);
        for (int i = 0; i < N; ++i) scanf("%d", &R[i]);
        int nxt = 0;
        for (int i = 0; i < N; ++i) {
            for (int j = 0, x; j < P; ++j) {
                scanf("%d", &x);
                x *= 10;
                pq[i].push(x);
            }
            nxt = max(nxt, pq[i].top()/(11*R[i]));
        }
        //printf("nxt = %d\n", nxt);
        int ans = 0;
        bool pass = 1;
        while (pass) {
            bool ok = 1;
            for (int i = 0; i < N && ok; ++i) {
                while (!pq[i].empty()) {
                    if (nxt*R[i]*9 > pq[i].top()) pq[i].pop();
                    else break;
                }
                if (pq[i].empty()) {
                    pass = 0;
                    ok = 0;
                    break;
                }
                if (nxt*R[i]*11 < pq[i].top())  ok = 0;
            }
            if (ok) {
                ++ans;
                for (int i = 0; i < N; ++i) {
                    pq[i].pop();
                    if (pq[i].empty()) pass = 0;
                    else {
                        nxt = max(nxt, pq[i].top()/(11*R[i]));
                    }
                }
            }
            else if (pass) {
                ++nxt;
                //assert(0);
                //printf("wtf %d?\n", nxt);
            }
        }
        
    
        printf("Case #%d: ", Txn);
        printf("%d\n", ans);
        
        for (int i = 0; i < N; ++i) {
            while (!pq[i].empty()) pq[i].pop();
        }
    }
}