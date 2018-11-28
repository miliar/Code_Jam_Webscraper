#include <bits/stdc++.h>
#define rep(i,n) for(__typeof(n) i=0;i<n;++i)
#define reu(i,s,e) for(__typeof(e) i=s;i<e;++i)
#define each(it,o) for(auto it= (o).begin(); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x7fffffff
#define INFL 0x7fffffffffffffffLL
#define inrep int t;cin>>t; while(t--)
const double PI = 3.141592653589793;
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<string> vs;
typedef map<int,int> mii;
typedef map<ll,ll> mll;

template<typename T> ostream& operator<< (ostream &o,vector<T> v){
    if (v.size()>0)	o<<v[0];
    for (unsigned i=1;i<v.size();i++)	o<<" "<<v[i];
    return o<<endl;
}
template<typename U,typename V> ostream& operator<< (ostream &o,pair<U,V> p){
    return o<<"("<<p.first<<", "<<p.second<<") ";
}
template<typename T> istream& operator>> (istream &in,vector<T> &v){
    for (unsigned i=0;i<v.size();i++)	in>>v[i];
    return in;
}

int t;
int N,k,r,h;
vpii pc;
double dp[1005][1005];
double mpc(int k,int n,int top){
    if(k==0 || n>=N) return 0;
    // if(dp[k][n]!=0) return dp[k][n];
    double area=0,ca;
    ca=PI*(pc[n].F)*(pc[n].F+2*pc[n].S);
    if(top!=-1) ca-=PI*(pc[top].F)*(pc[top].F);
    area=max(mpc(k,n+1,top),mpc(k-1,n+1,n)+ca);
    // dp[k][n]=area;
    return area;
}
int main(){
      freopen("A-small-attempt0.in","r",stdin);
      freopen("A-small.out","w",stdout);
      // freopen("A-large.in","r",stdin);
      // freopen("A-large.out","w",stdout);
      cin>>t;
      rep(testcase,t){
        cout<<"Case #"<<testcase+1<<": ";
        cin>>N>>k;
        rep(i,N){
          cin>>r>>h;
          pc.pb(mp(r,h));
        }
        sort(all(pc));
        mset(dp,0);
        cout.precision(10);
        cout<<fixed<<mpc(k,0,-1);
        cout<<"\n";
        pc.clear();
      }
      return 0;
}
