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
    string s;
    cin>>s;
    for (int i=1; i<s.size(); ++i)
        if (s[i]<s[i-1])
        {
            int dz=0;
            for (int j=i-1; 0<j; --j)
                if (s[j-1]<s[j])
                {
                    dz=j;
                    break;
                }
            if (dz==0 && s[0]=='1')
            {
                s.erase(s.end()-1);
                dz=-1;
            }
            else --s[dz];
            for (int k=dz+1; k<s.size(); ++k)
                s[k]='9';
            break;
        }
    cout<<"Case #"<<ca<<": "<<s;
    cout<<endl;
  }
  return 0;
}
