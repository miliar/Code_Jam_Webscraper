#include <iostream>
#include <string>
using namespace std;

const int N_MAX = 1e3;
int T, N, K;
string s;
bool p[N_MAX];

int main() {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> s >> K;
        N = s.size();
        for (int i = 0; i < N; i++) p[i] = (s[i] == '+');
        int flips = 0;
        for (int i = 0; i < N && flips != -1; i++) {
            if (p[i]) continue;
            if (N < i+K) flips = -1;
            else {
                for (int j = i; j < i+K; j++) p[j] = !p[j];
                flips++;
            }
        }
        cout << "Case #" << t << ": ";
        if (flips == -1) cout << "IMPOSSIBLE" << endl;
        else cout << flips << endl;
    }
    return 0;
}
