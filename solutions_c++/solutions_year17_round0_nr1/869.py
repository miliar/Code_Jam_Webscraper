#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define FILE "file"

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int INF = numeric_limits<int>::max();
const ll LLINF = numeric_limits<ll>::max();
const ull ULLINF = numeric_limits<ull>::max();
const double PI = acos(-1.0);

int main()
{
    freopen(FILE".in", "r", stdin);
    freopen(FILE".out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for(int tcase = 1; tcase <= T; tcase++)
    {
        cout << "Case #" << tcase << ": ";
        string s;
        int k;
        cin >> s >> k;
        int cnt = 0;
        int n = s.size();
        for(int i = 0; i <= n - k; i++)
        {
            if(s[i] == '-')
            {
                for(int j = 0; j < k; j++)
                    s[i + j] = (s[i + j] == '-' ? '+' : '-');
                cnt++;
            }
        }
        bool good = 1;
        for(char a: s)
            if(a == '-')
                good = 0;
        if(!good)
            cout << "IMPOSSIBLE\n";
        else
            cout << cnt << '\n';
    }
    return 0;
}
