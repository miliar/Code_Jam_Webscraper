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

void wyp(string &s)
{
    char pierw='?', ost='?';
    for (int i=0; i<s.size(); ++i)
        if (s[i]=='?') s[i]=ost;
        else
        {
            ost=s[i];
            if (pierw=='?')
                pierw=s[i];
        }
    if (pierw!='?')
        for (int i=0; i<s.size(); ++i)
            if (s[i]=='?')
                s[i]=pierw;
}

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
      int r, c;
      cin>>r>>c;
      string s[25], ost;
      for (int i=0; i<r; ++i)
      {
          cin>>s[i];
          wyp(s[i]);
          if (s[i][0]!='?')
              ost=s[i];
      }
      for (int i=r-1; 0<=i; --i)
          if (s[i][0]=='?') s[i]=ost;
          else ost=s[i];

      cout<<"Case #"<<ca<<": "<<endl;
      for (int i=0; i<r; ++i)
          cout<<s[i]<<endl;
  }
  return 0;
}
