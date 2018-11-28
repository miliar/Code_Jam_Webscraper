#include <bits/stdc++.h>
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define RFOR(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,A) FOR(I,0,A-1)
#define REP1(I,A) FOR(I,1,A)
#define PB push_back
#define MP make_pair
#define PI pair<lld,lld>
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

ld PII = 3.1415926535897L;
PI x[1010];
bool comp(PI a,PI b)
{
    //return ((a.A*a.A+2*a.B)<(b.A*b.A+2*b.B));
    return (a.B*a.A<b.B*b.A);
}
bool sel[1010];
bool rad[1000010];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    GN(t);
    REP1(tt,t) {
        int n,k;
        cin>>n>>k;
        REP(i,n) cin>>x[i].A>>x[i].B;//PRES(PII,9)<<endl;
        sort(x,x+n,comp);//REP(i,n) cout<<x[i].A<<" "<<x[i].B<<endl;
        //ld mx = 0;
        memset(sel,0,sizeof(sel));
        memset(rad,0,sizeof(rad));//cout<<"asa\n";
        lld ann=0,rr=0,cmm,rmm;
        //for(int i=0;i<=n-3;i++) for(int j=i+1;j<=n-2;j++) {
        int cnt=0;
        for(int i=n-1;i>=0;i--) {
            if(sel[i]) continue;
            cnt++;
            if(cnt==k) {
                sel[i] = true;
                rmm = max(rr,x[i].A);
                cmm = ann + rmm*rmm + 2*x[i].B*x[i].A;break;
            }
            ann += 2*x[i].B*x[i].A;
            //rad[x[i].A]=true;
            sel[i]=true;
            rr = max(rr,x[i].A);
            //cnt++;
        }
        //bool done = false;
        for(int i=0;i<n;i++) {
            if(sel[i]) continue;
            lld rmt = max(rr,x[i].A);
            lld cmt = ann+rmt*rmt+2*x[i].B*x[i].A;
            cmm=max(cmm,cmt);
        }
        cout<<"Case #"<<tt<<": ";
        PRES((cmm*PII),9);cout<<endl;
    }
    return 0;
}

