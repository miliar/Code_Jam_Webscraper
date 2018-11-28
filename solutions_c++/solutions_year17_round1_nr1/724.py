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

#define MAX_N 100
char cake[MAX_N][MAX_N];
bool nonempty[MAX_N];

void solve() {
    PN();
    memset(nonempty, 0, sizeof(nonempty));
    int R, C;
    RI(R, C);
    REP(i, R) {
        scanf("%s", cake[i]);
        REP(j, C) {
            if(cake[i][j] != '?') {
                nonempty[i] = true;
            }
        }
    }

    int empty_cnt = 0;
    vector<pair<char, int> > tmp;
    REP(i, R) {
        if(nonempty[i]) {
            tmp.clear();
            REP(j, C) {
                if(cake[i][j] != '?') {
                    tmp.PB(MP(cake[i][j], j));
                }
            }
            tmp.PB(MP(tmp.back().first, C-1));
            REP(j, tmp.size()-1, -1, -1) {
                for(int k = tmp[j].second; (j == 0 and k >= 0) or k > tmp[j-1].second; k--) {
                    REP(l, i, i-empty_cnt-1, -1) {
                        cake[l][k] = tmp[j].first;
                    }
                }
            }
            empty_cnt = 0;
        } else {
            empty_cnt ++;
        }
    }
    if(empty_cnt > 0) {
        REP(j, tmp.size()-1, -1, -1) {
            for(int k = tmp[j].second; (j == 0 and k >= 0) or k > tmp[j-1].second; k--) {
                REP(l, R-1, R-empty_cnt-1, -1) {
                    cake[l][k] = tmp[j].first;
                }
            }
        }
    }
    REP(i, R) {
        printf("%s\n", cake[i]);
    }
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
