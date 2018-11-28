#include <bits/stdc++.h>
#define ll long long
#define int long long
#define F first
#define S second
using namespace std;

const int N = 1e5 + 10;

int n, m;
pair <int, int> t[N];
const double PI = 3.14159265359;

void sol() {
    cin >> n >> m;
    for(int i = 1; i <= n; i++) {
        cin >> t[i].F >> t[i].S;
    }
    sort(t + 1, t + 1 + n);
    reverse(t + 1, t + 1 + n);
    double maxl = 0;
    for(int l = 1; l <= n; l++) {
        vector <double> lst;
        for(int j = 1; j + l <= n; j++) {
            lst.push_back(t[j + l].F * PI * t[j + l].S * 2);
        }
        sort(lst.rbegin(), lst.rend());
        double ans = t[l].F * t[l].F * PI + t[l].F * PI * t[l].S * 2;
        if(lst.size() < m - 1) break;
        for(int i = 0; i < m - 1; i++) {
            ans += lst[i];
        }
        maxl = max(maxl, ans);
    }
    printf("%.10f", maxl);
}

main() {
    freopen("A-large (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);
    //ios_base::sync_with_stdio(0);
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        cout << "Case #" << i << ": ";
        sol();
        cout << endl;
    }
}
