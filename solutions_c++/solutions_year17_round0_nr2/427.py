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

ll n;
int t, m, a[20], f[20][10][2];

int cal(int x, int last, int ok)
{
    if (x < 0) return 1;
    if (f[x][last][ok] != -1) return f[x][last][ok];
    int tmp = 0, imax;
    if (ok) imax = 9; else imax = a[x];
    f(i, last, imax)
        tmp |= cal(x - 1, i, ok | (i < a[x]));
    f[x][last][ok] = tmp;
    return tmp;
}

void trace(int x, int last, int ok1, int ok2)
{
    if (x < 0)
    {
        cout << endl;
        return;
    }
    int imax;
    if (ok1) imax = 9; else imax = a[x];
    fd(i, imax, last)
        if (cal(x - 1, i, ok1 | (i < a[x])))
        {
            if (i != 0 || ok2) cout << i;
            trace(x - 1, i, ok1 | (i < a[x]), ok2 | (i != 0));
            return;
        }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin >> t;
    f(tt, 1, t)
    {
        memset(f, 255, sizeof(f));
        cin >> n;
        m = 0;
        while (n > 0)
        {
            a[m++] = n % 10;
            n /= 10;
        }
        cout << "Case #" << tt << ": ";
        trace(m - 1, 0, 0, 0);
    }
}
