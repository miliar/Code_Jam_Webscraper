#include <string>
#include <vector>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<functional>
#include<list>
#include<deque>
#include<bitset>
#include<set>
#include<map>
#include<unordered_map>
#include<unordered_set>
#include<cstring>
#include<sstream>
#include<complex>
#include<iomanip>
#include<numeric>
#include<cassert>
#define X first
#define Y second
#define pb push_back
#define rep(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define reps(X,S,Y) for (int (X) = S;(X) < (Y);++(X))
#define rrep(X,Y) for (int (X) = (Y)-1;(X) >=0;--(X))
#define repe(X,Y) for ((X) = 0;(X) < (Y);++(X))
#define peat(X,Y) for (;(X) < (Y);++(X))
#define all(X) (X).begin(),(X).end()
#define rall(X) (X).rbegin(),(X).rend()
#define eb emplace_back
#define UNIQUE(X) (X).erase(unique(all(X)),(X).end())
#define Endl endl

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
template<class T> using vv=vector<vector<T>>;
template<class T> ostream& operator<<(ostream &os, const vector<T> &t) {
os<<"{"; rep(i,t.size()) {os<<t[i]<<",";} os<<"}"<<endl; return os;}
template<class S, class T> ostream& operator<<(ostream &os, const pair<S,T> &t) { return os<<"("<<t.first<<","<<t.second<<")";}
template<class T> inline bool MX(T &l,const T &r){return l<r?l=r,1:0;}
template<class T> inline bool MN(T &l,const T &r){return l>r?l=r,1:0;}
#define out(args...){vector<string> a_r_g_s=s_p_l_i_t(#args, ','); e_r_r(a_r_g_s.begin(), args); }
vector<string> s_p_l_i_t(const string& s, char c) { vector<string> v; stringstream ss(s); string x; while(getline(ss,x,c)) v.emplace_back(x); return move(v);}
void e_r_r(vector<string>::iterator it) {}
template<typename T, typename... Args> void e_r_r(vector<string>::iterator it, T a, Args... args){ if(*it==" 1"||*it=="1") cerr<<endl; else cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << ", "; e_r_r(++it, args...);}
const ll MOD=1e9+7;

typedef pair<pll,ll> plll;

inline void ins(set<plll> &st,ll l,ll x,ll r,bool f){
  if(f){
    st.erase(plll(pll(min(r-x,x-l),max(r-x,x-l)),-x));
  }else{
    st.emplace(pll(min(r-x,x-l),max(r-x,x-l)),-x);
  }
}
inline void ins(set<plll> &st,ll l,ll r,bool f=0){
  ins(st,l,(l+r)/2,r,f);
  ins(st,l,(l+r+1)/2,r,f);
}

int main(){
  ios_base::sync_with_stdio(false);
  cout<<fixed<<setprecision(0);
  int T;
  cin>>T;
  rep(kase,T){
    ll n,t;
    cin>>n>>t;
    set<ll> usd{0,n+1};
    set<plll> cand;
    ins(cand,0,n+1);
    pll re;
    rep(i,t){
      //for(auto p:cand) cout<<p;cout<<endl;
      plll p=*cand.rbegin();
      ll x=-p.Y;
      re=p.X;
      auto r=usd.upper_bound(x);
      auto l=r; --l;
      ins(cand,*l,*r,true);
      //out(p,*l,*r,1);
      ins(cand,*l,x);
      ins(cand,x,*r);
      usd.insert(x);
      //rep(j,n+2) cout<<".0"[usd.count(j)];cout<<endl;
    }
    cout<<"Case #"<<kase+1<<": "<<re.Y-1<<" "<<re.X-1<<endl;
  }
  return 0;
}
