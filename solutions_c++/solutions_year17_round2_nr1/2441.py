
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

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    GN(t);
    REP1(tt,t) {
        int d,n;
        cin>>d>>n;
        ld tm = 0;
        REP1(i,n) {
            ld k,s;
            cin>>k>>s;
            tm = max(tm,(d-k)/s);
        }
        cout<<"Case #"<<tt<<": ";
        PRES((d/tm),8);
        cout<<endl;
    }
    return 0;
}
