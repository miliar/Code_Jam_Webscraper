#include <iostream>
#include <string>
using namespace std;

void code() {
    string s;
    cin >> s;
    int N = s.size();
    int K;
    cin >> K;

    int flips = 0;
    for (int i = 0; i < N; i++) {
        if (s[i] == '-') {
            if (i + K > N) {
                cout << "IMPOSSIBLE\n";
                return;
            }
            flips++;
            for (int j = i; j < i+K; j++) {
                if (s[j] == '-') s[j] = '+';
                else s[j] = '-';
            }
        }
    }
    cout << flips << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cout << "Case #" << (i + 1) <<": ";
        code();
    }
}
