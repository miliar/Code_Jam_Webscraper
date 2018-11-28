#include <bits/stdc++.h>

using namespace std;

#define all(v) (v).begin(), (v).end()

using li = long long;

void solve()
{
    int n, k;
    cin >> n >> k;
    k--;
    
    vector<pair<int, int>> p(n);
    for (int i = 0; i < n; i++)
        cin >> p[i].first >> p[i].second;
    
    sort(all(p), [](pair<int, int> a, pair<int, int> b) { return a.first * (li)a.second > b.first * (li)b.second; });
    
    vector<li> prefSum(n);
    for (int i = 0; i < n; i++)
        prefSum[i] = (i ? prefSum[i - 1] : 0) + p[i].first * (li)p[i].second;
    
    li answer = 0;
    for (int i = 0; i < n; i++)
    {
        li rMax = p[i].first;
        li sum = 0;
        
        if (i >= k)
            sum = (k - 1 >= 0 ? prefSum[k - 1] : 0) + p[i].first * (li)p[i].second;
        else
            sum = (k >= 0 ? prefSum[k] : 0);
        
        answer = max(answer, rMax * (li)rMax + sum * 2);
    }
    
    long double PI = acosl(-1);
    cout << fixed << setprecision(12) << PI * answer << endl;
}

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
