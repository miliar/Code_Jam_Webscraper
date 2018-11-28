#include<iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);

    int t;

    cin >> t;
    for (int i = 0; i < t; i++) {
        string s;
        cin >> s;
        int minimal = 9999999;
        for (int j = (int) s.length() - 1; j >= 0; j--) {
            if (s[j] > minimal) {
                if ((j != 0 && s[j] > '0') || (j == 0 && s[j] > '1')) {
                    s[j]--;
                    for (int x = j + 1; x < s.length(); x++) {
                        s[x] = '9';
                    }
                    minimal = 9999999;
                } else {
                    int size = (int) s.length() - 1;
                    string result = "";
                    for (int x = 0; x < size; x++) {
                        result += '9';
                    }

                    s = result;
                    break;
                }
            }

            minimal = min((int) s[j], minimal);
        }

        cout << "Case #" << i + 1 << ": " << s << endl;
    }
}