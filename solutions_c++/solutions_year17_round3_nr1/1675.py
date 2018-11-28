#include <bits/stdc++.h>
#define F first
#define S second
typedef long long ll;
using namespace std;
const double PI = 3.1415926535897932384626433832795028841971693993751058209749;
int main()
{
    int t, tt, n, k;
    cin>>t;
    cout<<fixed<<setprecision(10);
    for(int tt = 1; tt <= t; tt++)
    {
        cin>>n>>k;
        pair<double, double> dim[n];
        for(int i = 0; i < n; i++)
        {
            cin>>dim[i].F>>dim[i].S;
        }
        sort(dim, dim+n);
        reverse(dim, dim+n);

        double area = 0;
        double maxar = 0;

        for(int i = 0; i <= n-k; i++)
        {
            priority_queue<ll> q;
            area = dim[i].F*dim[i].F + 2*dim[i].F*dim[i].S;
            for(int j = i+1; j < n; j++)
            {
                q.push(2*dim[j].F*dim[j].S);
            }
            int cnt = k - 1;
            for (int x = 0; x < k-1; x++)
            {
                area += q.top();
                q.pop();
            }
            maxar = max(maxar, area);
        }

        maxar *= PI;

        cout<<"Case #"<<tt<<": "<<maxar<<"\n";
    }
    return 0;
}
