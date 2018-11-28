#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl
#define pb push_back
using namespace std;
typedef long long ll;


const int MAXN = 100005;

void cans(int test, int ans)
{
    cout << "Case #" << test << ": " << ans << endl;
}


int main()
{
    freopen("input.txt", "r", stdin);
        freopen("out.txt", "w", stdout);

    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        ll n, k;
        cin >> n >> k;
        ll a = n;
        ll ca = 1;
        ll b = n+1;
        ll cb = 0;

        cout << "Case #" << tt << ": ";
        while(true)
        {
            if (k <= cb)
            {
                cout << (a+1)/2 << " " << a / 2;
                break;
            }
            else if (k <= ca + cb)
            {
                cout << a/2 << " " << (a-1) / 2;
                break;
            }
            else
            {
                k -= ca + cb;
                if (a % 2 == 0)
                    cb = 2*cb + ca;
                else
                    ca = 2*ca + cb;
                a = (a-1)/2;
            }
            //cout << k << " " << ca << " " << cb << endl;
        }
        cout << endl;
    }

    return 0;
}


