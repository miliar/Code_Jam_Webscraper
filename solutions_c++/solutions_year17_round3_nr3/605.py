#include <cstdio>
#include <vector>
#include <iostream>
#include <iomanip>

using namespace std;

vector<double> v;

void PrintDebug() {
    return;
    cout << endl;
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;
}

void solve()
{
    int N, K;
    double U;

    cin >> N >> K;
    cin >> U;
    v.clear();
    for (int i = 0; i < N; i++) {
        double x;
        cin >> x;
        v.push_back(x);
    }

    sort(v.begin(), v.end());
    v.push_back(1);
    PrintDebug();
    for (int i = 0; i < K; i++) {
        double target = v[i + 1];
        double needed = (target - v[0]) * (i + 1);

        // cout << "NEEDED " << needed << " LEFT " << U << endl;

        if (needed <= U) {
            for (int j = 0; j <= i; j++) {
                v[j] = v[i + 1];
            }
            U = U - needed;
            PrintDebug();
        } else {
            double add = U / (i + 1);
            for (int j = 0; j <= i; j++) {
                v[j] = v[j] + add;
            }
            PrintDebug();
            break;
        }
    }

    double sol = 1;
    for (int i = 0; i < N; i++) {
        sol = sol * v[i];
    }

    cout << setprecision(20) << fixed << sol << endl;
}

int main() {
    freopen("cores.in", "r", stdin);
    freopen("cores.out", "w", stdout);
    
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}
