#include <sstream>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <complex>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <string>
#include <utility>
#include <vector>
#include <algorithm>
#include <bitset>
#include <list>
#include <string.h>
#include <assert.h>
#include <time.h>

using namespace std;

#define SZ(x) ((int)x.size())
#define all(a) a.begin(),a.end()
#define allr(a) a.rbegin(),a.rend()
#define clrall(name,val) memset(name,(val),sizeof(name))
#define EPS 1e-9
#define ll long long
#define ull long long unsigned
#define SF scanf
#define PF printf
#define sf scanf
#define pf printf
#define psb(b) push_back((b))
#define ppb() pop_back()
#define oo (1<<28)
#define inf 0x3f3f3f3f
#define mp make_pair
#define mt make_tuple
#define get(a,b) get<b>(a)
#define fs first
#define sc second
#define Read freopen("in3.txt","r",stdin)
#define Write freopen("out3.txt","w",stdout)
#define __ std::ios_base::sync_with_stdio (false),cin.tie(0),cout.tie(0)
#define csprint cout<<"Case #"<<++cas<<": "

ll MulModL(ll B,ll P,ll M) {    ll R=0; while(P>0)      { if((P&1ll)==1) { R=(R+B); if(R>=M) R-=M; } P>>=1ll; B=(B+B); if(B>=M) B-=M; } return R; }

ll MulModD(ll B, ll P,ll M) {   ll I=((long double)B*(long double)P/(long double)M);    ll R=B*P-M*I; R=(R%M+M)%M;  return R; }

ll BigMod(ll B,ll P,ll M) {     ll R=1; while(P>0)      { if(P%2==1) { R=(R*B)%M; } P/=2; B=(B*B)%M; } return R; } /// (B^P)%M

ll BigModML(ll B,ll P,ll M) {     ll R=1; while(P>0)      { if(P%2==1) { R=MulModL(R,B,M); } P/=2; B=MulModL(B,B,M); } return R; } /// (B^P)%M

template<class T1> void deb(T1 e1){cout<<e1<<"\n";}
template<class T1,class T2> void deb(T1 e1,T2 e2){cout<<e1<<" "<<e2<<"\n";}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3){cout<<e1<<" "<<e2<<" "<<e3<<"\n";}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<"\n";}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<"\n";}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<"\n";}
template<class T1,class T2,class T3,class T4,class T5,class T6,class T7> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6,T7 e7){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<" "<<e7<<"\n";}

//int dx[]= {-1,-1,0,0,1,1};
//int dy[]= {-1,0,-1,1,0,1};
//int dx[]= {0,0,1,-1};/*4 side move*/
//int dy[]= {-1,1,0,0};/*4 side move*/
//int dx[]= {1,1,0,-1,-1,-1,0,1};/*8 side move*/
//int dy[]= {0,1,1,1,0,-1,-1,-1};/*8 side move*/
//int dx[]={1,1,2,2,-1,-1,-2,-2};/*night move*/
//int dy[]={2,-2,1,-1,2,-2,1,-1};/*night move*/

int EQ(long double x) {
    if(fabs(x)<EPS) return 0;
    else if(x>0) return 1;
    else return -1;
}

const int MAXN=1009;

int mark[MAXN];

typedef pair<int,int> pii;
typedef vector<pii> vpii;

void print(vpii &v){
    for(int i=0;i<SZ(v);i++){
        deb(v[i].fs,v[i].sc);
    }
    return ;
}

bool cmp(const pii& a,const pii& b){
    return a>b;
}

map<int,vpii> dp;

vpii rec(int n){
//    deb(n);
//    getchar();
    if(n==1) {
        vpii v={mp(0,0)};
        return v;
    }
    else if(n==0){
        vpii v;
        return v;
    }
    if(dp.count(n)) return dp[n];
    int l=(n-1)>>1;
    int r=(n-1)-l;
    vpii lv=rec(l);
    vpii rv=rec(r);
    vpii v(n-1),ret(n);
    ret[0]=mp(r,l);
    merge(all(lv),all(rv),v.begin(),cmp);
    for(int i=0;i<SZ(v);i++){
        ret[i+1]=v[i];
    }
//    deb("::::::::");
//    print(lv);
//    deb("::::::::");
//    deb("########");
//    print(rv);
//    deb("########");
//    deb("********");
//    print(ret);
//    deb("********");
    dp[n]=ret;
    return ret;
}


void go(int n,int k){
    clrall(mark,0);
    mark[0]=1;
    mark[n+1]=1;
    int l,r,p,mx,mn,t;
    for(int i=1;i<=k;i++)
    {
        p=-1;
        for(int j=1;j<=n;j++){
            if(mark[j]) continue;
            l=r=0;
            t=j-1;
            while(t>=0 && !mark[t--]) l++;
            t=j+1;
            while(!mark[t++]) r++;
            if(p==-1){
                p=j,mn=min(l,r),mx=max(l,r);
            }
            else if(mn<min(l,r)){
                p=j,mn=min(l,r),mx=max(l,r);
            }
            else if(mn==min(l,r)){
                if(mx<max(l,r)){
                    p=j,mn=min(l,r),mx=max(l,r);
                }
            }
        }
        mark[p]=1;
        assert(p!=-1);
        deb(mx,mn);
    }
//    deb(mx,mn);
    return ;
}

void solve(ll n,ll k){
    if(n<=1){
        deb(0,0);
        return ;
    }
    ll l=(n-1)>>1ll;
    ll r=(n-1)-l;
    if(k==1){
        deb(r,l);
        return ;
    }
    k--;
    ll p=k/2ll;
    if(k&1ll){
        solve(r,k-p);
    }
    else {
        solve(l,p);
    }
    return ;
}

int main()
{
    #ifdef MAHDI
    Read;
    Write;
    #endif // MAHDI
//    for(int i=5;i<=20;i++){
//        deb(":::::::::::::::::::::::");
////        go(i,i);
////        cerr<<i<<endl;
//        vpii v=rec(i);
//        for(int i=0;i<SZ(v);i++){
//            deb(v[i].fs,v[i].sc);
//        }
//        deb(":::::::::::::::::::::::");
//    }

//    return 0;

    int t;
    ll n,k;
    cin>>t;
    vpii v;
    int cas=0;
    while(t--){
        cin>>n>>k;
        csprint;
//        go(n,k);
//        v=rec(n);
//        deb(v[k-1].fs,v[k-1].sc);
        solve(n,k);
    }
    return 0;
}















