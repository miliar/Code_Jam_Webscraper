#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, p;
int c[100];

void solve(int t) {
    cin >> n >> p;
    for (int i = 0; i < p; i++) c[i] = 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        c[x%p]++;
    }
    cout << "Case #" << t << ": ";
    int z = 0;
    if (p == 2) {
        z += c[1]/2;
    }
    if (p == 3) {
        while (c[1] && c[2]) {
            c[1]--; c[2]--;
            z++;
        }
        for (int i = 0; i < c[1]; i++) {
            if (i%3 != 0) z++;
        }
        for (int i = 0; i < c[2]; i++) {
            if (i%3 != 0) z++;
        }
    }
    if (p == 4) {
        while (c[1] && c[3]) {
            c[1]--; c[3]--;
            z++;
        }
        while (c[2] >= 2) {
            c[2]--; c[2]--;
            z++;
        }
        vector<int> lol;
        for (int i = 0; i < c[1]; i++) lol.push_back(1);
        for (int i = 0; i < c[2]; i++) lol.push_back(2);
        for (int i = 0; i < c[3]; i++) lol.push_back(3);
        int pz = 999999999;
        do {
            int uz = 0;
            int cc = 0;
            for (int i = 0; i < lol.size(); i++) {
                if (cc%4 != 0) uz++;
                cc += lol[i];
            }
            pz = min(pz,uz);
        } while (next_permutation(lol.begin(),lol.end()));
        z += pz;
    }
    cout << n-z << "\n";
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
}
