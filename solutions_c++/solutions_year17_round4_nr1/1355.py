#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
#include <iostream>
#include <iomanip>
#include <set>
using namespace std;

typedef long long ll;

const int maxn = 305;
const double eps = 1e-8;
const int inf = 1e9 + 7;


int n,g[maxn],p;

int mo[10];

int solve()
{
  int res = mo[0];
  if(p==2)
    return res + (mo[1]+1)/2;
  if(p==3)
  {
    int ma = max(mo[1], mo[2]);
    int mi = min(mo[1], mo[2]);
    res += mi;
    ma -= mi;
    return res + (ma + 2) / 3;
  }
  if(p==4)
  {
    int ma = 0;
    for(int i=0;i<=n;i++)
      for(int j=0;j<=n;j++)
        for(int k=0;k<=n;k++)
        {
          if(2*i + k > mo[1])
            break;
          if(i + j > mo[2])
            break;
          if(2*j + k > mo[3])
            break;
          int l1 = mo[1] - 2*i - k;
          int l2 = mo[2] - i - j;
          int l3 = mo[3] - 2*j - k;
          int tp = i + j + k + l1/4 + l2/2 + l3/4;
          if(l1%4>0||l2%2>0||l3%4>0)
            tp+=1;
          ma = max(ma,tp);
        }
    return res + ma;
  }
}
int main() 
{
  int t,cs = 0;
  cin>>t;
  while(t--)
  {
    cin>>n>>p;
    memset(mo,0,sizeof(mo));
    for(int i=1;i<=n;i++)
    {
      cin>>g[i];
      mo[g[i]%p]++;
    }
    cout << "Case #" << ++cs <<": " << solve() << endl;
  }

}