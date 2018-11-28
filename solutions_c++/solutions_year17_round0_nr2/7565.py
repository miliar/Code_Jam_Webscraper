#include <bits/stdc++.h>
#define forinc(i,a,b) for(int i = a, _key = b; i <= _key; ++i)
#define fordec(i,a,b) for(int i = a, _key = b; i >= _key; --i)
#define fori(i,n) for(int i = 0, _key = n; i < _key; ++i)
#define ford(i,n) for(int i = n - 1; i >= 0; --i)
#define forvct(i,v) for(int i = 0, _key = v.size(); i < _key; ++i)
#define sqr(x) ((ll)x) * (x)
#define task "td"
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

int l, a[30];

void enter()
{
    ll n;
    cin >> n;
    l = 0;
    while (n)
    {
        a[++l] = n % 10;
        n /= 10;
    }
}

bool backtrack(const int &i, const int &x, const ll &s, const bool &o)
{
    if (i == 0)
    {
        cout << s << "\n";
        return true;
    }
    int t = a[i];
    if (o) t = 9;
    fordec(d,t,x)
    {
        bool _o = (o || d < a[i]);
        if (backtrack(i-1,d,s*10+d,_o)) return true;
    }
    return false;
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
    forinc(tt,1,tst)
    {
        cout << "Case #" << tt << ": ";
        enter();
        backtrack(l,0,0,0);
    }
}
