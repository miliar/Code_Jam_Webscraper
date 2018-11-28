#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
    int T;
    string N;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> N;
        int j = 0;
        while (j < N.length() - 1) {
            if (N[j] > N[j + 1]) {
                int k = j;
                while (k > 0 && N[k - 1] == N[k]) k--;
                N[k++]--;
                for (; k < N.length(); k++) {
                    N[k] = '9';
                }
                break;
            }
            j++;
        }
        if (N[0] == '0') {
            N = N.substr(1);
        }
        cout << "Case #" << i << ": " << N << endl;
    }
    return 0;
}