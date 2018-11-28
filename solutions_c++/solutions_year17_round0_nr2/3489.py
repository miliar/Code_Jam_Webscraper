#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
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
        string s;
        in >> s;
        fr(s.length()) {
            bool y = 0;
            for (int j = i; j < s.length(); j++) {
                if (s[j] > s[i]) break;
                if (s[j] < s[i]) {
                    y = 1;
                    break;
                }
            }
            if (y) {
                s[i]--;
                for (int j = i + 1; j < s.length(); j++) s[j] = '9';
            }
        }
        if (s[0] == '0') s.erase(s.begin());
        out << s << '\n';
    }
}
