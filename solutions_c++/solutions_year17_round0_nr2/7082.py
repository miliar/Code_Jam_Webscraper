#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        string N, mn;
        cin >> N;
        mn = N;
        for (int i = N.size() - 2; i >= 0; i--)
            if (mn[i + 1] < N[i])
                mn[i]--;
        if (mn[0] == '0')
            N = string(N.size() - 1, '9');
        else
            for (int i = 0; i < N.size(); i++) {
                if (mn[i] < N[i]) {
                    N[i] = mn[i];
                    for (int j = i + 1; j < N.size(); j++)
                        N[j] = '9';
                    break;
                }
            }
        cout << "Case #" << t + 1 << ": " << N << endl;
    }
    return 0;
}
