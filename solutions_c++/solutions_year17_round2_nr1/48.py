#include <iostream>

using namespace std;

double d;
int n;

void solve(int x) {
    cin >> d >> n;
    double z = 0;
    for (int i = 1; i <= n; i++) {
        double k, s;
        cin >> k >> s;
        double u = (d-k)/s;
        z = max(z,u);
    }
    printf("Case #%d: %.9lf\n", x, d/z);
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
}
