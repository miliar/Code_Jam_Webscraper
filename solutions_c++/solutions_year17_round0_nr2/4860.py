#include <bits/stdc++.h>
using namespace std;

string tidy(string n) {
    int s = n.size();
    if (s == 1) {
        return n;
    }
    if (n == "10") {
        return "9";
    }
    for (int i = 0; i < s-1; i++) {
        if (n[i] > n[i+1]) {
            string n1 = n.substr(0,i+1);
            stringstream ss(n1);
            long long nl;
            ss >> nl;
            n1 = tidy(to_string(nl-1));
            if (n.substr(0,2) == "10") {
                n1 = "";
            }
            for (int j = i+1; j < s; j++) {
                n1 += "9";
            }
            return n1;
        }
    }
    return n;
}

int main() {
    freopen("b-large.in","r",stdin);
    freopen("b-large.out","w",stdout);

    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        string n;
        cin >> n;
        cout << "Case #" << i+1 << ": " << tidy(n) << "\n";
    }

    return 0;
}
