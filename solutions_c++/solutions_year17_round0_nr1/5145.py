#include<bits/stdc++.h>

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define FRI freopen("A-large.in","r",stdin)
#define FRO freopen("A-large.out","w",stdout)
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

char s[1005];

void solve(int &kase) {
    int i,j,k,ans=0;
    scanf("%s %d",s,&k);
    for(i=0;i<strlen(s);i++) {
        if(s[i]=='+') {
            continue;
        }
        if(i+k-1>=strlen(s)) {
            printf("Case #%d: IMPOSSIBLE\n",++kase);
            return;
        }
        ans++;
        for(j=0;j<k;j++) {
            if(s[i+j]=='+') {
                s[i+j]='-';
            }
            else {
                s[i+j]='+';
            }
        }
    }
    printf("Case #%d: %d\n",++kase,ans);
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
