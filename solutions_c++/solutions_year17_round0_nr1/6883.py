#include <iostream>
#include <string>
using namespace std;

int main()
{
    int T; cin >> T;
    for (int t = 0; t < T; t++)
    {
        string x; int k;
        cin >> x >> k;

        int count = 0;
        for (int i = 0; i < x.size() - k; ++i)
        {
            if (x[i] == '-') {
                ++count;
                for (int j = 0; j < k; j++) {
                    x[i+j] = (x[i+j] == '-') ? '+' : '-';
                }
            }
        }

        bool error = false;
        char std = x[x.size() - k];
        for (int i = x.size() - k + 1; i < x.size(); ++i) {
            if (x[i] != std) {
                error = true;
                break;
            }
        }

        if (std == '-') ++count;
        cout << "Case #" << t+1 << ": ";
        if (error) cout << "IMPOSSIBLE"; else cout << count;
        cout <<endl;

    }
    return 0;
}
