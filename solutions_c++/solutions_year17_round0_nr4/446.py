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

struct cell
{
    int x, y;
    char c;
};

cell make_trip(int x, int y, char c)
{
    cell res;
    res.x = x;
    res.y = y;
    res.c = c;
    return res;
}

int t, n, m, res;
char a[105][105], b[105][105];
vector<cell> res1;

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D.ou", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin >> t;
    f(tt, 1, t)
    {
        cin >> n >> m;
        f(i, 1, n)
            f(j, 1, n)
            {
                b[i][j] = '.';
                a[i][j] = '.';
            }
        int yy = 0;;
        f(i, 1, m)
        {
            char ch;
            int x,  y;
            cin >> ch >> x >> y;
            a[x][y] = ch;
            if (ch != '+') yy = y;
        }
        if (yy == 0) yy = 1;
        f(i, 1, n)
            if (i == yy) b[1][i] = 'o'; else b[1][i] = '+';
        int y1 = n;;
        f(i, 2, n)
        {
            if (y1 == yy) y1--;
            if (y1 > 0) b[i][y1] = 'x';
            y1--;
        }
        if (yy == 1)
        {
            b[n][2] = 'o';
            f(i, 3, n - 1)
                b[n][i] = '+';
        } else
        {
            f(i, 2, n - 1)
                b[n][i] = '+';
        }
        res = 0;
        res1.clear();
        if (n == 2)
        {
            f(i, 1, 2)
                if (i == yy) b[1][i] = 'o'; else b[1][i] = '+';
            f(i, 1, 2)
                if (i == yy) b[2][i] = '.'; else b[2][i] = 'x';
        }
        f(i, 1, n)
        {
            f(j, 1, n)
            {
                if (b[i][j] == '+' || b[i][j] == 'x') res++;
                if (b[i][j] == 'o') res += 2;
                if (b[i][j] != a[i][j]) res1.pb(make_trip(i, j, b[i][j]));
            }
        }
        cout << "Case #" << tt << ": " << res << " " << res1.size() << endl;
        f(i, 0, (int)res1.size() - 1)
            cout << res1[i].c << " " << res1[i].x << " " << res1[i].y << endl;
    }
    return 0;
}
