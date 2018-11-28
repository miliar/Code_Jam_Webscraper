#include <bits/stdc++.h>
using namespace std;
#define fin "GCJ17B.in"
#define fou "GCJ17B.out"
#define ff(i, a, b) for(int i = a; i <= b; i ++)
#define fd(i, a, b) for(int i = a; i >= b; i --)
#define x first
#define y second
#define endl '\n'
typedef long long data;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int test;
data n;

void read()
{
    cin >> n;
}

bool check(int x, int last)
{
    if (x == 0) return true;
    if (x % 10 > last) return false;
    return check(x / 10, x % 10);
}

void solve(int Tnumber)
{
    cout << "Case #" << Tnumber << ": ";
    if (n <= 1e6)
    {
        fd(i, n, 1)
            if (check(i, 9))
            {
                cout << i << '\n';
                return;
            }
    }
    else {

    }
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
