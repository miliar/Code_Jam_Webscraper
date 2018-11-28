#define DEB
#include<bits/stdc++.h>
#define REP(i,m) for(int i=0;i<(m);++i)
#define REPN(i,m,in) for(int i=(in);i<(m);++i)
#define ALL(t) (t).begin(),(t).end()
#define CLR(a) memset((a),0,sizeof(a))
#define pb push_back
#define mp make_pair
#define fr first
#define sc second

using namespace std;


#ifdef DEB
#define dump(x)  cerr << #x << " = " << (x) << endl
#define prl cerr<<"called:"<< __LINE__<<endl
#define dumpR(x) cerr<<"\x1b[31m"<<#x<<" = " <<(x)<<"\x1b[39m"<<endl
#define dumpY(x) cerr<<"\x1b[33m"<<#x<<" = " <<(x)<<"\x1b[39m"<<endl
#define dumpG(x) cerr<<"\x1b[32m"<<#x<<" = " <<(x)<<"\x1b[39m"<<endl
template<class T> void debug(T a,T b){ for(;a!=b;++a) cerr<<*a<<' ';cerr<<endl;}
#else
#define dump(x) ;
#define dumpR(x) ;
#define dumpY(x) ;
#define dumpG(x) ;
#define prl ;
template<class T> void debug(T a,T b){ ;}
#endif

template<class T> void chmin(T& a,const T& b) { if(a>b) a=b; }
template<class T> void chmax(T& a,const T& b) { if(a<b) a=b; }

typedef long long int lint;
typedef pair<int,int> pi;

namespace std{
  template<class S,class T>
  ostream &operator <<(ostream& out,const pair<S,T>& a){
    out<<'('<<a.fr<<','<<a.sc<<')';
    return out;
  }
}

//const int INF=5e8;
int n,P;

int ar[105];
typedef vector<int> vi;
map<vi,int> memo;
int rec(vi cur,int sum){
  if(memo.count(cur)) return memo[cur];

  int res=0;
  REP(i,P) if(cur[i]>0){
    --cur[i];
    chmax(res,rec(cur,(sum+i)%P)+(sum==0?1:0));
    ++cur[i];
  }
  memo[cur]=res;
  return res;
}
int main(){
  int T;cin>>T;
  for(int setn=1;setn<=T;++setn){
    printf("Case #%d: ",setn);
    cin>>n>>P;
    vi cnt(P);
    memo.clear();
    REP(i,n){
      cin>>ar[i];
      ar[i]%=P;
      ++cnt[ar[i]];
    }
    int add=cnt[0];
    cnt[0]=0;
    int res=rec(cnt,0)+add;
    cout<<res<<endl;
  }
  return 0;
}



