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
        int n, k;
        cin >> n >> k;
        priority_queue<int> q;
        int lsp;
        q.push(n);
        while(k--)
        {
            int x = q.top();
            q.pop();
            if(x > 2)
            {
                q.push(x - 1 >> 1);
                q.push(x >> 1);
            }
            else if(x == 2)
                q.push(1);
            lsp = x;
        }
        cout << "Case #" << tc << ": " << (lsp >> 1) << " " << (lsp - 1 >> 1) << endl;
    }
    return 0;
}