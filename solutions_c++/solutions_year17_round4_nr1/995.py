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
#define For(i,a,n) for (int i=a; i<n; ++i)
#define Fori(n) For(i,0,n)

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
      int n, p, x[10]={};
      cin>>n>>p;
      for (int i=0; i<n; ++i)
      {
          int a;
          cin>>a;
          ++x[a%p];
      }
      int wyn=x[0];
      switch (p)
      {
          case 2:
              wyn+=(x[1]+1)/2;
              break;
          case 3:
          {
              int b=min(x[1], x[2]);
              wyn+=b;
              x[1]-=b;
              x[2]-=b;
              wyn+=(x[1]+2)/3;
              wyn+=(x[2]+2)/3;
              break;
          }
          case 4:
          {
              int b=min(x[1], x[3]);
              wyn+=b;
              x[1]-=b;
              x[3]-=b;
              int c=x[2]/2;
              wyn+=c;
              x[2]-=2*c;
              if (x[1]==0)
              {
                  if (x[2]==0) wyn+=(x[3]+3)/4;
                  else if (x[3]<=2) ++wyn;
                  else wyn+=1+(x[3]+3-2)/4;
              }
              else//x[3]==0
              {
                  if (x[2]==0) wyn+=(x[1]+3)/4;
                  else if (x[1]<=2) ++wyn;
                  else wyn+=1+(x[1]+3-2)/4;
              }
              break;
          }
      }
      cout<<"Case #"<<ca<<": "<<wyn;

      cout<<endl;
  }
  return 0;
}
