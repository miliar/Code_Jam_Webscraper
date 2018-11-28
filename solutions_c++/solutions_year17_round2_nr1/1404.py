#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("ina-l.in","r",stdin);
  freopen("outa-large.txt","w",stdout);
  int t;cin>>t;
  for(int test=1;test<=t;test++) {
    double k,n,d,s;
    cin>>d>>n;
    double myti = 0.0;
    for(int i=0;i<n;i++){
      cin>>k>>s;
      double ti = (d-k)/s;
      myti = max(myti, ti);
    }
    double ans = (d/myti);
    printf("Case #%d: %.6f\n",test,ans );
  }
  return 0;
}
