#include <cstdio>
#include <iostream>
#include <iomanip>

using namespace std;

void solve(int t)
{
    int D, N;
    cin >> D >> N;
    float maxDuration = 0;
    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> b >> a;
        float duration = 1.0 * (D - b) / a;
        if (duration > maxDuration) {
            maxDuration = duration;
        }
    }
    
    cout << "Case #" << t << ": " << setprecision(6) << fixed << 1.0 * D / maxDuration << endl;
}

int main()
{
    freopen("horses.in" ,"r", stdin);
    freopen("horses.out", "w", stdout);

    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        solve(i + 1);
    }
}
