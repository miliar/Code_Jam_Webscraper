#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <cstring>
#include <set>
#include <map>
#include <fstream>
#include <string>
#include <stack>
#include <deque>
#include <algorithm>
#include <random>
#include <ctime>
#include <sstream>
#include <functional>
using namespace std;

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define mp make_pair
#define sq(x) ((x)*(x))
#define ifthen(x,y,z) ((x)?(y):(z))

using ll = long long;
using ull = unsigned long long;
using intpair = pair<int, int>;
using llpair = pair<ll, ll>;
using ld = long double;
using d = double;
using vint = vector<int>;
using vll = vector<ll>;

struct Edge
{
    int to, w;
};

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n;
    cin >> n;

    for (int z = 1; z <= n; ++z)
    {
        string q;
        cin >> q;

        for (int k = 0; k < q.size(); ++k)
            for (int i = 0; i < q.size() - 1; ++i)
            {
                if (q[i] > q[i + 1])
                {
                    q[i]--;
                    for (int j = i + 1; j < q.size(); ++j)
                        q[j] = '9';
                }
            }

        if (q[0] == '0')
        {
            for (int i = 0; i < q.size() - 1; ++i)
                q[i] = '9';
            q.pop_back();
        }

        cout << "Case #" << z << ": " << q << "\n";
    }

    return 0;
}