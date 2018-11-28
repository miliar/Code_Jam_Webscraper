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

#define MAX_N 1005
char s[MAX_N];
bool b[MAX_N];

void solve() {
    int k;
    scanf("%s%d", s, &k);
    int n = strlen(s);
    REP(i, n) {
        b[i] = (s[i] == '+')? true : false;
    }
    int cnt = 0;
    REP(i, n-k+1) {
        if(b[i]) {
            continue;
        }

        REP(j, i, i+k) {
            b[j] = !b[j];
        }
        cnt += 1;
    }
    REP(i, n-k+1, n) {
        if(!b[i]) {
            printf("IMPOSSIBLE\n");
            return;
        }
    }
    printf("%d\n", cnt);
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
