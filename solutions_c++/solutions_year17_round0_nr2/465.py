#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair

string s;

void update(int indx, string& str, char val) {
    for (int i = indx; i < str.size(); i++) {
        str[i] = val;
    }
}

int main() {

    ifstream cin ("input.txt");
    ofstream cout ("ans.txt");

    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";

        cin >> s;
        if (s.size() == 1) {
            cout << s<< "\n";
            continue;
        }

        string str = s;
        char cur = s[0];
        for (int i = 0; i < s.size(); i++) {
            while (cur <= '9') {
                update(i, str, cur);
                if (str > s) {
                    cur--;
                    update(i, str, cur);
                    break;
                }
                cur++;
            }
            if (str[0] == '0') {
                str = "";
                for (int k = 0; k < s.size() - 1; k++)
                    str = str + '9';
                break;
            }
        }

        cout << str << "\n";
    }

    return 0;
}