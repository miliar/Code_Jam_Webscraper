#include<bits/stdc++.h>

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define FRI freopen("C-small-2-attempt0.in","r",stdin)
#define FRO freopen("C-small-2-attempt0.out","w",stdout)
#define debug(args...) {dbg,args; cerr<<endl;}
#define DB(x) #x"=>",x
#define RAD(x) ((x*PI)/180)
#define NEX(x) ((x)==n-1?0:(x)+1)
#define PRE(x) ((x)==0?n-1:(x)-1)
#define DEG(x) ((x*180)/PI)

#define EPS 1e-12
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

class Range {
public:
    int l,r;
    Range() {}
    Range(int l,int r) : l(l), r(r) {}
    Range(const Range &rng) : l(rng.l), r(rng.r) {}
    bool operator < (const Range &rng) const {
        if(r-l<rng.r-rng.l) return true;
        else if (r-l>rng.r-rng.l) return false;
        else return l>rng.l;
    }
    pair<int,int>SplitNInsert(priority_queue<Range> &q) {
        int sz;
        pair<int,int>ret=MP(0,0);
        if(r-l+1>2) {
            sz=(r-l)/2;
            q.push(Range(l,l+sz-1));
            ret.F=sz;
        }
        if(r-l+1>1) {
            sz=(r-l+1)/2;
            q.push(Range(r-sz+1,r));
            ret.S=sz;
        }
        return ret;
    }
};

void solve(int &kase) {
    int i,n,k;
    pair<int,int>ans;
    priority_queue<Range>q;
    Range rng;
    scanf("%d %d",&n,&k);
    q.push(Range(0,n-1));
    for(i=0;i<k;i++) {
        rng=q.top();
        q.pop();
        ans=rng.SplitNInsert(q);
    }
    printf("Case #%d: %d %d\n",++kase,max(ans.F,ans.S),min(ans.F,ans.S));
}

int main() {
    FRI;
    FRO;
    int t=0,T;
    scanf("%d",&T);
    while(t<T) {
        solve(t);
    }
    return 0;
}
