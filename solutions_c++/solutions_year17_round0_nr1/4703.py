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
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> OST;

int main()
{
    fio;
    int t;
    cin >> t;
    for(int tc=1; tc<=t; tc++)
    {
        string s;
        int k;
        cin >> s >> k;
        int n = s.length();
        vector<int> v(n, 0);
        for(int i=0; i<n; i++)
            if(s[i] == '+')
                v[i] = 1;
        int lim = n - k, ans = 0;
        for(int i=0; i<=lim; i++)
        {
            if(v[i] == 0)
            {
                ans++;
                for(int j=0; j<k; j++)
                    v[i+j] ^= 1;
            }
        }
        int flag = true;
        for(int i=lim+1; i<n; i++)
        {
            if(v[i] == 0)
            {
                flag = false;
                break;
            }
        }
        cout << "Case #" << tc << ": ";
        if(flag)
            cout << ans << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}