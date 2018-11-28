#include <iostream>
#include <string>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int c = 1; c <= T; c++) {
        string S;
        int K, r = 0;
        cin >> S >> K;
        for (int i = 0; i < S.size(); i++) {
            if (S[i] == '-') {
                if (i + K > S.size()) {
                    r = -1;
                    break;
                }
                for (int j = i; j < i + K; j++) {
                    if (S[j] == '+') S[j] = '-';
                    else S[j] = '+';
                }
                r++;
            }
        }
        cout << "Case #" << c << ": ";
        if (r == -1) cout << "IMPOSSIBLE" << endl;
        else cout << r << endl;
    }
    
    return 0;
}
