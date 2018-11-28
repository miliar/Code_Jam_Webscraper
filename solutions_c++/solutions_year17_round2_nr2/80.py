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

const int MXN = 100005;

int gao(vector<string>&L,int R,int G,string r,string g){
    if(G>=R and G)return 0;
    int rem = R-G-1;
    rep(i,0,rem)L.PB(string(r));
    string temp =r;
    rep(i,0,G){
        temp+=g;
        temp+=r;
    }
    if(rem>=0)
        L.PB(temp);
    return 1;
}

int two(string &ans,vector<string>r,vector<string>y){
    assert(sz(r)==sz(y));
    int l=sz(r);
    rep(i,0,l)ans+=r[i]+y[i];
    return 1;
}

int three(string &ans,vector<string>r,vector<string>y,vector<string>b){
    assert(sz(r)>=sz(y) and sz(r)>=sz(b) and sz(r)<=sz(y)+sz(b));
    int lr=sz(r),ly=sz(y),lb=sz(b);
    int iy=0,ib=0,ir=0;
    ans=r[ir++];
    while(ir<lr){
        if(lb-ib>ly-iy)
            ans+=b[ib++];
        else ans+=y[iy++];
        ans+=r[ir++];
    }
    if(lb-ib>ly-iy){
        ans+=b[ib++];
        assert(lb-ib==ly-iy);
        while(ib<lb and iy<ly){
            ans+=y[iy++];
            ans+=b[ib++];
        }
    }else if(ly-iy>lb-ib){
        ans+=y[iy++];
        assert(lb-ib==ly-iy);
        while(ib<lb and iy<ly){
            ans+=b[ib++];
            ans+=y[iy++];
        }
    }else {
        assert(lb-ib==ly-iy);
        while(ib<lb and iy<ly){
            ans+=b[ib++];
            ans+=y[iy++];
        }
    }
    
    assert(iy==ly and ib==lb and ir==lr);
    return 1;
}

int merge(string &ans,vector<string>r,vector<string>y,vector<string>b){
    int lr=sz(r),ly=sz(y),lb=sz(b);
    if(lr+ly==0 or lr+lb==0 or ly+lb==0)return 0;
    if(lb==0 and lr==ly)return two(ans,r,y);
    else if(lb==0)return 0;
    if(ly==0 and lr==lb)return two(ans,r,b);
    else if(ly==0)return 0;
    if(lr==0 and ly==lb)return two(ans,y,b);
    else if(lr==0)return 0;
    if(lb>=lr and lb>=ly ){
        if(lb<=lr+ly)
            return three(ans,b,r,y);
        else return 0;
    }
    if(lr>=ly and lr>=lb ){
        if(lr<=lb+ly)
            return three(ans,r,b,y);
        else return 0;
    }
    if(ly>=lr and ly>=lb ){
        if(ly<=lb+lr)
            return three(ans,y,b,r);
        else return 0;
    }
    return 0;
}
void solve(){
    DRI(N);
    DRI(R);
    DRI(O);
    DRI(Y);
    DRI(G);
    DRI(B);
    DRI(V);
    if(B==O and B+O==N){
        rep(i,0,B)printf("BO");
        printf("\n");
        return;
    }
    if(Y==V and Y+V==N){
        rep(i,0,Y)printf("YV");
        printf("\n");
        return;
    }
    if(R==G and R+G==N){
        rep(i,0,R)printf("RG");
        printf("\n");
        return;
    }
    vector<string>r,y,b;
    int valid = 1;
    valid = valid * gao(r,R,G,"R","G");
    valid = valid * gao(y,Y,V,"Y","V");
    valid = valid * gao(b,B,O,"B","O");
    string ans;
    valid = valid * merge(ans,r,y,b);
    if(valid){
        cout<<ans<<"\n";
    }else {
        cout<<"IMPOSSIBLE\n";
    }
}

int main(){
    int _T=1;
    scanf("%d",&_T);
    rep(CA,0,_T){
        printf("Case #%d: ",CA+1);
        solve();
    }
    return 0;
}
/*
100
10 3 0 3 0 4 0
10 5 0 5 0 0 0


 */