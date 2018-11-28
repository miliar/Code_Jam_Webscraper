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
ll d, n;
ll t;
struct horse{
    ll k, s;
    bool operator <(horse b){
        return (k<b.k)||(k==b.k&&s<b.s);
    }
} h[1001];
typedef long double db;
int main(){
//    #ifdef I_have_no_girlfriend
//        if(fopen(taskname".inp", "r"))
//            freopen(taskname".inp", "r", stdin);
//    #endif // I_have_no_girlfriend
    freopen(taskname".in", "r", stdin);
    freopen(taskname".out", "w", stdout);
    read(t);
    FOR(itest, 1, t){
        read(d);
        read(n);
        FOR(i, 1, n){
            read(h[i].k);
            read(h[i].s);
        }
        db time=0;
        FOR(i, 1, n)
            time=max(time, ((db)(d-h[i].k))/h[i].s);
        time=(db)(d)/time;
        cout<<"Case #"<<itest<<": "<<setprecision(6)<<fixed<<time<<'\n';
    }
}