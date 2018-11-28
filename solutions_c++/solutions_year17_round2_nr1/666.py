#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define fio ios_base::sync_with_stdio(false)
#define MOD 1000000007
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define range(a, b, c) (a>=b && a<c)
#define stlfor(a, b) for(auto a=b.begin(); a!=b.end(); a++)
#define rstlfor(a, b) for(auto a=b.rbegin(); a!=b.rend(); a++)
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
using namespace std;
using namespace __gnu_pbds;
typedef pair<int, int> pii;
typedef priority_queue<pii, vector<pii>, greater<pii>> min_pq;
typedef tree<pii, null_type, less<pii>, rb_tree_tag, tree_order_statistics_node_update> OST;

const double one = 1;

int main()
{
    fio;
    cout << fixed << setprecision(10);
    int t;
    cin >> t;
    for(int tc=1; tc<=t; tc++)
    {
        int d, n;
        cin >> d >> n;
        double tim = 0;
        for(int i=0; i<n; i++)
        {
            int k, s;
            cin >> k >> s;
            double tt = ((d - k) * one) / s;
            tim = max(tim, tt);
        }
        cout << "Case #" << tc << ": " << d / tim << endl;
    }
    return 0;
}