#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
#define pp pair<double,double>
#define PI 3.14159265358979323846
#define INF 1000000007
int dp[1440][720][2][2];
int main() {
  int t,test;
  scanf("%d",&t);
  for(test=1;test<=t;test++){
    int n,k,i,j;
    scanf("%d%d",&n,&k);
    double u=0, ans=0;
    scanf("%lf",&u);
    vector<double> G;
    for(i=0;i<n;i++){
      double p;
      scanf("%lf",&p);
      G.push_back(p);
    }
    sort(G.begin(), G.end());
    for(i=0;i<n;i++){
      for(j=1;j<=n;j++){
        double sum = 0, maxVal = 0, val;
        if(i+j > n)
          continue;
        for(k=i;k<i+j;k++){
          sum+=G[k];
          maxVal = max(maxVal, G[k]);
        }
        val = min(1, (u+sum)/(j*1.0));
        if(val > maxVal){
          double localAns = 1;
          for(k=0;k<i;k++){
            localAns *= G[k];
          }
          for(k=0;k<j;k++){
            localAns *= val;
          }
          for(k=i+j;k<n;k++){
            localAns *= G[k];
          }
          ans = max(ans, localAns);
        }
      }
    }
    printf("Case #%d: %0.8lf\n",test,ans);
  }
  return 0;
}