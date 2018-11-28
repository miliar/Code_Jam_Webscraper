#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
typedef long long int ll;


void solve() {
  int d,n;cin>>d>>n;
  double max_t=0;
  REP(i,n) {
    int k,s;cin>>k>>s;
    max_t=max(max_t, (double)(d-k)/(double)s);
  }
  double result=(double)d/max_t;
  cout.precision(8);
  cout<<result<<endl;
}
int main() {
  int t;cin>>t;REP(i,t) {
    cout<<"Case #"<<(i+1)<<": ";
    solve();
  }

}
