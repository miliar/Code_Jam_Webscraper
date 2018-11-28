#include <bits/stdc++.h>
using namespace std;
#pragma GCC diagnostic ignored "-Wmissing-declarations"

#define FINAL_OUT(x) {cout << (x) << '\n'; exit(0);}

#define SHOW(x) std::cout << #x << " = " << x << std::endl;

inline int safe_mul(int x, int y) __attribute__ ((warn_unused_result));


inline void maxs(int& x, int y)
{
    x = max(x, y);
}


void solve(int numtest)
{
    int n,c,m;
    cin >> n >> c >> m;

    vector<int> numpla(c + 1, 0);
    vector<int> numt(n + 1, 0);

    for(int i = 0; i < m; ++i)
    {
        int p,b;
        cin >> p >> b;
        ++numt[p];
        ++numpla[b];
    }

    int l = (*max_element(begin(numpla), end(numpla))) - 1;
    int r = 10001;

    while (r - l > 1)
    {
        int mid = (l + r) >> 1;

        bool flag = true;

        int cnt_free = 0;
        for(int i = 1; i <= n; ++i)
        {
            cnt_free += mid;
            cnt_free -= numt[i];
            if (cnt_free < 0)
                flag = false;
        }

        if (flag)
            r = mid;
        else
            l = mid;
    }

    int res = 0;
    for(int i = 1; i <= n; ++i)
        res += max(0, numt[i] - r);

    cout << "Case #" << numtest << ": " << r << ' ' << res << endl;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    //freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i)
        solve(i);
}
