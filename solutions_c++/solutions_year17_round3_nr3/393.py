#include <bits/stdc++.h>

using namespace std;

#define all(v) (v).begin(), (v).end()

using li = long long;

void solve()
{
    int n, k;
    cin >> n >> k;
    assert(n == k);
    
    double u;
    cin >> u;
    
    vector<double> p(n);
    for (int i = 0; i < n; i++)
        cin >> p[i];
    
    sort(all(p));
    
    for (int t = 0; t < n; t++)
    {
        int i = 0;
        while (i + 1 < n && abs(p[i + 1] - p[0]) < 1e-9) i++;
        
        // 0..i are equal
        
        double next = (i + 1 < n ? p[i + 1] : 2);
        double can = min(u / (i + 1), next - p[0]);
        
        for (int j = 0; j <= i; j++)
            p[j] += can;
        
        u -= can * (i + 1);
    }
    assert(abs(u) < 1e-9);
    
    double prob = 1;
    for (int i = 0; i < n; i++)
        prob *= p[i];
    
    cout << fixed << setprecision(12) << prob << endl;
}

// prob N function -> max
// prod (p_i + c_i) -> max
// sum c_i <= U

int main()
{
    int nt;
    cin >> nt;
    
    for (int i = 0; i < nt; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    
    return 0;
}
