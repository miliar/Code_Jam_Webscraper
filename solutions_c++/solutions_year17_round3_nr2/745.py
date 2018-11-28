#include <iostream>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <tuple>
#include <algorithm>
#include <functional>
#include <cstring>
#include <limits.h>

#define FOR(i,k,n)  for (int i=(k); i<(int)(n); ++i)
#define REP(i,n)    FOR(i,0,n)
#define FORIT(i,c)	for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define SZ(i) ((int)i.size())
#define pb          push_back
#define mp          make_pair
#define mt          make_tuple
#define ALL(X)      (X).begin(),(X).end()
#define ft          first
#define sd          second
typedef long long LL;

using namespace std;
int N;
vector<pair<pair<int,int>, int> > A;

int solve(){
    int change=0;
    int free=0;
    vector<int> nonfree[2];
    int t0=0,t1=0;
    // printf("N=%d\n",N);
    REP(i,N){
        // printf("A=((%d,%d),%d)\n",A[i].ft.ft,A[i].ft.sd,A[i].sd);
        if(A[i].sd==0)
            t0+=A[i].ft.sd-A[i].ft.ft;
        else
            t1+=A[i].ft.sd-A[i].ft.ft;

        int a=A[i].ft.sd;
        int b=A[(i+1)%N].ft.ft;
        if(A[i].sd==A[(i+1)%N].sd){
            nonfree[A[i].sd].pb((b-a<0)?b+1440-a:b-a);
        }else{
            change++;
            free+=(b-a<0)?b+1440-a:b-a;
        }
    }
    int g0=720-t0,g1=720-t1;

    sort(ALL(nonfree[0]));
    REP(i,SZ(nonfree[0])){
        if(nonfree[0][i] <= g0){
            g0-=nonfree[0][i];
        }else{
            g0=0;
            change+=2;
        }
    }
    if(g0<=free)
        return change;
    g0-=free;

    sort(ALL(nonfree[1]));
    reverse(ALL(nonfree[1]));
    REP(i,SZ(nonfree[1])){
        if(nonfree[1][i] <= g0){
            change+=2;
            g0-=nonfree[1][i];
        }else{
            g0=0;
            change+=2;
        }
        if(g0==0)
            return change;
    }
}

int main(void){
    int T;
    scanf("%d",&T);
    REP(i,T){
        int nc,nd;
        scanf("%d%d",&nc,&nd);
        N=nc+nd;
        A.clear();
        REP(j,nc){
            int a,b;
            scanf("%d%d",&a,&b);
            A.pb(mp(mp(a,b),0));
        }
        REP(j,nd){
            int a,b;
            scanf("%d%d",&a,&b);
            A.pb(mp(mp(a,b),1));
        }
        sort(ALL(A));
        printf("Case #%d: %d\n",i+1,solve());
    }
    return 0;
}

