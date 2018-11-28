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
int n;
int R,O,Y,G,B,V;

string ans;
bool solve(){
  if(B+O==n){
    if(B==O){
      REP(i,B) ans+="BO";
      return true;
    }
    return false;
  }
  if(R+G==n){
    if(R==G){
      REP(i,R) ans+="RG";
      return true;
    }
    return false;
  }
  if(Y+V==n){
    if(Y==V){
      REP(i,Y) ans+="YV";
      return true;
    }
    return false;
  }
  if((O>0 && B<O+1) || (G>0 && R<G+1) || (V>0 && Y<V+1)) return false;
  B-=O;R-=G;Y-=V;
  if(B>R+Y || R>B+Y || Y>R+B) return false;

  char col[]="RYB";
  int ar[3];
  ar[0]=R*2;ar[1]=Y*2;ar[2]=B*2;

  int lef,rig;
  if(R){
    ans="R";
    lef=rig=0;
  }else if(B){
    ans="B";
    lef=rig=2;
  }else if(Y){
    ans="Y";
    lef=rig=1;
  }else{
    assert(false);
  }
  REP(i,R+B+Y-1){
    assert((*max_element(ar,ar+3))*2<=accumulate(ar,ar+3,0));
    int mx=-1;
    REP(j,3) if(j!=lef && (mx==-1 || ar[mx]<ar[j])){
      mx=j;
    }
    ans+=col[mx];
    --ar[lef];
    --ar[mx];
    lef=mx;
  }
  if(O){
    REP(i,ans.size()) if(ans[i]=='B'){
      string tmp="B";
      REP(j,O) tmp+="OB";
      ans.replace(i,1,tmp);
      break;
    }
  }
  if(G){
    REP(i,ans.size()) if(ans[i]=='R'){
      string tmp="R";
      REP(j,G) tmp+="GR";
      ans.replace(i,1,tmp);
      break;
    }
  }
  if(V){
    REP(i,ans.size()) if(ans[i]=='Y'){
      string tmp="Y";
      REP(j,V) tmp+="VY";
      ans.replace(i,1,tmp);
      break;
    }
  }
  return true;
}
int main(){
  int T;cin>>T;
  for(int setn=1;setn<=T;++setn){
    printf("Case #%d: ",setn);
    cin>>n>>R>>O>>Y>>G>>B>>V;
    vector<int> want={R,O,Y,G,B,V};
    ans.clear();
    bool ret=solve();

    if(!ret) puts("IMPOSSIBLE");
    else{
      char code[]="ROYGBV";
      int cnt[6]={0};
      REP(i,ans.size()) REP(j,6) if(ans[i]==code[j]) ++cnt[j];
      REP(i,6) assert(want[i]==cnt[i]);
      vector<int> ar;
      REP(i,ans.size()) REP(j,6) if(code[j]==ans[i]) ar.pb(j);
      REP(i,ar.size()){
        int dif=ar[i]-ar[(i+1)%n];
        dif=(dif+6)%6;
        assert(dif==3 || ((dif==2 || dif==4) && ar[i]%2==0));
      }
      cout<<ans<<endl;
    }
  }
  return 0;
}



