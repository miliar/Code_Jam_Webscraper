#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i= a; i<= b; i++)
#define FORD(i,a,b) for(int i= a; i>= b; i--)
#define For(i,a,b) for(int i= a; i< b; i++)
#define Ford(i,a,b) for(int i= a; i> b; i--)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define Fill(s,a) memset(s,a,sizeof(s))
#define pb push_back
#define mp make_pair
#define ALL(x) (x).begin(),(x).end()
#define fi first
#define se second

using namespace std;

typedef long long ll;
typedef vector<ll> vi;
typedef pair<int, int> pii;
typedef unsigned long long ull;

int tests;
ll k, n, rmin, rmax;
vi a;
map<ll, ll> M;


void process(int test)
{
    a.clear();
    a.pb(n);
    M.clear();
    M[n] = 1;
    int i = 0;
    while (i < a.size())
    {
        ll p = a[i++];
        if (p == 1 || p == 0) continue;
        ll mid = (p + 1)/2;
        if (p % 2 == 1)
        {
            if (M.find(mid-1) == M.end())
            {
                a.pb(mid - 1);
                M[mid - 1] = 0;
            }
            M[mid - 1] += 2 * M[p];
        }
        else
        {
            if (M.find(p-mid) == M.end())
            {
                a.pb(p - mid);
                M[p - mid] = 0;
            }
            M[p - mid] += M[p];

            if (M.find(mid-1) == M.end())
            {
                a.pb(mid - 1);
                M[mid - 1] = 0;
            }
            M[mid - 1] += M[p];


        }
    }
    //sort(a.begin(),a.end(),greater<ll>());
    int t = a.size();
    if (a[t-1] == 0)
        t--;
    /*
    ll cnt1 = 0;
    For(i,0,t)
        {
            cout << a[i] << " " << M[a[i]] << endl;
            cnt1 += M[a[i]];

        }
    //cout << cnt1 << endl;
    if (cnt1 != n) cout << cnt1 << " "<< "SSS" << endl;

    */

    ll cnt = 0;
    For(i,0,t)
        if (cnt + M[a[i]] >= k)
        {
            ll mid = (a[i] + 1)/2;
            rmin = min(mid - 1,a[i] - mid);
            rmax = max(mid - 1,a[i] - mid);
            break;
        }
        else cnt += M[a[i]];

    cout << "Case #" << test << ": " << rmax << " " << rmin << endl;
}

int main()
{
    //ios_base::sync_with_stdio(false);
    freopen("C3.in","r",stdin);
    freopen("C3.out","w",stdout);
    cin >> tests;
    FOR(t,1,tests)
    {
        cin >> n >> k;
        process(t);
    }
    return 0;
}


