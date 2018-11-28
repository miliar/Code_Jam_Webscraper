
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
lld x[64],y[64];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    x[0]=1;
    REP1(i,61) {x[i] = 1LL<<i;y[i]=x[i]-1;}
    int t;
    GN(t);
    REP1(tt,t) {
        lld n,k,mn,mx;
        cin>>n>>k;
        REP1(i,61) if(k<=y[i]) {
            n-=y[i-1];
            lld a,b,X,Y;
            X=n/x[i-1];Y=X+1;b=n%x[i-1];
            if(b>0 && k<=y[i-1]+b) {
                mn=mx=(Y-1)/2;
                if((Y-1)%2) mx+=1;
            }
            else {
                mn=mx=(X-1)/2;
                if((X-1)%2) mx+=1;
            }
            //cout<<n;
            //mx = (k <= (y[i-1]+(n%x[i]))) ? mn+1 : mn;
            break;
        }
        cout<<"Case #"<<tt<<": "<<mx<<" "<<mn<<endl;
    }
    return 0;
}
