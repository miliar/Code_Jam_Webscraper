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

double arr[nax],s[nax];

int main()
{
    freopen("input1.in", "r", stdin);
    freopen("output1.txt", "w", stdout);

    ios::sync_with_stdio(0);
    int t;
    cin >> t;
    int test = 0;
    while(t--)
    {
        ++test;
        double d;
        int n;
        cin >> d >> n;
        double mt = 0;
        for(int i = 1; i <= n; i++)
        {
            cin >> arr[i] >> s[i];
            double t = (d - arr[i]) / s[i];
            mt = max(mt, t);
        }
        double ans = d / mt;
        cout << "Case #"<<test<<": ";
        cout << fixed << setprecision(8) << ans << endl;
    }
    return 0;
}
