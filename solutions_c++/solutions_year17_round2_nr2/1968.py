#include <bits/stdc++.h>
using namespace std;
#define fin "B-small-attempt2.in"
#define fou "B.out"
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

int test, n, a[7];
char ch[7] = { '0', 'R', 'O', 'Y', 'G', 'B', 'V'};
string s;

void read()
{
    cin >> n ;
    ff(i, 1, 6) cin >> a[i];
}

inline bool ok(int x)
{
    return s[s.size() - 1] != ch[x];
}

int getBit(int x, int k)
{
    return (x >> (k - 1)) & 1;
}

int best(int X)
{
    int r = 0;
    ff(i, 1, 6)
        if (getBit(X, i)) {r = i; break;}
    ff(i, 1, 6)
        if (getBit(X, i) && a[i] > a[r]) r = i;
    return r;
}

void solve(int tnum)
{
    s = "";
    if (a[1] > 0) s += 'R', a[1]--;
    else if (a[3] > 0) s += 'Y', a[3]--;
    else if (a[5] > 0) s += 'B', a[5]--;
   // cerr << tnum << endl;
    while (a[1] + a[3] + a[5] > 0)
    {
        int X = ok(1) * (a[1] > 0) + ok(3) * 4 * (a[3] > 0) + ok(5) * 16 * (a[5] > 0);
        if (X == 0)
        {
            cout << "Case #" << tnum << ": IMPOSSIBLE\n";
            return;
        }
       // cerr << ok(1) << " " <<ok(3) <<" " <<ok(5) << endl;
        int c = best(X);
        s += ch[c];
       // cerr << ch[c] << endl;
        a[c] --;
    }

    if (s.size() >= 2 && s[0] == s[s.size() - 1])
    {
        cout << "Case #" << tnum << ": IMPOSSIBLE\n";
            return;
    }
    cout << "Case #" << tnum << ": " << s << '\n';
}

int main()
{
    ios_base::sync_with_stdio(0);
    freopen(fin,"r",stdin), freopen(fou,"w",stdout);

    cin >> test;
    ff(i, 1, test)
    read(),
    solve(i);
    return 0;
}
