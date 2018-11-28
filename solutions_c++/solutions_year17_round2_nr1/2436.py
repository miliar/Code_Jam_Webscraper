#include <iostream>
#include <string>
#include <math.h>
#include <vector>
#include <algorithm>
#include <map>
#include <unordered_map>
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
    ifstream cin("inp.in");
    ofstream cout("outp.out");

    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0);

    int t;
    cin >> t;
    for (int ti = 1; ti <= t; ++ti)
    {
        ld d, n, k, s;
        cin >> d >> n;
        vector<pair<ld, ld>> inp(n + 1);
        fori(n)
        {
            cin >> k >> s;
            inp[i] = mp(k, s);
        }
        inp[n] = mp(0, ll_max);
        sort(inp.begin(), inp.end());
        reverse(inp.begin(), inp.end());

        ld curt = 0;
        for (int i = 0; i < n + 1; ++i)
        {
            curt = max(curt, (d - inp[i].first) / inp[i].second);
        }
        ld answ = d / curt;

        cout << "Case #" << ti << ": ";

        cout << fixed << setprecision(7) << answ << endl;
    }



    int letsmakepause;
    std::cin >> letsmakepause;
    return 0;
}