#include<bits/stdc++.h>
using namespace std;

int T;
int m;
double d;
double k,s;
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);

  cin>>T;
  for(int it=1;it<=T;it++)
  {
    cin>>d>>m;
    double ans = 1e30;
    for(int i=1;i<=m;i++)
    {
      cin>>k>>s;
      if(fabs(k-d)>0.1)
        ans=min(ans,d*s/(d-k));
      //cout<<"speed="<<k<<" "<<s<<endl;
      //cout<<"need="<<d*s/(d-k)<<endl;
    }
    printf("Case #%d: %.8f\n",it,ans);
  }
  return 0;
}
