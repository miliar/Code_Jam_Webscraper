#include<bits/stdc++.h>

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define FRI freopen("C-small-1-attempt0.in","r",stdin)
#define FRO freopen("C-small-1-attempt0.out","w",stdout)
#define debug(args...) {dbg,args; cerr<<endl;}
#define DB(x) #x"=>",x
#define RAD(x) ((x*PI)/180)
#define NEX(x) ((x)==n-1?0:(x)+1)
#define PRE(x) ((x)==0?n-1:(x)-1)
#define DEG(x) ((x*180)/PI)

#define EPS 1e-10
#define INF 1000000007
#define MOD 1000000007
#define MAXN 100005
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const double PI=acos(-1.0);

struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;

vector<LD>prob,cum;

void solve(int cas) {
    LD ans,p,lo,hi,target,u,mid,need,cnt;
    int n,k,i,j;
    cin>>n>>k;
    cin>>u;
    prob.clear();
    for(i=0;i<n;i++) {
        cin>>p;
        prob.PB(p);
    }
    sort(prob.begin(),prob.end());
    prob.PB(1);
    n++;
    cum.clear();
    cum.resize(n);
    cum[0]=prob[0];
    for(i=1;i<n;i++) {
        cum[i]=cum[i-1]+prob[i];
    }
    for(i=0;i<n;i++) {
        target=prob[i];
        need=target*i-cum[i-1];
        if(need>u) {
            break;
        }
    }
    lo=0;
    hi=target;
    cnt=0;
    while(hi-lo>EPS && cnt++<20000) {
        mid=(lo+hi)*0.5;
        need=mid*i-cum[i-1];
        if(need>u) {
            hi=mid;
        }
        else {
            lo=mid;
        }
    }
    ans=1;
    for(j=0;j<i;j++) {
        ans*=lo;
    }
    for(;i<n;i++) {
        ans*=prob[i];
    }
    cout<<"Case #"<<cas<<": "<<setprecision(8)<<fixed<<ans<<"\n";
}

int main() {
    FRI;
    FRO;
    int T,t=0;
    scanf("%d",&T);
    while(t++<T) {
        solve(t);
    }
    return 0;
}
