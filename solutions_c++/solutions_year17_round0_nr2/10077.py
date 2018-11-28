#include <iostream>
#include <string>

using namespace std;

int main() {
    int t, n, res, flag = 0;
    cin >> t;

    string eval;
    for (int i = 1; i <= t; ++i){
        flag = 0;
        cin >> n;
        for (res = n; res >= 0; res--) {
            eval = std::to_string(res);
            int j = eval.length() - 1;
            if (j == 0) break;
            for (j; j>=1; j--) {
                if (eval[j] < eval[j-1]) {
                    break;
                }
                if (j == 1) flag = 1;
            }
            if (flag == 1) break;
        }
        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}