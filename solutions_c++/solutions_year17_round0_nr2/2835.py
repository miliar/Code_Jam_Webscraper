// Tidy Numbers
// Author: aroussau

#include <iostream>
#include <string>
#include <vector>

using namespace std;

long long T;
string N;

string solve(string s) {
    if (s.length() == 1) {
        return s;
    }
    
    char last_digit = '9';
    string res = s;

    for (int i = res.length() - 1; i >= 0 ; --i) {
        if ((int)res[i] > (int)last_digit) {
            res[i] = (char)((int)res[i] - 1);

            for (int j = i + 1; j < res.length(); ++j) {
                res[j] = '9';
            }
        }

        last_digit=res[i];
    }

    int aux;
    for (aux = 0; aux < res.length(); ++aux) {
        if (res[aux] != '0') {
            break;
        }
    }

    return res.substr(aux);
}

int main() {
    cin >> T;

    for (long long i = 1; i <= T; ++i) {
        cin >> N;
        string res = solve(N);
        cout << "Case #" << i << ": " << res << "\n";
    }
    
    return 0;
}
