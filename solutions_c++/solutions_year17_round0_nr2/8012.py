#include <iostream>
#include <string>
#include <math.h>
#include <vector>
#include <algorithm>
#include <map>
// #include <unordered_map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <stdio.h>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <iterator>
#include <bitset>
#include <ctime>

 #pragma warning(disable : 4996)
 
 using namespace std;
 
 #define pb push_back
 #define mp make_pair
 
 #define fori(n) for (int i = 0; i < n; ++i)
 #define forj(n) for (int j = 0; j < n; ++j)
 
 #define fordi(n) for (int i = n - 1; i >= 0; --i)
 #define fordj(n) for (int j = n - 1; j >= 0; --j)

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef std::vector<int> vi;
typedef std::vector<ll> vll;
typedef std::pair<int, int> pii;


const ll ll_max = 9223372036854775800;
const ll ll_min = -9223372036854775800;

const int int_max = 2147483640;
const int int_min = -2147483640;

const ll mod = 1000000007;

/*----------------------------------------------------------------*/

string toString(ll n)
{
    stringstream ss;
    ss << n;
    return ss.str();
}

int main()
{
     ifstream cin("input.in");
     ofstream cout("output.out");

    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0);

    int t;
    cin >> t;
    forj(t)
    {
        ll n;
        cin >> n;    
        string s = toString(n);

        cout << "Case #" << j + 1 << ": ";

        ll li = 0;
        for (int i = 0; i < s.size() - 1; ++i)
        {
            if (i != 0 && s[i] != s[i - 1])
            {
                li = i;
            }
            if (s[i] - '0' > s[i + 1] - '0')
            {
                ll p = pow(10, s.size() - li - 1);
                n -= p;
                n /= p;
                n *= p;

                p /= 10;
                while (p != 0)
                {
                    n += p * 9;

                    p /= 10;
                }

                break;
            }
        }

        cout << n << endl;

    }




      int letsmakepause;
      std::cin >> letsmakepause;

    return 0;
}

