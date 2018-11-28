#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define pb push_back
#define mp make_pair

int d, n;
int k[1010];
int s[1010];

void solve()
{
    cin >> d >> n;
    for(int i = 0; i < n; i++) cin >> k[i] >> s[i];
    double mx = 0;
    for(int i = 0; i < n; i++){
        double dist = d - k[i];
        mx = max(mx, dist / (double)s[i]);
    }
    cout << fixed << setprecision(12) << (double)d / mx << endl;
}

int main()
{
    freopen("A.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    for(int i = 1; i <= test; i++){
        cout << "Case #" << i << ": ";
        solve();
    }
}
