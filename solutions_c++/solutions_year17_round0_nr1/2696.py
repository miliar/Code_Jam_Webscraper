#include <iostream>
#include <string>
using namespace std;

int main(int argc, char** argv) {
    int T, S, K;
    char ch;
    cin >> T;
    char buf[2048];
    cerr << T << endl;
    for (int t = 0; t < T; ++t) {
        S = 0;
        cin >> ch;
        while (true) {
            cerr << '[' << ch << ']';
            if (ch == ' ') break;
            buf[S] = ch;
            ++S;
            ch = cin.get();
        }
        cin >> K;
        cerr << S << ' ' << K << endl;

        int a = 0;
        for (int i = 0; i <= S - K; ++i) {
            if (buf[i] == '+') continue;
            ++a;
            for (int j = 0; j < K; ++j) {
                buf[i+j] = '+' + '-' - buf[i+j];
            }
//            cerr << i << ' ' << (S-K) << ' ';
//            for (int x = 0; x < S; ++x) cerr << "{" << buf[x] << "}"; cerr << endl;
        }
        for (int j = 0; j < S; ++j) {
            if (buf[j] != '+') a = -1;
        }
        cout << "Case #" << (t + 1) << ": ";
        if (a == -1) cout << "IMPOSSIBLE\n";
        else cout << a << endl;
    }

}
