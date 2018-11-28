#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

const int MaxInt=numeric_limits<int>::max();
typedef vector<int> VI;
typedef vector<string> VS;

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
      int n, c, m, p1[1001]={}, p2[1001]={}, ile1=0, ile2=0;
      cin>>n>>c>>m;
      for (int i=0; i<m; ++i)
      {
          int p, b;
          cin>>p>>b;
          if (b==1)
          {
              ++p1[p];
              ++ile1;
          }
          else
          {
              ++p2[p];
              ++ile2;
          }
      }
      int y=0, z=0;
      while (ile1 || ile2)
      {
          int k1=0;
          for (int i=0; i<=n; ++i)
              if (min(p1[k1], p2[k1])<min(p1[i], p2[i]))
                  k1=i;
          if (k1==0)
          {
              y+=max(ile1, ile2);
              break;
          }
          int k2=0;
          for (int i=0; i<=n; ++i)
              if (i!=k1 && min(p1[k2], p2[k2])<min(p1[i], p2[i]))
                  k2=i;
          if (k2!=0)
          {
              --ile1;
              --ile2;
              --p1[k1];
              --p2[k2];
              ++y;
              continue;
          }
          int k=0;
          for (int i=0; i<=n; ++i)
              if (i!=k1 && (p1[i] || p2[i]))
              {
                  k=i;
                  break;
              }
          if (k==0)
          {
              if (k1==1) y+=ile1+ile2;
              else
              {
                  y+=max(ile1, ile2);
                  z+=min(ile1, ile2);
              }
              break;
          }
          if (p1[k])
          {
              --p1[k];
              --p2[k1];
              --ile1;
              --ile2;
              ++y;
          }
          else
          {
              --p1[k1];
              --p2[k];
              --ile1;
              --ile2;
              ++y;
          }

      }
      cout<<"Case #"<<ca<<": "<<y<<' '<<z;
      cout<<endl;
  }
  return 0;
}
