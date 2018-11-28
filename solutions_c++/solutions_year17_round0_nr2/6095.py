#include <iostream>
using namespace std;

string solve(string str) {
    if (str.length() == 1)
        return str;

    int index = -1;
    for (int i = 1; i < str.length(); i++) {
        if (str[i - 1] > str[i]) {
            index = i - 1;
            break;
        }
    }

    if (index == -1)
        return str;

    for (int i = 0; i < index; i++) {
        if (str[i] == str[index]) {
            index = i;
            break;
        }
    }

    str[index]--;
    for (int i = index + 1; i < str.length(); i++)
        str[i] = '9';

    if (str[0] == '0') return str.substr(1);
    return str;
}

int main() {
    int T, Case = 1;
    cin >> T;
    while (T--) {
        string str;
        cin >> str;
        str = solve(str);
        cout << "Case #" << Case++ << ": " << str << endl;
    }
    return 0;
}
