#include <bits/stdc++.h>

using namespace std;
#define lli long long int
#define ii pair<lli, lli>

vector<ii> v;
#define pi 3.14159265358979323846264338327950288419716939937510582097494

int main() {
  freopen("ina-large.in","r",stdin);
  freopen("outa-large.txt","w",stdout);
  int t; cin>>t;
  for(int test=1;test<=t;test++){
    v.clear();
    double ans = 0.0;
    int n,k;
    cin>>n>>k;
    for(int i=0;i<n;i++){
      lli a,b;
      cin>>a>>b;
      v.push_back(ii(a,b));
    }
    sort(v.begin(), v.end());

    for(int i=n-1;i>=0;i--){
      vector<double> temp;
      for(int j=i-1;j>=0;j--){
        temp.push_back(v[j].first* v[j].second*1.0);
      }
      sort(temp.begin(), temp.end());
      int p = temp.size();
      int c =0;
      double si = 0.0;
      for (int l=p-1;l>=0;l--){
        if(c==k-1) break;
        // cout<<c<<" "<<l<<endl;
        si += (temp[l]*1.0);
        c++;
      }
      double ar = ( (v[i].first*v[i].first*1.0 + 2.0 * si + 2.0*v[i].first*v[i].second));
      // printf("%.6f\n",ar );
      ans = max(ans,ar);
    }
    printf("Case #%d: %.8f\n",test,(ans*pi) );
  }

  return 0;
}
