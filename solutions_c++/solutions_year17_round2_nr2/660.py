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

char col[] = {'R', 'O', 'Y', 'G', 'B', 'V'};

int main()
{
    fio;
    int t;
    cin >> t;
    for(int tc=1; tc<=t; tc++)
    {
        int n, c[6];
        cin >> n;
        int m = -1, mc;
        for(int i=0; i<6; i++)
        {
            cin >> c[i];
            if(c[i] > m and c[i])
            {
                m = c[i];
                mc = i;
            }
        }
        cout << "Case #" << tc << ": ";
        if(m + m > n)
        {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        vector<char> v;
        for(int k=0; k<n; k++)
        {
            v.pb(col[mc]);
            c[mc]--;
            int tm = -1, tmc;
            for(int i=0; i<6; i+=2)
            {
                if(i != mc and c[i] > tm and c[i])
                {
                    tm = c[i];
                    tmc = i;
                }
            }
            mc = tmc;
        }
        if(v[0] == v[v.size()-1])
            swap(v[v.size()-1], v[v.size()-2]);
        for(int i=0; i<v.size(); i++)
        {
            cout << v[i];
            assert(v[i] != v[(i-1+int(v.size())) % int(v.size())]);
        }
        cout << endl;
    }
    return 0;
}