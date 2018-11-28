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
        int n;
        long double u, a[52] = {}, z = 1;
        in >> n >> n >> u;
        fr1(n) in >> a[i];
        a[n + 1] = 1;
        sort(a + 1, a + n + 1);
        fr1(n) {
            if (i * (a[i + 1] - a[i]) <= u) {
                u -= i * (a[i + 1] - a[i]);
                for (int j = 1; j <= i; j++) a[j] = a[i + 1];
            } else {
                for (int j = 1; j <= i; j++) a[j] += u / i;
                break;
            }
            //for (int j = 1; j <= n; j++) cout << a[j] << ' '; cout << '\n';
        }
        //fr1(n) cout << a[i] << ' ';
        fr1(n) z *= a[i];
        out << fixed << setprecision(13) << z << '\n';
    }
}
