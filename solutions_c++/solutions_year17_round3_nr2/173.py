#include<bits/stdc++.h>

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define Cameron 0
#define Jaime 1

#define FRI freopen("B-large.in","r",stdin)
#define FRO freopen("B-large.out","w",stdout)
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

vector<int>gap[2];
vector< pair< pair<int,int>,int > >schedules;

void solve(int cas) {
    int cam,jam,i,s,e,n,camGot=0,jamGot=0,ans=0;

    gap[Cameron].clear();
    gap[Jaime].clear();
    schedules.clear();

    cin>>cam>>jam;
    for(i=0;i<cam;i++) {
        cin>>s>>e;
        schedules.PB(MP(MP(s,e),Cameron));
    }
    for(i=0;i<jam;i++) {
        cin>>s>>e;
        schedules.PB(MP(MP(s,e),Jaime));
    }

    sort(schedules.begin(),schedules.end());
    n=cam+jam;
    for(i=0;i<n;i++) {
        if(schedules[i].S==Cameron) {
            jamGot+=schedules[i].F.S-schedules[i].F.F;
            if(i>0&&schedules[i-1].S==schedules[i].S) {
                jamGot+=schedules[i].F.F-schedules[i-1].F.S;
                gap[Jaime].PB(schedules[i].F.F-schedules[i-1].F.S);
            }
        }
        else {
            camGot+=schedules[i].F.S-schedules[i].F.F;
            if(i>0&&schedules[i-1].S==schedules[i].S) {
                camGot+=schedules[i].F.F-schedules[i-1].F.S;
                gap[Cameron].PB(schedules[i].F.F-schedules[i-1].F.S);
            }
        }
        if(i>0&&schedules[i-1].S!=schedules[i].S) {
            ans++;
        }
    }

    if(ans&1) {
        ans++;
    }
    else {
        if(schedules[0].S==Cameron) {
            jamGot+=1440-schedules[n-1].F.S+schedules[0].F.F;
            gap[Jaime].PB(1440-schedules[n-1].F.S+schedules[0].F.F);
        }
        else {
            camGot+=1440-schedules[n-1].F.S+schedules[0].F.F;
            gap[Cameron].PB(1440-schedules[n-1].F.S+schedules[0].F.F);
        }
    }
    assert(jamGot<=720||camGot<=720);
    if(jamGot>720) {
        sort(gap[Jaime].begin(),gap[Jaime].end());
        reverse(gap[Jaime].begin(),gap[Jaime].end());
        for(i=0;i<gap[Jaime].size();i++) {
            jamGot-=gap[Jaime][i];
            ans+=2;
            if(jamGot<=720) {
                break;
            }
        }
        assert(jamGot<=720);
    }
    else if(camGot>720) {
        sort(gap[Cameron].begin(),gap[Cameron].end());
        reverse(gap[Cameron].begin(),gap[Cameron].end());
        for(i=0;i<gap[Cameron].size();i++) {
            camGot-=gap[Cameron][i];
            ans+=2;
            if(camGot<=720) {
                break;
            }
        }
        assert(camGot<=720);
    }
    cout<<"Case #"<<cas<<": "<<ans<<"\n";
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
