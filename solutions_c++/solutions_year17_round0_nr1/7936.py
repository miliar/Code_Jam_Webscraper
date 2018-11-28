#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int cases, n, len, cnt;
    bool possible;
    string s;
    ifstream cin;
    ofstream cout;
    cin.open("large.in");
    cout.open("large.out");
    cin >> cases;
    for (int i = 1; i <= cases; i++) {
        cin >> s >> n;
        cout << "Case #" << i << ": ";
        cnt = 0;
        possible = true;
        len = s.length();
        for (int j = 0; j <= len - n; j++) {
            if (s[j] == '-') {
                cnt++;
                for (int k = 0; k < n; k++) {
                    if (s[j + k] == '-') {
                        s[j + k] = '+';
                    }
                    else {
                        s[j + k] = '-';
                    }
                }
            }
        }
        for (int j = 0; j < len; j++) {
            if (s[j] == '-') {
                possible = false;
                cout << "IMPOSSIBLE" << endl;
                break;
            }
        }
        if (possible) {
            cout << cnt << endl;
        }
    }
    cin.close();
    cout.close();
    return 0;
}
