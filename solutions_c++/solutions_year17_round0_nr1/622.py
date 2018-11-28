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
        int k;
        cin >> k;

        int count = 0;
        for (int i = 0; i <= s.length() - k; i++) {
            if (s[i] == '-') {
                for (int j = i; j < i + k; j++)
                    s[j] = '+' + '-' - s[j];
                count++;
            }
        }

        bool flag = false;
        for (int i = s.length() - k + 1; i < s.length(); i++)
            if (s[i] == '-') {
                flag = true;
                break;
            }

        cout << "Case #" << t + 1 << ": ";
        if (flag)
            cout << "IMPOSSIBLE\n";
        else
            cout << count << "\n";
    }

    return 0;
}