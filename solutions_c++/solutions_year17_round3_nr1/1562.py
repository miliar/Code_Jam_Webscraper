#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef long long int ll;
typedef vector< pair<int, int> > vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<long long int> vll;
typedef pair<int, int> pii;

const ll INF = 1e18;
const int inf = 1e9;
const int MOD = 1e9 + 7;
const int nax = 1000000 + 10;

double r[nax], h[nax];
vector< pair< double, pair<double, int> > > v;
vector< pair< pair<double, double>, int> >v1;
const double pi = acos(-1);

int main()
{
    ios::sync_with_stdio(0);

    freopen("input1.in", "r", stdin);
    freopen("output1.txt", "w", stdout);

    int t; cin >> t;
    int test = 0;
    while(t--)
    {
        test++;
        v.clear();
        v1.clear();
        int n; cin >> n;
        int k; cin >> k;

        for(int i = 1; i <= n; i++)
        {
            cin >> r[i] >> h[i];

            v.pb(mp(r[i] * h[i] , mp(r[i], i)));
            v1.pb(mp(mp(r[i], h[i]),(i)));
        }
        sort(v1.begin(), v1.end());
        reverse(v1.begin(), v1.end());
        sort(v.begin(), v.end());

        double maxi = 0;

        for(int i = 0; i <= n - k; i++)
        {
            double cur = pi * v1[i].ff.ff * v1[i].ff.ff;
            double rhsum = v1[i].ff.ff * v1[i].ff.ss;
            int taken = 1;
            for(int j = n - 1; j >= 0; j--)
            {
                if(taken == k)
                    break;

                if(v[j].ss.ff <= v1[i].ff.ff && v[j].ss.ss != v1[i].ss)
                {
                    taken++;
                    rhsum += v[j].ff;
                }

            }
            cur += 2 * pi * rhsum;
            //cout << cur << endl;
            maxi = max(maxi, cur);
        }
        cout << "Case #" << test << ": ";
        cout << fixed << setprecision(8) << maxi << endl;

    }

    return 0;
}
