#include <bits/stdc++.h>


#define f(i, a, b) for(int i = a; i <= b; i++)
#define fd(i, a, b) for(int i = a; i >= b; i--)
#define fin ""
#define fou ""
#define mp make_pair
#define fi first
#define se second
#define pb push_back

using namespace std;


typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

int t, n, p, a[105];

int main()
{
    ios_base::sync_with_stdio(0);
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.ou", "w", stdout);
    cin >> t;
    f(tt, 1, t)
    {
        cin >> n >> p;
        f(i, 1, n)
            cin >> a[i];
        if (p == 2)
        {
            int cnt = 0;
            f(i, 1, n)
                if (a[i] % 2 == 1) cnt++;
            cout << "Case #" << tt << ": " << n - cnt / 2 << endl;
        }
        if (p == 3)
        {
            int cnt1 = 0;
            int cnt2 = 0;
            f(i, 1, n)
                if (a[i] % 3 == 1) cnt1++; else if (a[i] % 3 == 2) cnt2++;
            int res = n - min(cnt1, cnt2);
            int remain = max(cnt1, cnt2) - min(cnt1, cnt2);
            res -= (remain / 3 * 2 + (remain % 3 == 2));
            cout << "Case #" << tt << ": " << res << endl;
        }
    }
    return 0;
}
