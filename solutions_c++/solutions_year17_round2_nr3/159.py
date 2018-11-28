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
#define nn 110

using namespace std;

const ll oo = 100000000000000007ll;

int n, q;
ll e[nn], s[nn], d[nn][nn];
long double dis[nn];
heap<pair<long double,int>, vector<pair<long double,int> >, greater<pair<long double,int> > > h;

void enter()
{
    cin >> n >> q;
    forinc(i,1,n) cin >> e[i] >> s[i];
    forinc(i,1,n)
        forinc(j,1,n)
        {
            cin >> d[i][j];
            if (d[i][j] == -1) d[i][j] = oo;
        }
    forinc(i,1,n) d[i][i] = 0;
    forinc(k,1,n)
    forinc(i,1,n)
    forinc(j,1,n)
        d[i][j] = min(d[i][j],d[i][k] + d[k][j]);
}

void query(const int &st, const int &tt)
{
    forinc(i,1,n) dis[i] = oo;
    dis[st] = 0;
    h.push(m_p(0,st));
    while (!h.empty())
    {
        int u = h.top().nd;
        if (dis[u] != h.top().st)
        {
            h.pop();
            continue;
        }
        h.pop();
        forinc(v,1,n)
            if (d[u][v] <= e[u] && dis[v] > dis[u] + (long double) d[u][v] / s[u])
            {
                dis[v] = dis[u] + (long double) d[u][v] / s[u];
                h.push(m_p(dis[v],v));
            }
    }
    if (dis[tt] == oo) dis[tt] = -1;
    cout << dis[tt] << " ";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    //srand(time(NULL));
    freopen(task".inp","r",stdin);
    freopen(task".out","w",stdout);
    cout.precision(10);
    cout << fixed;
    int tst;
    cin >> tst;
    forinc(t,1,tst)
    {
        cout << "Case #" << t <<": ";
        enter();
        forinc(i,1,q)
        {
            int u, v;
            cin >> u >> v;
            query(u,v);
        }
        cout << "\n";
    }
}
