#include <iostream>

using namespace std;

string lol(string x) {
    int k = x.size();
    for (int i = 0; i < k-1; i++) {
        if (x[i] > x[i+1]) {
            x[i]--;
            for (int j = i+1; j < k; j++) x[j] = '9';
            while (x[0] == '0') x = x.substr(1);
            return x;
        }
    }
    return x;
}

void solve(int x) {
    string s;
    cin >> s;
    while (true) {
        string u = lol(s);
        if (s == u) break;
        s = u;
    }
    cout << "Case #" << x << ": " << s << "\n";
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
}
