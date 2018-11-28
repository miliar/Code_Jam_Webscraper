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

bool good(string s)
{
    for(int i = 1; i < s.size(); i++)
        if(s[i - 1] > s[i])
            return false;
    return true;
}

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
        cin >> s;
        while(!good(s))
        {
            for(int i = 1; i < s.size(); i++)
            {
                if(s[i - 1] > s[i])
                {
                    s[i - 1]--;
                    for(int j = i; j < s.size(); j++)
                        s[j] = '9';
                    break;
                }
            }
        }
        int start = 0;
        for(; start < s.size() && s[start] == '0'; start++);
        cout << s.substr(start, s.size() - start + 1) << '\n';
    }
    return 0;
}
