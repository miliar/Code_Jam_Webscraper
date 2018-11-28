//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<fstream>
#include<numeric>
#include<iomanip>
#include<bitset>
#include<list>
#include<stdexcept>
#include<functional>
#include<utility>
#include<ctime>
#include<cassert>
using namespace std;
#define RI(X) scanf("%d", &(X))
#define RLL(X) scanf("%lld", &(X))
#define DRI(X) int (X); scanf("%d", &X)
#define rep(i,a,n) for(int i=(a);i<(int)(n);i++)
#define repd(i,a,b) for(int i=(a);i>=(b);i--)
#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define MP make_pair
#define PB push_back
#define AA first
#define BB second
#define OP begin()
#define ED end()
#define SZ size()
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<PII> VPII;
typedef vector<PLL> VPLL;
#define cmin(x,y) x=min(x,y)
#define cmax(x,y) x=max(x,y)
const LL MOD = 1000000007;
const double PI = acos(-1.);
const double eps = 1e-9;
LL modPow(LL a,LL b,LL MOD){
    LL ret=1;for(;b;b>>=1){
        if(b&1)ret=ret*a%MOD;a=a*a%MOD;
    }return ret;
}

const int MXN = 105;
int E[MXN],S[MXN];
LL D[MXN][MXN];
int U[MXN],V[MXN];
void solve(){
    DRI(N);DRI(Q);
    rep(i,1,N+1){RI(E[i]);RI(S[i]);}
    rep(i,1,N+1)rep(j,1,N+1)RLL(D[i][j]);
    rep(i,0,Q){RI(U[i]);RI(V[i]);}
    rep(k,1,N+1)rep(i,1,N+1)rep(j,1,N+1)
        if(~D[i][k] and ~D[k][j]){
            if(~D[i][j])
                cmin(D[i][j],D[i][k]+D[k][j]);
            else D[i][j]=D[i][k]+D[k][j];
        }
    rep(i,0,Q){
        double t[MXN];
        int v[MXN];
        memset(v,0,sizeof v);
        int st=U[i],ed=V[i];
        v[st]=1;t[st]=0;
        priority_queue< pair<double,int> >Q;
        Q.push(MP(-t[st],st));
        while(!Q.empty()){
            pair<double,int> top = Q.top();
            //cout<<-top.AA<<" "<<top.BB<<"\n";
            Q.pop();
            int now = top.BB;
            rep(i,1,N+1)if(~D[now][i] and D[now][i]<=E[now]){
                double time=-top.AA+1.*D[now][i]/S[now];
                if(!v[i] or time<t[i]){
                    v[i]=1;
                    t[i]=time;
                    Q.push(MP(-t[i],i));
                }
            }
        }
        printf(" %.15f",t[ed]);
    }
    printf("\n");
}

int main(){
    int _T=1;
    scanf("%d",&_T);
    rep(CA,0,_T){
        printf("Case #%d:",CA+1);
        solve();
    }
    return 0;
}