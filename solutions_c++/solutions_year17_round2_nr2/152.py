#include <bits/stdc++.h>
#define forinc(i,a,b) for(int i = a, _key = b; i <= _key; ++i)
#define fordec(i,a,b) for(int i = a, _key = b; i >= _key; --i)
#define fori(i,n) for(int i = 0, _key = n; i < _key; ++i)
#define ford(i,n) for(int i = n - 1; i >= 0; --i)
#define forvct(i,v) for(int i = 0, _key = v.size(); i < _key; ++i)
#define sqr(x) ((ll)x) * (x)
#define task "x"
#define st first
#define nd second
#define m_p make_pair
#define m_t make_tuple
#define p_b push_back
#define p_f push_front
#define pp_b pop_back
#define pp_f pop_front
#define sn string::npos
#define heap priority_queue
#define ll long long
#define db double
#define str string
#define nn 100010

using namespace std;

const int oo = 1000000007;

int n, r, o, y, g, b, v, a[nn], c[5], p[5];

bool process()
{
    //cerr << n << "\n";
    if (r < g) return false;
    if (r == g && r)
    {
        if (r + g != n) return false;
        forinc(i,1,r) cout << "RG";
        return true;
    }
    r -= g;
    n -= 2 * g;
    //cerr << n << "\n";
    if (y < v) return false;
    if (y == v && y)
    {
        if (y + v != n) return false;
        forinc(i,1,y) cout << "YV";
        return true;
    }
    y -= v;
    n -= 2 * v;
    //cerr << n << "\n";
    if (b < o) return false;
    if (b == o && b)
    {
        if (b + o != n) return false;
        forinc(i,1,b) cout << "BO";
        return true;
    }
    b -= o;
    n -= 2 * o;
    //cerr << n << "\n";
    if (r > n / 2 || y > n / 2 || b > n / 2) return false;
    c[1] = r, c[2] = y, c[3] = b;
    p[1] = 1, p[2] = 2, p[3] = 3;
    forinc(i,1,2)
        forinc(j,i+1,3)
            if (c[p[i]] < c[p[j]]) swap(p[i],p[j]);
    //forinc(i,1,3) cerr << c[p[i]] << " ";
    for(int i = 1; i <= n; i += 2)
        if (c[p[1]])
        {
            a[i] = p[1];
            c[p[1]]--;
        }
        else
        if (c[p[2]])
        {
            a[i] = p[2];
            c[p[2]]--;
        }
        else
        if (c[p[3]])
        {
            a[i] = p[3];
            c[p[3]]--;
        }
    for(int i = 2; i <= n; i += 2)
        if (c[p[1]])
        {
            a[i] = p[1];
            c[p[1]]--;
        }
        else
        if (c[p[2]])
        {
            a[i] = p[2];
            c[p[2]]--;
        }
        else
        if (c[p[3]])
        {
            a[i] = p[3];
            c[p[3]]--;
        }
    bool pr = false, py = false, pb = false;
    forinc(i,1,n)
        if (a[i] == 1)
        {
            cout << "R";
            if (!pr)
            {
                forinc(j,1,g) cout << "GR";
                pr = true;
            }
        }
        else
        if (a[i] == 2)
        {
            cout << "Y";
            if (!py)
            {
                forinc(j,1,v) cout << "VY";
                py = true;
            }
        }
        else
        if (a[i] == 3)
        {
            cout << "B";
            if (!pb)
            {
                forinc(j,1,o) cout << "OB";
                pb = true;
            }
        }
    //cerr << "\n";
    //cerr << n << "\n";
    //forinc(i,1,n) cerr << a[i] << " ";
    return true;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    //srand(time(NULL));
    freopen(task".inp","r",stdin);
    freopen(task".out","w",stdout);
    int tst;
    cin >> tst;
    forinc(t,1,tst)
    {
        cout << "Case #" << t << ": ";
        cin >> n >> r >> o >> y >> g >> b >> v;
        if (process()) cout << "\n"; else cout << "IMPOSSIBLE\n";
    }
}
