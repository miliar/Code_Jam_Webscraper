#include <bits/stdc++.h>

using namespace std;

const int N = 55;

double p[N];
int n, k;
double u;

void solveTest() {
    cin >> n >> k;
    cin >> u;
    for (int i = 1; i <= n; i++) {
        cin >> p[i];
    }
    
    double low = 0.0;
    double high = 1.0;
    for (int it = 1; it <= 100; it++) {
        double mid = (low + high) / 2;
        double usedUnits = 0;
        for (int i = 1; i <= n; i++) {
            if (p[i] < mid) {
                usedUnits += mid - p[i];
            }
        }
        if (usedUnits <= u) {
            low = mid;
        } else {
            high = mid;
        }
    }
    
    double ans = 1.0;
    for (int i = 1; i <= n; i++) {
        if (p[i] < high) {
            ans *= high;
        } else {
            ans *= p[i];
        }
    }
    
    cout << fixed << setprecision(10) << ans << endl;
}

int main() {

    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cout << "Case #" << test << ": ";
        solveTest();
    }
    
    return 0;
}