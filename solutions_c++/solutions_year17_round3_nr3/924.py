#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("inc1.in","r",stdin);
  freopen("outc-s.txt","w",stdout);
  int t; cin>>t;
  for(int test=1;test<=t;test++){
    int n,k;
    double u,p,sum=0.0;
    cin>>n>>k;
    vector<double> x;
    cin>>u;

    for(int i=0;i<n;i++){
      cin>>p;
      x.push_back(p);
      sum+=p;
    }

    sort(x.begin(), x.end());
    double ans = 0.0;

    for(int i=0;i<n;i++){
      for(int j=1;j<=n;j++){
        double sum = 0.0;
        double max_val = 0.0;
        if (i+j>n) continue;
        for(int k=i;k<(i+j);k++){
          sum += x[k];
          max_val = max(max_val, x[k]);
        }
        double val = min(1.000000,(double) (u+sum)/(j*1.0));
        if (val >= max_val){
          double res = 1.0;
          for(int p=0;p<i;p++){
            res *=x[p];
          }
          for(int p=0;p<j;p++){
            res*=val;
          }
          for(int p=(i+j);p<n;p++){
            res*=x[p];
          }

          ans = max(ans,res);
        }
      }
    }

    printf("Case #%d: %.8f\n",test,(ans));
  }
  return 0;
}
