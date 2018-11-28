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

int t, n, p, r[55], q[55][55], pointer[55], mi[55], ma[55];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B.ou", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin >> t;
    f(tt, 1, t)
    {
        cin >> n >> p;
        f(i, 1, n)
            cin >> r[i];
        f(i, 1, n)
            f(j, 1, p)
                cin >> q[i][j];
        f(i, 1, n)
        {
            pointer[i] = 1;
            sort(q[i] + 1, q[i] + p + 1);
        }
        int res = 0;
        int currdish = 1;
        while (1)
        {
            f(i, 1, n)
            {
                mi[i] = currdish * r[i] * 9 / 10;
                ma[i] = currdish * r[i] * 11 / 10;
            }
            bool over = false;
            f(i, 1, n)
                while (q[i][pointer[i]] < mi[i] && pointer[i] <= p) pointer[i]++;
            f(i, 1, n)
                if (pointer[i] > p)
                {
                    over = true;
                    break;
                }
            if (over) break;
            int ok = 1;
            f(i, 1, n)
                if (q[i][pointer[i]] > ma[i])
                {
                    ok = 0;
                    break;
                }
            if (ok)
            {
                res++;
                f(i, 1, n)
                    pointer[i]++;
            } else currdish++;
        }
        cout << "Case #" << tt << ": " << res << endl;
    }
    return 0;
}
