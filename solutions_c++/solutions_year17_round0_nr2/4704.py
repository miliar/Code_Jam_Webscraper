#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    for (int n = 0; n < N; ++ n) {
        string a;
        cin >> a;
        int i, lower = 0;
        for (i = 0; i < a.size(); ++ i) {
            if (a[i] - '0' < lower) break;
            lower = a[i] - '0';
        }
        if (i < a.size()) {
            -- i;
            while (a[i] == '0' || (i > 0 && a[i] == a[i - 1])) -- i;
            // a'[i] = a[i] - 1
            -- a[i];
            for (int j = i + 1; j < a.size(); ++ j) a[j] = '9';
        }
        while (a[0] == '0') a.erase(0, 1);
        printf("Case #%d: %s\n", n+1, a.c_str());
    }
    return 0;
}
