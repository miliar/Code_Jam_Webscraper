
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
#define Read freopen("in2.in","r",stdin)
#define Write freopen("out2.txt","w",stdout)
#define __ std::ios_base::sync_with_stdio (false),cin.tie(0),cout.tie(0)

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

string s="RYB",im="IMPOSSIBLE";

void go(vector<pair<int,int> > v,int n)
{
    int d=v[2].fs-v[1].fs;
    if(d>v[0].fs) {
        cout<<im<<"\n";
    }
    else{

        string t;
        for(int i=0;i<d;i++){
            t.psb(s[v[0].sc]);
            t.psb(s[v[2].sc]);
        }
        v[0].fs-=d;
        v[2].fs-=d;
        d=v[0].fs;
        for (int i=0;i<d;i++)
        {
            t.psb(s[v[0].sc]);
            t.psb(s[v[1].sc]);
            t.psb(s[v[2].sc]);
        }
        for(int i=0;i<SZ(v);i++){
            v[i].fs-=d;
        }
        d=v[1].fs;
        for (int i=0;i<d;i++)
        {
            t.psb(s[v[1].sc]);
            t.psb(s[v[2].sc]);
        }
        if(SZ(t)!=n || t[0]==t[n-1])
        {
            cout<<im<<"\n";
        }
        else cout<<t<<"\n";
    }
}

int main()
{
    #ifdef MAHDI
    Read;
    Write;
    #endif // MAHDI
    int t,n,cas=0;
    sf("%d",&t);
    while(t--){
        int a,b,c,x,y,z;
        cin>>n>>a>>x>>b>>y>>c>>z;
        vector<pair<int,int> > val;
        if(a) val.psb(mp(a,0));
        if(b) val.psb(mp(b,1));
        if(c) val.psb(mp(c,2));
        sort(all(val));
        cout<<"Case #"<<++cas<<": ";
        if(SZ(val)==1){
            if(val[0].fs>1){
                cout<<im<<"\n";
            }
            else{
                cout<<s[val[0].sc]<<"\n";
            }
        }
        else if(SZ(val)==2){
            if(val[1].fs-val[0].fs>0){
                cout<<im<<"\n";
            }
            else{
                for(int i=0;i<val[0].fs+val[1].fs;i++)
                {
                    cout<<s[val[!(i&1)].sc];
                }
                cout<<"\n";
            }
        }
        else if(SZ(val)==3){
            go(val,n);
        }
        else assert(true);
    }
    return 0;
}














