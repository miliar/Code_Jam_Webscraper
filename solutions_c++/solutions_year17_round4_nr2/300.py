#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

typedef long double ld;

const ld EPS = 1e-9;

const ll llinf = 1e18 + 100;

const int maxn = 1100, inf = 1e9 + 100;

int tst;

int n, C, g;

vector<int> q[maxn];

int ans;

int s[maxn];

bool check(int val){
    for (int i = 0; i < C; i++)
        s[i] = val;
    int rem = 0;
    ans = 0;
    for (int i = 0; i < n; i++){
        int d = val;
        int x = 0;
        for (int j = 0; j < q[i].size(); j++){
            if (j > 0 && q[i][j] != q[i][j - 1]){
                if (s[q[i][j - 1]] < x)
                    return 0;
                s[q[i][j - 1]] -= x;
                int vl = min(d, x);
                d -= vl;
                x -= vl;
                if (rem >= x)
                    rem -= x, ans += x, x = 0;
                else
                    return 0;
            }
            x++;
        }
        if (x > 0){
            if (s[q[i].back()] < x)
                return 0;
            s[q[i].back()] -= x;
            int vl = min(d, x);
            d -= vl;
            x -= vl;
            if (rem >= x)
                rem -= x, ans += x, x = 0;
            else
                return 0;
        }
        rem += d;
    }
    return 1;
}

int main()
{
    #ifdef ONPC
    ifstream cin("a.in");
    ofstream cout("a.out");
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
	    #ifndef STR
	    //ifstream cin("a.in");
	    //ofstream cout("a.out");
	    //freopen("a.in", "r", stdin);
	    //freopen("a.out", "w", stdout);
    	    #endif // STR
    #endif // ONPC
    ios::sync_with_stdio(0);
    cin >> tst;
    for (int iter = 1; iter <= tst; iter++){
        cin >> n >> C >> g;
        for (int i = 0; i < n; i++)
            q[i].clear();
        for (int i = 0; i < g; i++){
            int p, x;
            cin >> p >> x;
            q[p - 1].push_back(x - 1);
        }
        for (int i = 0; i < n; i++)
            sort(q[i].begin(), q[i].end());
        int l = 0, r = g;
        while (r - l > 1){
            int m = (l + r) / 2;
            if (check(m))
                r = m;
            else
                l = m;
        }
        check(r);
        cout << "Case #" << iter << ": " << r << ' ' << ans << '\n';
    }
}
