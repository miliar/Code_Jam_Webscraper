#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    
    int t;
    cin >> t;
    for (int j = 0; j < t; ++j) {
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        for (int i = 0; i < (int)s.size() - k + 1; ++i) {
            if (s[i] == '-') {
                for (int z = 0; z < k; ++z) {
                    if (s[i + z] == '-')
                        s[i + z] = '+';
                    else
                        s[i + z] = '-';
                }
                ++ans;
            }
        }
        for (int i = 0; i < (int)s.size(); ++i)
            if (s[i] == '-')
                ans = -1;
        cout << "Case #" << j + 1 << ": ";
        if (ans == -1)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << '\n';
    }

    return 0;
}