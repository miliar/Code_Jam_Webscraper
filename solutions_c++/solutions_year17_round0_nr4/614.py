#include <bits/stdc++.h>
#define forinc(i,a,b) for(int i = a, _key = b; i <= _key; ++i)
#define fordec(i,a,b) for(int i = a, _key = b; i >= _key; --i)
#define fori(i,n) for(int i = 0, _key = n; i < _key; ++i)
#define ford(i,n) for(int i = n - 1; i >= 0; --i)
#define forvct(i,v) for(int i = 0, _key = v.size(); i < _key; ++i)
#define sqr(x) ((ll)x) * (x)
#define task "fs"
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

using namespace std;

const int oo = 1000000007;

int n, m, res, cnt, tt, tst, a[110][110], ax[10010], ay[10010], az[10010], m1[110], m2[110], pass[210], r1[110], c1[110], r2[210], c2[210];

bool find1(const int &i)
{
    if (pass[i] == tt) return false;
    pass[i] = tt;
    forinc(j,1,n)
        if (c1[j] == 0 || (c1[j] != -1 && find1(c1[j])))
        {
            c1[j] = i;
            r1[i] = j;
            return true;
        }
    return false;
}

bool match(int x, int y)
{
    y -= n;
    if ((x + y) & 1) return false;
    int i = (x + y) >> 1, j = x - i;
    return 1 <= i && i <= n && 1 <= j && j <= n;
}

bool find2(const int &i)
{
    if (pass[i] == tt) return false;
    pass[i] = tt;
    forinc(j,1,2*n-1)
        if (match(i,j) && (c2[j] == 0 || (c2[j] != -1 && find2(c2[j]))))
        {
            c2[j] = i;
            r2[i] = j;
            return true;
        }
    return false;
}

void process()
{
    res = cnt = 0;
    cin >> n >> m;
    memset(a,0,sizeof a);
    memset(r1,false,sizeof r1);
    memset(c1,false,sizeof c1);
    memset(r2,false,sizeof c2);
    memset(c2,false,sizeof c2);
    forinc(i,1,m)
    {
        char c; int x, y, z;
        cin >> c >> x >> y;
        if (c == '+') z = 1;
        else
        if (c == 'x') z = 2;
        else z = 3;
        a[x][y] = z;
        if (z & 2)
        {
            res++;
            r1[x] = -1;
            c1[y] = -1;
        }
        if (z & 1)
        {
            res++;
            r2[x+y] = -1;
            c2[x-y+n] = -1;
        }
    }
    forinc(i,1,n)
        if (r1[i] != -1)
        {
            tt++;
            if (find1(i)) res++;
        }
    forinc(i,2,2*n)
        if (r2[i] != -1)
        {
            tt++;
            if (find2(i)) res++;
        }
    forinc(i,1,n)
        forinc(j,1,n)
        {
            int x = a[i][j];
            if (r1[i] == j) x |= 2;
            if (r2[i+j] == i - j + n) x |= 1;
            if (a[i][j] != x)
            {
                cnt++;
                ax[cnt] = i;
                ay[cnt] = j;
                az[cnt] = x;
            }
        }
    cout << res << " " << cnt << "\n";
    forinc(i,1,cnt)
    {
        if (az[i] == 1) cout << "+ ";
        else
        if (az[i] == 2) cout << "x ";
        else cout << "o ";
        cout << ax[i] << " " << ay[i] << "\n";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    //srand(time(NULL));
    freopen(task".inp","r",stdin);
    freopen(task".out","w",stdout);
    int test;
    cin >> test;
    forinc(tst,1,test)
    {
        cout << "Case #" << tst << ": ";
        process();
    }
}
