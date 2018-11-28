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

void solve()
{
    LL n, k;
    cin >> n >> k;
    
    LL wieksza = n;
    LL ilosc_wiekszych = 1, ilosc_mniejszych = 0;
    LL zostalo = k;
    while(zostalo > ilosc_wiekszych + ilosc_mniejszych)
    {
        zostalo -= ilosc_mniejszych + ilosc_wiekszych;
        if(wieksza%2 == 0)
        {
            wieksza = (wieksza - 1)/2 + 1;
            // ilosc_wiekszych taka sama
            ilosc_mniejszych = ilosc_mniejszych*2 + ilosc_wiekszych;
        }
        else
        {
            wieksza = (wieksza - 1)/2;
            // ilosc_mniejszych taka sama
            ilosc_wiekszych = ilosc_wiekszych*2 + ilosc_mniejszych;
        }
    }

    if(zostalo <= ilosc_wiekszych)
    {
        LL w = wieksza - 1;
        if(w%2 == 1) cout << w/2 + 1 << ' ' << w/2 << '\n';
        else cout << w/2 << ' ' << w/2 << '\n';
    }
    else
    {
        LL w = wieksza - 2;
        if(w%2 == 1) cout << w/2 + 1 << ' ' << w/2 << '\n';
        else cout << w/2 << ' ' << w/2 << '\n';
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    REP(i, t)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    } 
}