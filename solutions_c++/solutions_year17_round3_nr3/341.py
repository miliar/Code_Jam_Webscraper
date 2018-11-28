#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
typedef long long int ll;
void solve() {
  int n,k;
  double u;
  cin>>n>>k>>u;
  vector<double>  p(n);
  REP(i,n) cin>>p[i];
  while(u>0.0000000001) {
    sort(p.begin(), p.end());
    int equal=1;
    while(equal<n && p[equal]==p[equal-1])++equal;

    double m=min(u/(double)equal,1.0-p[0]);
    if(equal<n) m=min(m, p[equal]-p[0]);
    u-=m*(double)equal;
    REP(i,equal) p[i]+=m;
  }
  double result=1.0;
  REP(i,n) result*=p[i];
  cout.precision(20);
  cout<<result<<endl;
}
int main() {
  int t;cin>>t;REP(i,t) {
    cout<<"Case #"<<(i+1)<<": ";
    solve();
  }

}
