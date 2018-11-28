#include <iostream>
using namespace std;

int main () {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string l;
        cin >> l;
        int m;
        cin >> m;
        int s = 0;
        for (int j = 0; j < l.length() - m + 1; j++) {
            if (l[j] == '-') {
                for (int k = j; k < j + m; k++) {
                    if (l[k] == '+') {
                        l[k] = '-';
                    }
                    else {
                        l[k] = '+';
                    }
                }
                s++;
            }
        }
        string check;
        for (int j = 0; j < l.length(); j++) {
            check.push_back('+');
        }
        if (l == check) {
            cout << "Case #" << i + 1 << ": " << s << endl;
        }
        else {
            cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
        }
    }
}
