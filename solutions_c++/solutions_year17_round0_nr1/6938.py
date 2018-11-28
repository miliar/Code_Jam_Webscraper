// Nguyen Cao Nhat Long
// Pikachuuuuuuuuuuuuu
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <set>
#include <queue>
#include <vector>
#include <stack>
#include <map>
#include <string>
#include <sstream>
using namespace std;

#define next oapsidfjiuunfiujfa
#define prev sdofljkauohfaodisf

#define sqr(x) ((x)*(x))
#define PI acos(-1)

#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define REP(i,a) for(int i = 0, _a = (a); i < _a; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)

#define ii pair<int,int>
#define fi first
#define se second
#define mp make_pair

#define sz(x) (int)x.size()
#define ALL(x) (x).begin(), (x).end()
#define MS(a,x) memset(a, x, sizeof(a))

#define sync ios::sync_with_stdio(false)

#define ll long long
#define vi vector<int>
#define vll vector<ll>
#define vii vector<ii>
#define pb push_back

#define inf 1000000000
#define INF 100000000000000000LL
#define mod 1000000007LL
#define maxn 100010

// End of template

int main()
{
    freopen("Alarge.in", "r", stdin);
    freopen("Alarge.txt", "w", stdout);

    sync;

    int q;
    cin >> q;

    FOR(test, 1, q)
    {
        int k, res = 0;
        string s;

        cin >> s >> k;

        REP(i, sz(s))
        {
            if(s[i] == '-')
            {
                if(i + k - 1 >= sz(s))
                {
                    //cout << i << '\n';
                    res = -1;
                    break;
                }
                FOR(j, i, i + k - 1)
                    s[j] = s[j] == '-' ? '+' : '-';
                res++;
            }
        }

        cout << "Case #" << test << ": ";

        if(res < 0) cout << "IMPOSSIBLE\n";
        else cout << res << '\n';
    }
}
