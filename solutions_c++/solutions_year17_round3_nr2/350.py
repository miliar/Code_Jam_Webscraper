#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define S 1440
#define K (S/2+1)
#define inf 10000
typedef long long int ll;
int DP[S][K][2];
void solve() {
  int ac,aj;
  cin>>ac>>aj;
  vector<int> m(S,3);

  REP(i,ac) {
    int b,e;cin>>b>>e;
    for(int j=b;j<e;++j) m[j]&=2; // only second can
  }
  REP(i,aj) {
    int b,e;cin>>b>>e;
    for(int j=b;j<e;++j) m[j]&=1; // only first can
  }
  int best=inf;
  REP(starter,2) {

    REP(slot, S) {
      if(slot==0) {
        REP(i,K) DP[0][i][0]=DP[0][i][1]=inf;
        if(m[0] & 1) DP[0][1][0] = 0!=starter;
        if(m[0] & 2) DP[0][0][1] = 1!=starter;
      } else {
        REP(i,K) DP[slot][i][0]=DP[slot][i][1]=inf;
        REP(i,K) {
          REP(newholder,2) if(m[slot] & (1<<newholder)) {
            REP(holder,2) {
            // give it to 0
            if(i+(newholder==0)<K) {
              int &Q = DP[slot][i+(newholder==0)][newholder];
              int V= DP[slot-1][i][holder]+(newholder!=holder);
              Q=min(Q, V);            
            }
            }
          }
        }
      }
    }
    int v1=DP[S-1][K-1][0]+(starter!=0);
    int v2=DP[S-1][K-1][1]+(starter!=1);
    best=min(best, v1);
    best=min(best, v2);


  }


  cout<<best<<endl;
}
int main() {
  int t;cin>>t;REP(i,t) {
    cout<<"Case #"<<(i+1)<<": ";
    solve();
  }

}
