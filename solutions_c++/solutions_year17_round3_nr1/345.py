#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
typedef long long int ll;
double pi=3.1415926535897932385;
void solve() {
  int n,k;
  cin>>n>>k;
  vector<pair<double, double> >v(n);
  REP(i,n) cin>>v[i].first>>v[i].second;
  REP(i,n) v[i].second=-v[i].second;
  sort(v.begin(), v.end());
  REP(i,n) v[i].second=-v[i].second;
  double result=0;
  for(int i=n-1;i>=k-1;--i) {
    //cout<<i<<endl;
    vector<double> sm;
    vector<double> g;
    sm.push_back(pi*v[i].first*v[i].first+2.0*pi*v[i].first*v[i].second);
    REP(j,i) g.push_back(pi*2.0*v[j].first*v[j].second);
  //  cout<<"B"<<endl;
    sort(g.begin(),g.end());
    for(int j=g.size()-1;j>=(int)g.size()-k+1;--j) {
//      cout<<"FF "<<j<<"rr "<<(g.size()-k+1)<<endl;
      sm.push_back(g[j]);
    }
    double z=0.0;
    sort(sm.begin(), sm.end());
    REP(j,sm.size()) z+=sm[j];
    if(z>result) result=z;
  }
  cout.precision(20);
  cout<<result<<endl;
}
int main() {
  int t;cin>>t;REP(i,t) {
    cout<<"Case #"<<(i+1)<<": ";
    solve();
  }

}
