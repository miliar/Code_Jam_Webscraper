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

int n;
long double d;

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
    cout.precision(6);
    cout << fixed;
    forinc(t,1,tst)
    {
        cout << "Case #" << t << ": ";
        long double tt = 0;
        cin >> d >> n;
        forinc(i,1,n)
        {
            long double x, y;
            cin >> x >> y;
            tt = max(tt,(d - x) / y);
        }
        cout << d / tt << "\n";
    }
}
