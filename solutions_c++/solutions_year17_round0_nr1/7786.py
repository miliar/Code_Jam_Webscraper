#include <iostream>

using namespace std;

void solve(int N) {
    string line;
    int K;

    int i = 0;

    int moves = 0;

    cin >> line >> K;

    while(i < line.length()) {
        while(line[i] == '+') { i++; }
        if(i + K <= line.length()) {
            for(int j = i; j < i + K; j++) {
                if(line[j] == '-') {
                    line[j] = '+';
                }
                else {
                    line[j] = '-';
                }
            }
            moves++;
        }
        i++;
    }

    for(int i = 0; i < line.length(); i++) {
        if(line[i] == '-') {
            cout << "Case #" << N << ": IMPOSSIBLE" << endl;
            return;
        }
    }

    cout << "Case #" << N << ": " << moves << endl;
}

int main()
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; i++) {
        solve(i);
    }
    return 0;
}
