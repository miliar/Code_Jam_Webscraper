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

int n, s[20], res[20];

bool process(int id = 1, bool goLow = false)
{
    if(id == n + 1)
        return true;

    int st = (goLow ? 9 : s[id]);

    FORD(i, st, res[id - 1])
    {
        if(i != st) goLow = true;

        res[id] = i;

        //if(n - (id + 1) + 1 > 9 - res[id])
            //break;

        if(process(id + 1, goLow))
            return true;
    }


    return false;
}

int main()
{
    freopen("bsmall.in", "r", stdin);
    freopen("bsmall.out", "w", stdout);

    sync;

    int TEST;
    cin >> TEST;

    FOR(test, 1, TEST)
    {
        string tmp;
        cin >> tmp;

        n = sz(tmp);

        REP(i, n) s[i + 1] = tmp[i] - '0';
        REP(i, n) res[i + 1] = 0;

        process();

        int i = 1;
        while(!res[i]) i++;

        cout << "Case #" << test << ": ";
        FOR(k, i, n) cout << res[k];
        cout << '\n';
    }
}
