#include <iostream>
#include <string>

using namespace std;

int t, k;
string s;

void f(int i) {
    for (int j = 0; j < k; ++j) s[i+j] = 88 - s[i+j];
}

int main() {
    cin >> t;
    for (int c = 0; c ++< t;) {
        cin >> s >> k;
        cout << "Case #" << c << ": ";
        int n = 0;
        for (int i = 0; i < s.length(); ++i) if (s[i] == '-') {
            if (i + k > s.length()) goto fail;
            f(i);
            ++n;
         }
        cout << n << '\n';
        continue;
        fail:
        cout << "IMPOSSIBLE\n";
    }
    return 0;
}
