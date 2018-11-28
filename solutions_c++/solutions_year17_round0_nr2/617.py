#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <algorithm>

#define mp make_pair
#define pb push_back

using namespace std;

typedef pair<int, int> pii;

const int MAXN = 1e6;
const int inf = 1e9 + 5;

int main() {
    /*std::ios::sync_with_stdio(false);
    cin.tie(0);*/
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int q;
    cin >> q;
    for (int t = 0; t < q; t++) {
        string s;
        cin >> s;

        int i = 1;
        while (i < s.length() && s[i - 1] <= s[i])
            i++;

        if (i != s.length()) {

            int st = i - 2;
            while (st >= 0 && s[st] == s[st + 1])
                st--;
            s[st + 1]--;
            for (int j = st + 2; j < s.length(); j++)
                s[j] = '9';
            if (s[0] == '0')
                s = s.substr(1);
        }

        /*for (int i = n; i >= 1; i--) {
            string str = to_string(i);
            bool flag = false;
            for (int j = 0; j < str.length() - 1; j++)
                if (str[j] > str[j + 1]) {
                    flag = true;
                    break;
                }
            if (!flag) {
                if (i != stoi(s))
                    cout << "THIS FUCKING TEST!!!!" << i << "\n" ;
                break;
            }
        }*/

        cout << "Case #" << t + 1 << ": " << s << "\n";
    }

    return 0;
}