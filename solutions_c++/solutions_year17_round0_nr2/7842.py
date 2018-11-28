#include <fstream>
#include <string>

using namespace std;

ifstream cin ("B-large.in");
ofstream cout ("B-large.out");

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        string n;
        cin >> n;
        //cout << n << endl;
        cout << "Case #" << i + 1 << ": ";
        int j = 0;
        while (j < n.length() - 1 && n[j] <= n[j + 1]) {
            ++j;
        }
        if (j < n.length() - 1 && n[j] != '0' && n[j] > n[j + 1]) {
            n[j] = (n[j] - '0' - 1) + '0';
        }
        while (j > 0 && n[j] < n[j - 1]) {
            --j;
            if (n[j] != '0' && n[j] > n[j + 1]) {
                n[j] = (n[j] - '0' - 1) + '0';
            }
        }
        //cout << n << endl;
        if (n[j] != '0') {
            for (int k = 0; k <= j; ++k) {
                cout << n[k];
            }
        }
        for (int k = j + 1; k < n.length(); ++k) {
            cout << '9';
        }
        cout << endl;
    }
    return 0;
}
