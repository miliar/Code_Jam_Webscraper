#include <bits/stdc++.h>

using namespace std;

void solve(int test_num)
{
    double d;
    int n;
    cin >> d >> n;
    vector<pair<double, double>> x(n);
    for (int i = 0; i < n; i++) {
        cin >> x[i].first >> x[i].second;
    }
    sort(x.rbegin(), x.rend());
    double cur_best_time = 0;
    for (int i = 0; i < n; i++) {
        double my_time = (d - x[i].first) / x[i].second;
        if (my_time > cur_best_time) {
            cur_best_time = my_time;
        }
    }
    cout << " " << d / cur_best_time << endl;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.precision(15);
    cout.setf(ios::fixed);

    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cout << "Case #" << i + 1 << ":";
        solve(i);
    }
}
