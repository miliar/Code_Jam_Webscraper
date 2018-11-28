#include <iostream>
using namespace std;

void solve(int kase) {
    string order;
    int k;
    cin >> order >> k;

    int cnt = 0;
    for (int i = 0; i < order.size() - k + 1; i++) {
        if (order[i] == '-') {
            cnt++;
            for (int j = 0; j < k; j++) {
                if (order[i + j] == '-') order[i + j] = '+';
                else order[i + j] = '-';
            }
        }
    }
    bool possible = true;
    for (int i = 0; i < order.size(); i++) {
        if (order[i] == '-') {
            possible = false;
            break;
        }
    }
    if (possible) {
        cout << "Case #" << kase + 1 << ": " << cnt << endl;
    } else {
        cout << "Case #" << kase + 1 << ": IMPOSSIBLE" << endl;
    }
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) solve(i);
}
