#include <bits/stdc++.h>

using namespace std;

#define MP make_pair
#define PB push_back
typedef long long LL;
typedef pair<int,int> PII;
const double eps=1e-8;
const double pi=acos(-1.0);
const int K=1e6+7;
const int mod=1e9+7;


int n;
double d,ans,s[K],p[K];
int main(void)
{
    freopen("ans.txt","w",stdout);
    int t,cnt=1;cin>>t;
    while(t--)
    {
      cin>>d>>n;
      for(int i=1;i<=n;i++)
            scanf("%lf%lf",s+i,p+i);
      double mxt=0,t;
      for(int i=1;i<=n;i++)
      {
          t=(d-s[i])/p[i];
          mxt=max(t,mxt);
      }
      printf("Case #%d: %.6f\n",cnt++,d/mxt);
    }
    return 0;
}
