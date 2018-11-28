#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define pi M_PI
#define R cin>>
#define Z class
#define ll long long
#define ln cout<<'\n'
#define in(a) insert(a)
#define pb(a) push_back(a)
#define pd(a) printf("%.10f\n",a)
#define mem(a) memset(a,0,sizeof(a))
#define all(c) (c).begin(),(c).end()
#define iter(c) __typeof((c).begin())
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define REP(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define rep(i,n) REP(i,0,n)
#define tr(it,c) for(iter(c) it=(c).begin();it!=(c).end();it++)
template<Z A>void pr(A a){cout<<a;ln;}
template<Z A,Z B>void pr(A a,B b){cout<<a<<' ';pr(b);}
template<Z A,Z B,Z C>void pr(A a,B b,C c){cout<<a<<' ';pr(b,c);}
template<Z A,Z B,Z C,Z D>void pr(A a,B b,C c,D d){cout<<a<<' ';pr(b,c,d);}
template<Z A>void PR(A a,ll n){rep(i,n){if(i)cout<<' ';cout<<a[i];}ln;}
ll check(ll n,ll m,ll x,ll y){return x>=0&&x<n&&y>=0&&y<m;}
const ll MAX=1000000007,MAXL=1LL<<61,dx[4]={-1,0,1,0},dy[4]={0,1,0,-1};
typedef pair<int,int> P;

bool ck(char c,char d) {
  if(c=='R') return d!='V'&&d!='R'&&d!='O';
  if(c=='O') return d!='R'&&d!='O'&&d!='Y';
  if(c=='Y') return d!='O'&&d!='Y'&&d!='G';
  if(c=='G') return d!='Y'&&d!='G'&&d!='B';
  if(c=='B') return d!='G'&&d!='B'&&d!='V';
  return d!='B'&&d!='V'&&d!='R';
}
void Main() {
  int T,tt=1;
  R T;
  while(T--) {
    int n;
    R n;
    string s="ROYGBV";
    int a[6];
    rep(i,6) R a[i];
    string t="";
    bool f=1;
    rep(i,a[1]) {
      if(!a[4]) f=0;
      a[4]--;
      t+="BO";
    }
    if(a[1]&&t.size()!=n) {
      if(!a[4]) f=0;
      a[4]--;
      t+="B";
    }
    rep(i,a[3]) {
      if(!a[0]) f=0;
      a[0]--;
      t+="RG";
    }
    if(a[3]&&t.size()!=n) {
      if(!a[0]) f=0;
      a[0]--;
      t+="R";
    }
    rep(i,a[5]) {
      if(!a[2]) f=0;
      a[2]--;
      t+="YV";
    }
    if(a[5]&&t.size()!=n) {
      if(!a[2]) f=0;
      a[2]--;
      t+="Y";
    }
    cout << "Case #" << tt++ << ": ";
    if(!f) {
      pr("IMPOSSIBLE");
      continue;
    }
    int m=n-t.size();
    vector<P> v(3);
    v[0]=P(a[0],0),v[1]=P(a[2],1),v[2]=P(a[4],2);
    sort(all(v));
    f=0;
    do {
      char c[m];
      queue<char> que;
      rep(i,3) {
        char ch;
        if(v[i].S==0) ch='R';
        if(v[i].S==1) ch='Y';
        if(v[i].S==2) ch='B';
        rep(j,v[i].F) que.push(ch);
      }
      for(int i=0; i<m; i+=2) {
        c[i]=que.front();que.pop();
      }
      for(int i=1; i<m; i+=2) {
        c[i]=que.front();que.pop();
      }
      string r=t;
      rep(i,m) r+=c[i];
      bool ff=1;
      rep(i,n) {
        if(!ck(r[i],r[(i+1)%n])) ff=0;
      }
      if(ff) {
        f=1;
        t=r;
        break;
      }
    } while(next_permutation(all(v)));
    if(f) pr(t);
    else pr("IMPOSSIBLE");
  }
}

int main(){ios::sync_with_stdio(0);cin.tie(0);Main();return 0;}
/*
  O RY
  G YB
  V BR
*/
