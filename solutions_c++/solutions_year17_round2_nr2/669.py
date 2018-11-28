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

unordered_set<long long> has;
int R, G, B;
int started;

inline pair<int, pair<int, pair<int, int>>> gett(int r, int g, int b, int e)
{
    return mp(r, mp(g, mp(b, e)));
}

int rec(int r, int g, int b, int e)
{
    stack<pair<int, pair<int, pair<int, int>>>> st;
    st.push(gett(r, g, b, e));
    while(!st.empty())
    {
        int r = st.top().first, g = st.top().second.first, b = st.top().second.second.first, e = st.top().second.second.second;
        st.pop();
        if(r > R || g > G || b > B)
            continue;
        if(has.find(r * 1000000000LL + g * 1000000LL + b * 1000 + e) != has.end())
            continue;
        has.insert(r * 1000000000LL + g * 1000000LL + b * 1000 + e);

        if(r == R && g == G && b == B && started != e)
            return e;
        if(e == 0)
            st.push(gett(r, g + 1, b, 1)), st.push(gett(r, g, b + 1, 2));
        else if(e == 1)
            st.push(gett(r + 1, g, b, 0)), st.push(gett(r, g, b + 1, 2));
        else
            st.push(gett(r + 1, g, b, 0)), st.push(gett(r, g + 1, b, 1));
    }
    return -1;
}

vector<int> ans;

void recover(int r, int g, int b, int e)
{
    if(r == 0 && g == 0 && b == 0)
        return;
    ans.pb(e);
//    cout << r << " " << g<< " " << b << " " << e << endl;
    if(e == 0)
        r--;
    if(e == 1)
        g--;
    if(e == 2)
        b--;
    for(int i = 0; i < 3; i++)
    {
        if(i == e)
            continue;
        if(has.find(r * 1000000000LL + g * 1000000LL + b * 1000 + i) != has.end())
        {
            recover(r, g, b, i);
            return;
        }
    }
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
        ans.clear();
        int a, b, c, n;
        cin >> n >> R >> a >> G >> b >> B >> c;
        int st = -1;
        if(R)
        {
            has.clear();
            started = 0;
            st = rec(1, 0, 0, 0);
            if(st != -1)
                recover(R, G, B, st);
        }
        if(ans.size() == 0 && G)
        {
            has.clear();
            started = 1;
            st = rec(0, 1, 0, 1);
            if(st != -1)
                recover(R, G, B, st);
        }
        if(ans.size() == 0 && B)
        {
            has.clear();
            started = 2;
            st = rec(0, 0, 1, 2);
            if(st != -1)
                recover(R, G, B, st);
        }
        cerr << "CASE " << tcase << endl;
        cout << "Case #" << tcase << ": ";
        if(ans.size() == 0)
            cout << "IMPOSSIBLE";
        else
        {
            for(int i: ans)
            {
                if(i == 0)
                    cout << "R";
                else if(i == 1)
                    cout << "Y";
                else
                    cout << "B";
            }
        }
        cout << "\n";
    }
    return 0;
}
