#include <iostream>
using namespace std;

int main() {
    int tot;
    cin >> tot;
    for (int i = 0; i < tot; i ++) {
        std::string input;
        cin >> input;
        int size;
        cin >> size;
        int ans = 0;
        for (int j = 0; j < input.size() - size + 1; j++) {
            if (input[j] != '+') {
                ans ++;
                for (int k = j; k < j + size; k ++) {
                    input[k] = input[k] == '+' ? '-' : '+';
                }
            }
        }
        cout << "Case #" << i + 1 << ": ";
        bool ret = true;
        for (auto& x : input) {
            if (x == '-') ret = false;
        }
        if (!ret) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;
    }
    return 0;
}
