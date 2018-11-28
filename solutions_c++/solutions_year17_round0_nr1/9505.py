#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
const int N = 1e4 + 5;
ifstream fi("A-large.in"); ofstream fo("test.out");
int test, n, c = 0;
bool a[N], r;
string s = "";
int main() {
    fi >> test; int i, j = 0;
    for (int k = 1; k <= test; k++) {
        fi >> s >> n;
        c = 0; r = 1;
        for (i = 0; i < (int) s.length(); i++) a[i] = s[i] == '+';
        for (i = 0; i < (int) s.length() - n + 1; i++) if (!a[i]) {
            c++; for (j = i; j < i + n; j++) a[j]^=1;
        } for (i = s.length() - n + 1; i < (int) s.length(); i++)
            if (!a[i]) r = 0;
        fo << "Case #" << k << ": ";
        if (r) fo << c; else fo << "IMPOSSIBLE";
        fo << '\n';
    } return 0;
}
