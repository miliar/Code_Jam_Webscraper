#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define MODV 1000000007

typedef long long ll;
typedef double dbl;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pi;
void addmod(int &a, ll b){a=(a+b); if(a>=MODV)a-=MODV;}
void mulmod(int &a, ll b){a=(a*b)%MODV;}
template<class T>bool domin(T &a, const T &b){return a>b?a=b,1:0;}
template<class T>bool domax(T &a, const T &b){return a<b?a=b,1:0;}
int gi(){int a;scanf("%d",&a);return a;}
ll gll(){ll a;scanf("%lld",&a);return a;}

void doit() {
  int hm=gi(), am=gi(), ho=gi(), ao=gi(), b=gi(), d=gi();
  set<pair<pi,pi>> st;
  queue<pair<pi,pi>> q;
  queue<int> cnt;
  int ans=MODV;
  q.push({{hm,am},{ho,ao}});
  st.insert({{hm,am},{ho,ao}});
  cnt.push(0);


  for(int i=0;i<1000000 && q.size()>0;i++){
    pair<pi,pi> t=q.front();
    int sf=cnt.front();
    q.pop();
    cnt.pop();
    int thm=t.fi.fi, tam=t.fi.se, tho=t.se.fi, tao=t.se.se;
    int nr=(tho-1)/tam + 1;
    if(tao*(nr-1)<thm){
      ans=min(ans,sf+nr);
    }
    if(thm>tao){
      //attack
      {
        int nhm=thm-tao,nam=tam,nho=tho-tam,nao=tao;
        if(nho>0){
        pair<pi,pi> nkey = {{nhm,nam},{nho,nao}};
        if(st.find(nkey)==st.end()){
          q.push(nkey);
          st.insert(nkey);
          cnt.push(sf+1);
        }
        }
      }

      //buff
      {
        int nhm=thm-tao,nam=tam+b,nho=tho,nao=tao;
        pair<pi,pi> nkey = {{nhm,nam},{nho,nao}};
        if(st.find(nkey)==st.end()){
          q.push(nkey);
          st.insert(nkey);
          cnt.push(sf+1);
        }
      }
    }else{
      if(hm>tao){
        //cure
        int nhm=hm-tao, nam=tam, nho=tho, nao=tao;
        pair<pi,pi> nkey = {{nhm,nam},{nho,nao}};
        if(st.find(nkey)==st.end()){
          q.push(nkey);
          st.insert(nkey);
          cnt.push(sf+1);
        }
      }
    }
    //reduce opp
    if(thm>tao-d){
      int nam=tam, nho=tho, nao=tao-d;
      if(nao<0)nao=0;
      int nhm=thm-nao;
      pair<pi,pi> nkey = {{nhm,nam},{nho,nao}};
      if(st.find(nkey)==st.end()){
        q.push(nkey);
        st.insert(nkey);
        cnt.push(sf+1);
      }
    }
  }


  if(ans==MODV){
    printf("IMPOSSIBLE");
  }else{
    printf("%d",ans);
  }

}

int main() {
  int tc=gi();
  for(int i=1;i<=tc;i++){
    printf("Case #%d: ",i);
    doit();
    puts("");
  }
  return 0;
}
