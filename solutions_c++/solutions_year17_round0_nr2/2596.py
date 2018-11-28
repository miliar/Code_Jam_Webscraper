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
    for(int cn = 1; cn <= t; cn++)
    {
        string s;
        cin >> s;
        cout << "Case #" << cn << ": ";
        for(int i = s.size() - 1; i >= 1; i--)
        {
            if(s[i] < s[i-1])
            {
                s[i-1]--;
                for(int j = i; j < s.size(); j++)
                    s[j] = '9';
            }
        }
        if(s[0] == '0') cout << s.substr(1) << endl;
        else cout << s << endl;
    }
    return 0;
}

