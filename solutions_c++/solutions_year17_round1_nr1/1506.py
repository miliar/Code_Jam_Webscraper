#include <bits/stdc++.h>
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define RFOR(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,A) FOR(I,0,A-1)
#define REP1(I,A) FOR(I,1,A)
#define PB push_back
#define MP make_pair
#define PI pair<int,int>
#define A first
#define B second
#define GN(a) scanf("%d",&a)
#define MEM(a,b) memset(a,b,sizeof a)
#define MEM0(a) MEM(a,0)
#define MOD (1000000007)
#define VI vector<int>
#define PRES(a,b) cout<<std::setprecision(b)<<std::fixed<<a
#define FOREACH(it, l) for (auto it = l.begin(); it != l.end(); it++)

////for(auto &xx:vv) cout<<xx;

//int __builtin_popcount
//long int __builtin_popcountl
//long long __builtin_popcountll
//int __builtin_ctz Returns the number of trailing 0-bits in x, starting at the least significant bit position. If x is 0, the result is undefined
//

using namespace std;
typedef long long int lld;
typedef long double ld;

char xx[30][30];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    GN(t);
    REP1(tt,t) {
        int r,c;
        cin>>r>>c;
        REP(i,r) REP(j,c) {
            cin>>xx[i][j];
        }
        REP(i,r) REP(j,c) {
            if(xx[i][j]=='?' && j>0) xx[i][j] = xx[i][j-1];
        }
        REP(i,r) RFOR(j,c-1,0) {
            if(xx[i][j]=='?' && j<c-1) xx[i][j] = xx[i][j+1];
        }
        REP(i,r) REP(j,c) {
            if(xx[i][j]=='?' && i>0) xx[i][j] = xx[i-1][j];
        }
        RFOR(i,r-1,0) REP(j,c) {
            if(xx[i][j]=='?' && i<r-1) xx[i][j] = xx[i+1][j];
        }
        cout<<"Case #"<<tt<<":\n";
        REP(i,r) {REP(j,c) {
            cout<<xx[i][j];
        }cout<<endl;}
    }
    return 0;
}
