#include <bits/stdc++.h>
#define forinc(i,a,b) for(int i = a, _key = b; i <= _key; ++i)
#define fordec(i,a,b) for(int i = a, _key = b; i >= _key; --i)
#define fori(i,n) for(int i = 0, _key = n; i < _key; ++i)
#define ford(i,n) for(int i = n - 1; i >= 0; --i)
#define forvct(i,v) for(int i = 0, _key = v.size(); i < _key; ++i)
#define sqr(x) ((ll)x) * (x)
#define task "bs"
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
#define nn 1010

using namespace std;

const int oo = 1000000007;

int l;
ll k, a1[nn], a2[nn], c1[nn], c2[nn];

void check(const ll &x, const ll &v)
{
    if (!x) return;
    if (!a1[l+1]) a1[l+1] = x;
    if (a1[l+1] == x) c1[l+1] += v;
    else
    {
        a2[l+1] = x;
        c2[l+1] += v;
    }
}

void process()
{
    l = 1;
    cin >> a1[1] >> k;
    c1[1] = 1;
    a2[1] = 0;
    c2[1] = 0;
    forinc(i,1,100)
        if (k > c1[l] + c2[l])
        {
            a1[l+1] = a2[l+1] = c1[l+1] = c2[l+1] = 0;
            if (a1[l])
            {
                a1[l]--;
                check(a1[l]/2,c1[l]);
                check(a1[l]-a1[l]/2,c1[l]);
            }
            if (a2[l])
            {
                a2[l]--;
                check(a2[l]/2,c2[l]);
                check(a2[l]-a2[l]/2,c2[l]);
            }
            if (a1[l+1] < a2[l+1])
            {
                swap(a1[l+1],a2[l+1]);
                swap(c1[l+1],c2[l+1]);
            }
            k -= c1[l] + c2[l];
            l++;
        }
        else
        {
            a1[l]--;
            a2[l]--;
            if (k <= c1[l]) cout << a1[l] - a1[l] / 2 << " " << a1[l] / 2 << "\n";
            else cout << a2[l] - a2[l] / 2 << " " << a2[l] / 2 << "\n";
            break;
        }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    //srand(time(NULL));
    //freopen(task".inp","r",stdin);
    //freopen(task".out","w",stdout);
    int tst;
    cin >> tst;
    forinc(t,1,tst)
    {
        cout << "Case #" << t << ": ";
        process();
    }
}
