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

string brute(int n){
  string res;
  for(int i=1;i<=n;++i){
    stringstream ss;ss<<i;
    string s=ss.str();
    bool ok=true;
    REP(j,s.size()-1){
      if(s[j]>s[j+1]) ok=false;
    }
    if(ok) res=s;
  }
  return res;
}
int main(){
  int T;cin>>T;
  for(int setn=1;setn<=T;++setn){
    string s;
    cin>>s;
    string res;
    int n=s.size();
    for(int i=0;i<n-1;++i){
      if(s[i]>s[i+1]){
        char d=s[i];
        int j;
        for(j=i;j>=0 && s[j]==d;--j) --s[j];
        j+=2;
        for(;j<n;++j) s[j]='9';
        res=s;
        break;
      }
    }
    if(res.empty()) res=s;
    while(res[0]=='0') res.erase(res.begin());
    if(res.size()<=n-1) res=(string(n-1,'9'));

    printf("Case #%d: %s\n",setn,res.c_str());
  }
  return 0;
}



