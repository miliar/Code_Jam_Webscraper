#include <iostream>

using namespace std;

string s;
int k, t, cnt;

int main() {
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        cin >> s >> k;
        cnt = 0;
        for (int j = 0; j < s.size() - k + 1; j++)
        {
            if (s[j] == '+') continue;
            cnt++;
            for (int z = j; z < j + k; z++) s[z] = (s[z] == '+' ? '-' : '+');
        }
        bool u = 1;
        for (auto it : s) u &= (it == '+');
        cout << "Case #" << i << ": ";
        if (u) cout << cnt;
        else cout << "IMPOSSIBLE";
        cout << "\n";
    }
    return 0;
}
