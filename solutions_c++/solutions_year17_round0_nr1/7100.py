#include <iostream>
using namespace std;

int main ()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        string s;
        int sol = 0, K, poss = 1;
        cin >> s >> K;
        for (int i = 0; i <= s.size() - K; i++) {
            if (s[i] == '-') {
                for (int j = i; j < i + K; j++) {
                    if (s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
                sol++;
            }
        }
        for (char c : s)
            if (c == '-')
                poss = false;
        cout << "Case #" << t + 1  << ": ";
        if (poss)
            cout << sol << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
