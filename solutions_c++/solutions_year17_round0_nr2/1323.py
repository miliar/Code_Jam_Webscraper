#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, s, n) for(int i=(s); i<=(n); i++)
#define FORD(i, s, n) for(int i=(s); i>=(n); i--)
#define SIZE(x) ((int) (x).size())
#define DEBUG 0
#define D if(DEBUG)
typedef long long LL;
typedef pair<int, int> PII;

void clear_zeros(string & s)
{
    reverse(s.begin(), s.end());
    while(SIZE(s) > 1 && s.back() == '0') s.pop_back();
    reverse(s.begin(), s.end());
}

void solve()
{
    string l;
    cin >> l;
    if(l == "0")
    {
        cout << "0\n";
        return;
    }

    int l_pref = 1;
    while(l_pref < SIZE(l) && l[l_pref] >= l[l_pref - 1]) l_pref++;
    if(SIZE(l) == l_pref)
    {
        cout << l << '\n';
        return;
    }

    while(l_pref > 1 && l[l_pref - 1] == l[l_pref - 2]) l_pref--;
    l[l_pref - 1]--;
    FOR(i, l_pref, SIZE(l) + 1) l[i] = '9';
    clear_zeros(l);
    cout << l << '\n';
}

int main()
{
    std::ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    REP(i, t)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}