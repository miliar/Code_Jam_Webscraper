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
        string s;
        int k;
        ll cnt = 0;

        cin >> s >> k;

        cout << "Case #" << j + 1 << ": ";

        bool flag = false;
        for (int i = 0; i < s.size(); ++i)
        {
            if (s[i] == '-')
            {
                if (i + k > s.size())
                { 
                    flag = true;
                    break;
                }
                ++cnt;
                for (int j = 0; j < k; ++j)
                {
                    s[i + j] = s[i + j] == '-' ? '+' : '-';
                }
            }
        }

        if (flag)
        {
            cout << "IMPOSSIBLE" << endl;
        }
        else
        {
            cout << cnt << endl;
        }
    }




    int letsmakepause;
    std::cin >> letsmakepause;

    return 0;
}

