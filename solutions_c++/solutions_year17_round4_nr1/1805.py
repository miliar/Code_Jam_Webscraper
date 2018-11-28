#include <bits/stdc++.h>
using namespace std;

#define GET_MACRO(_1,_2,_3,_4,NAME,...) NAME
#define REP2(i,n) for(int i=0;i<(int)(n);i++)
#define REP3(i,m,n) for(int i=m;i<(int)(n);i++)
#define REP4(i,m,n,s) for(int i=m;(s>0 and i<(int)(n)) or (s<0 and i>(int)(n));i+=s)
#define REP(...) GET_MACRO(__VA_ARGS__, REP4, REP3, REP2)(__VA_ARGS__)
#define REPIT(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define PIS(x) printf("%d ",x)
#define PRINTIA(a,n) REP(i,n){printf("%d ", *((a)+i));}putchar('\n');
#define PN() putchar('\n')
#define MP make_pair
#define PB push_back

typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;

void RI() {}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}
void PI() {putchar('\n');}
template<typename... T>
void PI(const int head, T... tail ) {
    printf("%d ", head);
    PI(tail...);
}

#define MAX_N 200
int G[5];

void solve() {
    memset(G, 0, sizeof(G));
    int N, P;
    RI(N, P);
    REP(i, N) {
        int g;
        RI(g);
        G[g % P] += 1;
    }
    int ans = 0;
    ans += G[0];

    if(P == 2) {
        ans += G[1] / 2 + G[1] % 2;
    } else if(P == 3) {
        int m12 = min(G[1], G[2]);
        ans += m12;
        G[1] -= m12;
        G[2] -= m12;
        if(G[1] > 0) {
            ans += G[1] / 3;
            if(G[1] % 3 > 0) {
                ans += 1;
            }
        } else if(G[2] > 0) {
            ans += G[2] / 3;
            if(G[2] % 3 > 0)
                ans += 1;
        }
    } else if(P == 4) {
        ans += G[2] / 2;
        G[2] = G[2] % 2;
        int m13 = min(G[1], G[3]);
        ans += m13;
        G[1] -= m13;
        G[3] -= m13;
        if(G[2] == 0) {
            if(G[1] > 0) {
                ans += G[1] / 4;
                if(G[1] % 4 > 0)
                    ans += 1;
            } else if(G[3] > 0) {
                ans += G[3] / 4;
                if(G[3] % 4 > 0)
                    ans += 1;
            }
        } else if(G[2] == 1) {
            if(G[1] > 0) {
                int s = 2 + G[1];
                ans += s / 4;
                if(s % 4 > 0)
                    ans += 1;
            } else if(G[3] > 0) {
                if(G[3] <= 2) {
                    ans += 1;
                } else {
                    ans += (G[3]-2) / 4 + 1;
                    if((G[3]-2) % 4 > 0)
                        ans += 1;
                }
            }
        }
    }
    PI(ans);
}

int main()
{
    int T;
    RI(T);
    REP(i, T) {
        printf("Case #%d: ", i+1);
        solve();
    }

    return 0;
}
