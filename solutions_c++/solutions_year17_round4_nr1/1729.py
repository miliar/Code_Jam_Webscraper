#include <bits/stdc++.h>
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
        int n, p, a[4] = {}, b;
        in >> n >> p;
        fr1(n) in >> b, a[b % p]++;
        if (p == 2) {
            out << a[0] + (a[1] + 1) / 2 << '\n';
        } else if (p == 3) {
            if (a[1] < a[2]) swap(a[1], a[2]);
            out << a[0] + a[2] + (a[1] - a[2]) / 3 + ((a[1] - a[2]) % 3 != 0) << '\n';
        }
    }
}
