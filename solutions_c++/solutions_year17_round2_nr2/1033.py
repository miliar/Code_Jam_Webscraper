#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#define ll long long int
#define mod 1000000007
#define pii pair<int, int>
#define fr(n) for (int i = 0; i < n; i++)
#define fr1(n) for (int i = 1; i <= n; i++)
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
    int T;
    in >> T;
    for (int U = 1; U <= T; U++) {
        out << "Case #" << U << ": ";
        int n, a[6] = {};
        in >> n;
        fr(6) in >> a[i];
        int b[3] = {a[0], a[2], a[4]};
        //cout << b[0] << ' ' << b[1] << ' ' << b[2] << '\n';
        if (max({b[0], b[1], b[2]}) == b[0]) {
            if (b[0] > b[1] + b[2]) {
                out << "Impossible\n";
            } else {
                string s;
                fr(b[1]) s += "RY";
                fr(b[0] - b[1]) s += "R";
                int k = (int)s.length() - 1;
                while (b[2]) {
                    if (s[k] == 'R') s.insert(s.begin() + k + 1, 'B'), b[2]--;
                    k--;
                }
                if (s[0] == s.back()) cout << U << '\n';
                int c[3] = {};
                fr(s.length()) {
                    if (s[i] == 'R') c[0]++;
                    if (s[i] == 'Y') c[1]++;
                    if (s[i] == 'B') c[2]++;
                }
                //cout << c[0] << ' ' << c[1] << ' ' << c[2] << '\n';
                out << s << '\n';
            }
        } else if (max({b[0], b[1], b[2]}) == b[1]) {
            if (b[1] > b[0] + b[2]) {
                out << "Impossible\n";
            } else {
                string s;
                fr(b[2]) s += "YB";
                fr(b[1] - b[2]) s += "Y";
                int k = (int)s.length() - 1;
                while (b[0]) {
                    if (s[k] == 'Y') s.insert(s.begin() + k + 1, 'R'), b[0]--;
                    k--;
                }
                if (s[0] == s.back()) cout << U << '\n';
                int c[3] = {};
                fr(s.length()) {
                    if (s[i] == 'R') c[0]++;
                    if (s[i] == 'Y') c[1]++;
                    if (s[i] == 'B') c[2]++;
                }
                //cout << c[0] << ' ' << c[1] << ' ' << c[2] << '\n';
                out << s << '\n';
            }
        } else {
            if (b[2] > b[0] + b[1]) {
                out << "Impossible\n";
            } else {
                string s;
                fr(b[0]) s += "BR";
                fr(b[2] - b[0]) s += "B";
                int k = (int)s.length() - 1;
                while (b[1]) {
                    if (s[k] == 'B') s.insert(s.begin() + k + 1, 'Y'), b[1]--;
                    k--;
                }
                if (s[0] == s.back()) cout << U << '\n';
                int c[3] = {};
                fr(s.length()) {
                    if (s[i] == 'R') c[0]++;
                    if (s[i] == 'Y') c[1]++;
                    if (s[i] == 'B') c[2]++;
                }
                //cout << c[0] << ' ' << c[1] << ' ' << c[2] << '\n';
                out << s << '\n';
            }
        }
        
    }
}
