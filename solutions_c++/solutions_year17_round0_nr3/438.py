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

ll n, k;
int t;

void write(ll x)
{
    if (x % 2 == 0) cout << x / 2 << " " << x / 2 - 1; else cout << x / 2 << " " << x / 2;
    cout << endl;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin >> t;
    f(tt, 1, t)
    {
        cin >> n >> k;
        cout << "Case #" << tt << ": ";
        ll big = 1;
        ll small = 0;
        f(i, 0, 70)
        {
            if (k > 1ll * 1 << i) k -= 1ll * 1 << i; else
            {
                if (k <= big) write(n / (1ll * 1 << i)); else write(n / (1ll * 1 << i) - 1);
                break;
            }
            ll nsmall, nbig;
            if ((n / (1ll * 1 << i)) % 2 == 0)
            {
                nsmall = big + small * 2;
                nbig = big;
            } else
            {
                nsmall = small;
                nbig = big * 2 + small;
            }
            big = nbig;
            small = nsmall;
        }
    }
    return 0;
}
