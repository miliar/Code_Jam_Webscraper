#include <bits/stdc++.h>
using namespace std;
#pragma GCC diagnostic ignored "-Wmissing-declarations"

#define FINAL_OUT(x) {cout << (x) << '\n'; exit(0);}


void solve(int numtest)
{
    int d;
    int n;
    cin >> d >> n;

    vector<pair<int,int> > h(n);
    for(int i = 0; i < n; ++i)
        cin >> h[i].first >> h[i].second;

    //sort(begin(h), end(h));


    double last = 0.0;
    for(int i = 0; i < n; ++i)
        last = max(last, static_cast<double>(d - h[i].first) / static_cast<double>(h[i].second));

    cout << "Case #" << numtest << ": " << d / last << endl;
}

int main()
{
    freopen("a-large.in", "r", stdin);
    freopen("a-large.out", "w", stdout);
    ios_base::sync_with_stdio(false);

    cout << fixed << setprecision(10);

    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i)
        solve(i);
}
