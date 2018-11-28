#include <map>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

#define enableFastIO ios_base::sync_with_stdio(false);
#define inc(i,j,k) for (auto i=j;i<=k;i++)
#define li long int
#define lli long long int
#define ulli unsigned long long int

using namespace std;

namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

class Solution{
  public:
        bool isTidy(ulli t){
            string s = patch::to_string(t);
            char lastC = '0';
            for (char c:s) {
                if (c >= lastC) lastC = c;
                else return false;
            }
            return true;
        }
};




int main()
{
    enableFastIO;
    int n;
    ulli k;
    cin >> n;
    Solution s1;
    inc(testcase,1,n) {
        cin >> k;
        while (!s1.isTidy(k)) k--;
        cout << "Case #" << testcase << ": " << k << endl;
    }
}
