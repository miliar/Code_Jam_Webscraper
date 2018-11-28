#include <bits/stdc++.h>
using namespace std;
#define fin "GCJ17A3.in"
#define fou "GCJ17A.out"
#define ff(i, a, b) for(int i = a; i <= b; i ++)
#define fd(i, a, b) for(int i = a; i >= b; i --)
#define x first
#define y second
#define endl '\n'
typedef long long data;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
const int N = 1005;

int test, n, k, a[N];
string s;

void read()
{
    cin >> s;
    cin >> k;
    n = s.size();
}

void solve(int Tnumber, int ans = 0)
{
    ff(i, 1, n) a[i] = (s[i - 1] == '+');
    ff(i, 1, n - k + 1)
        if (!a[i])
        {
            ++ ans;
            ff(j, i, i + k - 1)
                a[j] ^= 1;
        }
    ff(i, n - k + 2, n)
        if (!a[i]) ans = -1;
    if (ans == -1) cout << "Case #" << Tnumber << ": IMPOSSIBLE\n";
        else cout << "Case #" << Tnumber << ": " << ans << "\n";
}

int main()
{
    ios_base::sync_with_stdio(0);
    //freopen(fin,"r",stdin), freopen(fou,"w",stdout);

    cin >> test;
    ff(i, 1, test)
    {
        read();
        solve(i);
    }
    return 0;
}
