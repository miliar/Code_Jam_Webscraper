// Kappa 123
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

vector<int> mod[4];

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
        for(int i = 0; i < 4; i++)
            mod[i].clear();
        int n, p;
        cin >> n >> p;
        for(int i = 0; i < n; i++)
        {
            int g;
            cin >> g;
            mod[g % p].pb(g);
        }
        vector<int> ans;
        if(p <= 3)
        {
            while(mod[0].size())
            {
                ans.pb(mod[0].back());
                mod[0].pop_back();
            }
            while(mod[1].size() && mod[2].size())
            {
                ans.pb(mod[1].back());
                ans.pb(mod[2].back());
                mod[1].pop_back();
                mod[2].pop_back();
            }
            while(mod[2].size())
            {
                ans.pb(mod[2].back());
                mod[2].pop_back();
            }
            while(mod[1].size())
            {
                ans.pb(mod[1].back());
                mod[1].pop_back();
            }
        }
        else
        {
            while(mod[0].size())
            {
                ans.pb(mod[0].back());
                mod[0].pop_back();
            }
            while(mod[2].size() > 1)
            {
                ans.pb(mod[2].back());
                ans.pb(mod[2].back());
                mod[2].pop_back();
                mod[2].pop_back();
            }
            while(mod[1].size() && mod[3].size())
            {
                if(mod[1].size() > mod[3].size())
                {
                    ans.pb(mod[3].back());
                    ans.pb(mod[1].back());
                }
                else
                {
                    ans.pb(mod[1].back());
                    ans.pb(mod[3].back());
                }
                mod[1].pop_back();
                mod[3].pop_back();
            }
            while(mod[2].size())
            {
                ans.pb(mod[2].back());
                mod[2].pop_back();
            }
            while(mod[1].size())
            {
                ans.pb(mod[1].back());
                mod[1].pop_back();
            }
            while(mod[3].size())
            {
                ans.pb(mod[3].back());
                mod[3].pop_back();
            }
        }
        int cnt = 0;
        int rem = 0;
        for(int i = 0; i < ans.size(); i++)
        {
            if(rem == 0)
                cnt++;
            rem += (ans[i] % p);
            rem %= p;
        }
        cout << "Case #" << tcase << ": " << cnt << '\n';
    }
    return 0;
}
