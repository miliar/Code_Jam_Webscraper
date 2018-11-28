#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
    string s;
    int k, wyn=0, n;
    cin>>s>>k;
    n=s.size();
    for (int i=0; i<n; ++i)
        if (s[i]=='-')
        {
            if (n<=i+k-1)
            {
                wyn=-1;
                break;
            }
            ++wyn;
            for (int j=0; j<k; ++j)
                s[i+j]= s[i+j]=='-' ? '+' : '-';
        }
    cout<<"Case #"<<ca<<": ";
    if (wyn==-1) cout<<"IMPOSSIBLE";
    else cout<<wyn;
    cout<<endl;
  }
  return 0;
}
