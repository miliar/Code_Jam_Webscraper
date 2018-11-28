#include <iostream>
#include <vector>

using namespace std;

void run_testcase() {
    int n;
    double d;
    cin >> d >> n;
    double max_time = 0;
    while (n--) {
        int k, s;
        cin >> k >> s;
        max_time = max(max_time, (d - k) / s);
    }
    cout << fixed << d / max_time;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cout.precision(10);
    freopen("/Users/nikita/Desktop/input.txt", "r", stdin);
    freopen("/Users/nikita/Desktop/output.txt", "w", stdout);
    int Tcase;
    cin >> Tcase;
    for (int test = 1; test <= Tcase; ++test) {
        cout << "Case #" << test << ": ";
        run_testcase();
        cout << '\n';
    }
    
}
