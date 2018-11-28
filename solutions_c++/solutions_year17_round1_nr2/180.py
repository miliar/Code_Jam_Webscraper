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

int n, p, poprzIle;
VI r, q[50], poz;

bool przesun(int ile)
{
    for (int i=0; i<n; ++i)
    {
        long long z=ile*(long long) r[i];
        long long mi=(z*9+9)/10, ma=z*11/10;
        for (; ; )
        {
            if (p<=poz[i])
                return false;
            int x=q[i][poz[i]];
            if (x<mi) ++poz[i];
            else if (ma<x) return false;
            else break;
        }
    }
    for (int i=0; i<n; ++i)
        ++poz[i];
    return true;
}

bool przesun()
{
    while (poprzIle<=1000000)
    {
        if (przesun(poprzIle))
            return true;
        ++poprzIle;
    }
    return false;
}

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
      poprzIle=1;
      cin>>n>>p;
      r.clear();
      for (int i=0; i<n; ++i)
      {
          int a;
          cin>>a;
          r.push_back(a);
          q[i].clear();
      }
      for (int i=0; i<n; ++i)
      {
          for (int j=0; j<p; ++j)
          {
              int a;
              cin>>a;
              q[i].push_back(a);
          }
          sort(q[i].begin(), q[i].end());
      }
      int wyn=0;
      poz=VI(n, 0);
      while (przesun())
          ++wyn;
      cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }
  return 0;
}
