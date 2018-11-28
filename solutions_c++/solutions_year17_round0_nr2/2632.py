#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    cin.rdbuf(in.rdbuf());
    cout.rdbuf(out.rdbuf());
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        string n;
        cin >> n;
        int i;
        for (i = 0; i <(int)n.length()-1 && n[i] <= n[i + 1]; ++i);
        if (i < (int)n.length() - 1) {
            for (; i > 0 && n[i - 1] == n[i]; --i);
            if (i >= 0) {
                --n[i];
                for (++i; i < (int)n.length(); ++i)
                    n[i] = '9';
                if (n[0] == '0')
                    n = n.substr(1);
            }
        }
        cout << n << endl;
    }
    return 0;
}