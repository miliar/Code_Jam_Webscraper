#include <bits/stdc++.h>

using namespace std;

ifstream fin("test.in");
ofstream fout("test.out");

int main() {
    ios::sync_with_stdio(false);

    int t;
    fin >> t;

    int level = 0;
    while(t--) {
        level++;

        string s;
        int k;
        fin >> s >> k;

        int n = (int)s.size();

        int sw = 0;
        for(int i = 0; i < n - k + 1; i++) {
            if(s[i] == '-') {
                sw++;
                for(int j = i; j < i + k; j++) {
                    if(s[j] == '-') {
                        s[j] = '+';
                    } else {
                        s[j] = '-';
                    }
                }
            }
        }

        bool good = true;
        for(int i = 0; i < n; i++) {
            if(s[i] == '-') good = false;
        }

        fout << "Case #" << level << ": ";
        if(good == true) {
            fout << sw << "\n";
        } else {
            fout << "IMPOSSIBLE\n";
        }
    }
    return 0;
}
