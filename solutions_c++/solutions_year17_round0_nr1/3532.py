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
        int n, z = 0, y = 0;
        string s;
        in >> s >> n;
        for (int i = 0; i + n <= s.length(); i++) if (s[i] == '-') {
            z++;
            for (int j = i; j < i + n; j++) s[j] = (s[j] == '-' ? '+' : '-');
        }
        fr(s.length()) if (s[i] == '-') y = 1;
        if (y) out << "IMPOSSIBLE\n";
        else out << z << '\n';
    }
}
