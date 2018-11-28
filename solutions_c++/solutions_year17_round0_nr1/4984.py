#include <iostream>
#include <cstring>
using namespace std;

int K;
char cakes[1001];

int main() {
    int cases;
    cin >> cases;
    for (int T=1; T<=cases; ++T) {
        cin >> cakes >> K;

        int N = strlen(cakes), ans = 0;
        for (int i=0; i<=N-K; ++i) {
            if (cakes[i] == '-') {
                for (int j=i; j<i+K; ++j)
                    cakes[j] = cakes[j] == '+' ? '-' : '+';
                ++ans;
            }
        }
        bool possible = true;
        for (int i=N-K; i<N; ++i)
            if (cakes[i] == '-') {
                possible = false;
                break;
            }

        cout << "Case #" << T << ": ";
        if (!possible) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;
    }
    return 0;
}
