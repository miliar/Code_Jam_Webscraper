#include<bits/stdc++.h>
using namespace std;

int main()
{

  int t,i;
  double t1[105]={0};
  cin>>t;
  for(i=0;i<t;i++)
  {
      int j,k,n;
      double mi=0,a[100005],d,di,si,ans;
      cin>>d>>n;
      for(j=0;j<n;j++)
      {
          double cur;
          cin>>di>>si;
          if(di<d)
          {
              cur=(d-di)/si;
          }
          mi=max(cur,mi);
      }
      ans=d/mi;
      t1[i]=ans;
  }
  for(i=0;i<t;i++)
  {
      cout<<"Case #"<<i+1<<": ";
      printf("%0.6lf",t1[i]);
      cout<<" \n";
  }
  return 0;
}
