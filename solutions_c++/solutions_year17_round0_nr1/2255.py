#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string s;
int test , k;

int main () {
    freopen("input.txt" , "r" , stdin);
    freopen("output.txt" , "w" , stdout);

    cin >> test;

    for (int t = 1; t <= test; t++) {
        cout << "Case #" << t << ": ";
        cin >> s >> k;

        int l = s.size();
        int res = 0;

        for (int i = 0; i < l; i++)
            if (s[i] == '-' && i + k - 1 < l) {
                ++res;
                for (int j = i; j <= i + k - 1; j++)
                    if (s[j] == '+') s[j] = '-';
                    else s[j] = '+';
            }

        bool check = true;

        for (int i = 0; i < l; i++)
            if (s[i] == '-') check = false;

        if (!check) cout << "IMPOSSIBLE";
        else cout << res;

        cout << endl;
    }
    return 0;
}
