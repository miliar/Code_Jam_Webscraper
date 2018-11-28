#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        int flip = 0;
        string cake;
        cin >> cake;
        int K;
        cin >> K;
        for (int i = 0; i <= cake.size() - K; i++) {
            if (cake[i] == '-') {
                for (int j = i; j < i + K; j++)
                    if (cake[j] == '-')
                        cake[j] = '+';
                    else
                        cake[j] = '-';
                flip++;
            }
        }
        for (int i = 0; i < cake.size(); i++)
            if (cake[i] == '-')
                flip = -1;
        cout << "Case #" << tc << ": ";
        if (flip == -1)
            cout << "IMPOSSIBLE\n";
        else
            cout << flip << "\n";
    }
    return 0;
}
