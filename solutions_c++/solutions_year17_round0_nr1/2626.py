#include <bits/stdc++.h>
using namespace std;
typedef long long int ll; 
typedef vector<ll> vll;
typedef pair<ll,ll> pll;
#define pb push_back
#define endl '\n'
#define f first
#define s second
#define forn(i,n) for(int i = 0; i < int(n); i++)
const ll INF = 1e9, MOD = 1e9+7;

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for(int casen = 1; casen <= t; casen++)
    {
        cout << "Case #" << casen << ": ";
        string s;
        cin >> s;
        int k, ans = 0;
        cin >> k;
        for(int i = 0; i < s.size() - k + 1; i++)
            if(s[i] == '-')
            {
                ans++;
                for(int j = 0; j < k; j++)
                    s[i+j] = (s[i+j] == '+')?'-':'+';
            }
        forn(i, s.size()) if(s[i] == '-') ans = -1;
        // cerr << s << endl;
        if(ans == -1) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;
    }
    return 0;
}

