#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <limits>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<long long> vll;

template <typename T>
string tostring ( T value )
{
    ostringstream ss;
    ss << value;
    return ss.str();
}

template <typename T>
T strtonum ( const string &Text )
{
    istringstream ss(Text);
    T result;
    return ss >> result ? result : 0;
}
//----------------------------------

map<char,string> fromprs;

//==================================
void solve()
{
    int numCases = 1;
    cin >> numCases;

    for ( int ncase=1; ncase <= numCases; ncase++ )
    {
        //===== start case
        string s;
        cin >> s;
        vector<char> v(s.begin(),s.end());
        string ans;
        int firstidxchangeallto9 = -1;
        for (int i=v.size()-1; i>0; i--)
        {
            if (v[i]<v[i-1])
            {
                firstidxchangeallto9=i;
                // decrease by 1
                v[i-1] -= 1;
            }
        }
        if (firstidxchangeallto9>0)
        {
            // change all digits from this point to the end to '9'
            for (int j=firstidxchangeallto9; j<v.size(); j++)
            {
                v[j]='9';
            }
        }
        if (v[0]=='0')
            v.erase(v.begin());

        ans = string(v.begin(), v.end());
        cout << "Case #" << ncase << ": ";
        cout << ans << endl;

        //===== end case

    }
}

int main()
{
#ifdef CCQTEST
#include "HRCPP1.h"
#endif
    solve();
#ifdef CCQTEST
#include "HRCPP2.h"
#endif
    return 0;
}
