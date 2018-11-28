#include <bits/stdc++.h>

using namespace std;

bool es(string s) {
    for(int j = 1; j < s.size(); j++) {
        if(s[j] < s[j - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int t, j, corte;
    unsigned long long n, p1;
    string ns, ns2;
    cin >> t;
    for(int i = 1; i <= t; i++) {
        cin >> ns;
        while(!es(ns)) {
            for(j = 1; j < ns.size(); j++) {
                if(ns[j] < ns[j - 1]) {
                    corte = j;
                    break;
                }       
            }
            p1 = stoull(ns.substr(0, corte));
            p1--;
            ns2 = "";
            for(j = 0; j < ns.size() - corte; j++) {
                ns2 += "9";
            }
            if(p1 != 0) ns = to_string(p1) + ns2;
            else ns = ns2;
        }
        cout << "Case #" << i << ": " << ns << endl;
    }
    return 0;
}