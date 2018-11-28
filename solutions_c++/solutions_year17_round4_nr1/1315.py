#include <bits/stdc++.h>
using namespace std;
#define FOR(i, j, k) for(int i=j; i<=k; i++)
#define DFOR(i, j, k) for(int i=j; i>=k; i--)
#define bug(x) cerr<<#x<<" = "<<x<<'\n'
#define pb push_back
#define mp make_pair
typedef long long ll;
template <typename T> inline void read(T &x){
    char c;
    bool nega=0;
    while((!isdigit(c=getchar()))&&(c!='-'));
    if(c=='-'){
        nega=1;
        c=getchar();
    }
    x=c-48;
    while(isdigit(c=getchar()))
        x=x*10+c-48;
    if(nega)
        x=-x;
}
template <typename T> inline void writep(T x){
    if(x>9) writep(x/10);
    putchar(x%10+48);
}
template <typename T> inline void write(T x){
    if(x<0){
        putchar('-');
        x=-x;
    }
    writep(x);
}
template <typename T> inline void writeln(T x){
    write(x);
    putchar('\n');
}
#define taskname "A"
int cnt[4];
int f[101][101][101][4];
int t;
int itest;
int n, g, p;
inline void update(int &x, int y){
    x=(x>y)?x:y;
}
int main(){
//    #ifdef I_have_no_girlfriend
//        if(fopen(taskname".in", "r"))
//            freopen(taskname".in", "r", stdin);
//    #endif // I_have_no_girlfriend
    freopen(taskname".in", "r", stdin);
    freopen(taskname".out", "w", stdout);
    read(t);
    for(itest=1; itest<=t; itest++){
        read(n);
        read(p);
        DFOR(i, 3, 0)
            cnt[i]=0;
        FOR(i, 1, n){
            read(g);
            cnt[g%p]++;
        }
        FOR(i, 0, cnt[1])
            FOR(j, 0, cnt[2])
                FOR(k, 0, cnt[3])
                    FOR(d, 0, 3)
                        f[i][j][k][d]=-1000000;
        f[cnt[1]][cnt[2]][cnt[3]][0]=0;
        DFOR(i, cnt[1], 0)
            DFOR(j, cnt[2], 0)
                DFOR(k, cnt[3], 0){
                    DFOR(d, p-1, 1){
                        if(k>0)
                            update(f[i][j][k-1][(d-3+p)%p], f[i][j][k][d]);
                        if(j>0)
                            update(f[i][j-1][k][(d-2+p)%p], f[i][j][k][d]);
                        if(i>0)
                            update(f[i-1][j][k][(d-1+p)%p], f[i][j][k][d]);
                    }
                    if(i>0)
                        update(f[i-1][j][k][p-1], f[i][j][k][0]+1);
                    if(j>0)
                        update(f[i][j-1][k][p-2], f[i][j][k][0]+1);
                    if(k>0)
                        update(f[i][j][k-1][p-3], f[i][j][k][0]+1);
                }
        int ans=0;
        FOR(d, 0, 3)
            ans=max(ans, f[0][0][0][d]);
        printf("Case #%d: %d\n", itest, cnt[0]+ans);
    }
}