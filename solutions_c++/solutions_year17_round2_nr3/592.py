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
#define taskname "C"
const ll inf=10000000000000;
typedef long double db;
ll e[101];
ll s[101];
ll f[101][101];
db ans[101];
bool done[101];
ll t, n, q;
struct cmp{
    bool operator () (pair <int, db> a, pair <int, db> b){
        return a.second>b.second;
    }
};
priority_queue <pair <int, db>, vector <pair<int, db> >, cmp> heap;
int main(){
    #ifdef I_have_no_girlfriend
        if(fopen(taskname".inp", "r"))
            freopen(taskname".inp", "r", stdin);
    #endif // I_have_no_girlfriend
    freopen(taskname".in", "r", stdin);
    freopen(taskname".out", "w", stdout);
    read(t);
    FOR(itest, 1, t){
        read(n);
        read(q);
        FOR(i, 1, n){
            read(e[i]);
            read(s[i]);
        }
        FOR(i, 1, n)
            FOR(j, 1, n){
                read(f[i][j]);
                if(f[i][j]==-1)
                    f[i][j]=inf;
            }
        FOR(k, 1, n)
            FOR(i, 1, n)
                FOR(j, 1, n)
                    f[i][j]=min(f[i][j], f[i][k]+f[k][j]);
        cout<<"Case #"<<itest<<":";
        FOR(query, 1, q){
            int a, t;
            read(a);
            read(t);
            FOR(i, 1, n){
                ans[i]=inf;
                done[i]=0;
            }
            ans[a]=0;
            while(!heap.empty())
                heap.pop();
            heap.push(mp(a, 0));
            while(!heap.empty()){
                pair <int, db> top=heap.top();
                heap.pop();
                a=top.first;
                if(ans[a]<top.second) continue;
                done[a]=1;
                FOR(i, 1, n){
                    if(!done[i]){
                        if(f[a][i]<=e[a]){
                            db cost=ans[a]+((db)(f[a][i]))/s[a];
                            if(cost<ans[i]){
                                ans[i]=cost;
                                heap.push(mp(i, ans[i]));
                            }
                        }
                    }
                }
            }
            cout<<' '<<setprecision(8)<<fixed<<ans[t];
        }
        cout<<'\n';
    }
}