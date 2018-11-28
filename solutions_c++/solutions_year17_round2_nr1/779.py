#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int t;
ll d,n;
int main() {
  ios::sync_with_stdio(false);
  cin>>t;
  for(int cislo=1;cislo<=t;cislo++){
    cin>>d>>n;
    vector<pair<ll,ll> > kone(n);
    for(int i=0;i<n;i++)cin>>kone[i].first>>kone[i].second;
    sort(kone.begin(), kone.end());
    double cas=(d-kone.back().first)/(kone.back().second*1.0);
    for(int i=n-2;i>=0;i--){
      cas=max(cas,(d-kone[i].first)/(kone[i].second*1.0));
    }
    cout <<"Case #"<<cislo<<": ";
    cout <<setprecision(10)<<fixed;
    cout <<d/cas<<endl;
  }
  return 0;
}