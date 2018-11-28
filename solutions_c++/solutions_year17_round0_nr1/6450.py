#include <iostream>
#include <cstring>
using namespace std;
int main() {
    int T, K;
    char S[1005];
    int len;
    cin >> T;
    for(int i = 0; i < T; i++) {
        cin >> S >> K;
        len = strlen(S);
        int ans = 0;
        for (int j = 0; j < len; j++) {
            if (S[j] == '-') {
                // Controllo di non sforare
                int sx = j, dx = j + K;
                if (dx > len) { dx = len; sx = len - K; }
                // Giro tutti
                ans++;
                for (; sx < dx; sx++)
                    S[sx] = (S[sx] == '+') ? '-' : '+';
            }
        }
        bool left = false;
        for (int j = 0; j < len; j++) if (S[j] == '-') left = true;
        if (left)
            cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << i + 1 << ": " << ans << endl;
    }
}
