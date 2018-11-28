#include <iostream>
#include <string>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int c = 1; c <= T; c++) {
        string N;
        cin >> N;
        bool changed = true;
        while (changed) {
            changed = false;
            for (int k = 0; k < N.size(); k++) {
                if (k < N.size() - 1 && N[k] > N[k+1]) {
                    N[k]--;
                    for (k = k+1; k < N.size(); k++) N[k] = '9';
                    changed = true;
                    break;
                }
            }
        }
        if (N[0] == '0') N.erase(0,1);
        cout << "Case #" << c << ": " << N << endl;
    }
    return 0;
}
