#include <bits/stdc++.h>

using namespace std;

int main()
{
#ifdef DEBUG
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
#endif // DEBUG
    std::ios::sync_with_stdio(false);
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        cout << "Case #" << i+1 << ": ";
        string s;
        int k, flips = 0;
        cin >> s >> k;
        for(int j = 0; j < s.length() - k + 1; j++) {
            if(s[j] == '-') {
                flips++;
                for(int l = j; l < j + k; l++) {
                    if(s[l] == '-') {
                        s[l] = '+';
                    } else {
                        s[l] = '-';
                    }
                }
            }
        }
        bool possible = true;
        for(int j = s.length() - k; j < s.length(); j++) {
            if(s[j] == '-') {
                cout << "IMPOSSIBLE" << endl;
                possible = false;
                break;
            }
        }
        if(possible) {
            cout << flips << endl;
        }
    }
    return 0;
}
