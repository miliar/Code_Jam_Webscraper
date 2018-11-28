#include <iostream>

using namespace std;

int main()
{
  int n;
  cin>>n;
  for (int i=1;i<=n;i++)
  {
    int a,b;
    cin>>a>>b;
    int v[a+2];
    for (int i=0;i<a+2;i++)
      v[i]=0;
    v[0]=1;
    v[a+1]=1;
    for (int j=0;j<b;j++)
    {
      int mi=-1,ma=-1,t=0;
      for (int k=1;k<=a;k++)
        if (v[k]==0)
        {
          int l=0,r=0;
          int z=k;
          while (v[z-l]==0)
            l++;
          l--;
          while (v[z+r]==0)
            r++;
          r--;
          if (l>r)
          {
            int u=l;
            l=r;
            r=u;
          }
          if (l>mi || l==mi && r>ma)
          {
            mi=l;
            ma=r;
            t=k;
          }
        }
      v[t]=1;
      if (j==b-1)
        cout<<"Case #"<<i<<": "<<ma<<' '<<mi<<endl;
    }
  }
  return 0;
}