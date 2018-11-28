#include <iostream>
#include <algorithm>
#include <string> 

using namespace std;

bool istidy(int k) {
    string s = to_string(k);
    string ss = s;
    sort(ss.begin(), ss.end());

    return s == ss;
}

int main() {
    int t, n;

    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #"<<i<<": ";
        cin >> n;
        for (int m = n; m >= 1; m--)
            if (istidy(m)) {
                cout << m << endl;
                break;
            }
    }

    return 0;

}
