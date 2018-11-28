#include <bits/stdc++.h>
using namespace std;
#pragma GCC diagnostic ignored "-Wmissing-declarations"

#define FINAL_OUT(x) {cout << (x) << '\n'; exit(0);}


void solve(int numtest)
{
    vector<int> a(6);
    int sum;
    cin >> sum;
    for(int& x : a)
        cin >> x;

    string names = "ROYGBV";
    string ans;

    int prev = -1;
    for(int i = 0; i < 6; ++i)
        if (a[i] > 0)
        {
            --a[i];
            ans.push_back(names[i]);
            --sum;
            prev = i;
            break;
        }


    bool once = false;
    while (sum--)
    {
        int best = 1;
        for(int i = 0; i < 6; ++i)
            if (prev != i && a[best] < a[i])
                best = i;
        if (a[best] == 0 || prev == best)
        {
            ans = "IMPOSSIBLE";
            break;
        }
        prev = best;
        a[best]--;
        ans.push_back(names[best]);

        if (sum == 0 && names[best] == ans[0])
            ans = "IMPOSSIBLE";
    }
    cout << "Case #" << numtest << ": " << ans << endl;
}

int main()
{
//    freopen("in.txt", "r", stdin);
    freopen("B-small4.in", "r", stdin);
    freopen("B-small4.out", "w", stdout);
    ios_base::sync_with_stdio(false);

    //cout << fixed << setprecision(10);

    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i)
        solve(i);
}
