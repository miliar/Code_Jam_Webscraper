/**

**/
#include <bits/stdc++.h>
using namespace std;

#define N 20005
#define maxN 1000000007
#define PI 3.14159265358979
#define bb __builtin_popcount
#define ll long long
long long n, test, a[N], k;
string s;
void solve() {
    cin >> test;
    for (int te = 1; te <= test; te++) {
        cin >> s >> k;
        n = s.size();
        for (int i = 0; i < n; i++)
            if (s[i] == '+') a[i] = 0; else a[i] = 1;
        int kq = 0;
        for (int i = 0; i < n; i++)
            if (a[i]) {
                kq++;
                if (i + k - 1 >= n) kq = -1;
                else
                    for (int j = i; j <= i + k - 1; j++)
                        a[j] = (a[j] + 1) % 2;
            }
        for (int i = 0; i < n; i++)
            if (a[i]) kq = -1;
        if (kq != -1)
            cout << "Case #" << te << ": " << kq << endl;
        else cout << "Case #" << te << ": " << "IMPOSSIBLE" << endl;
    }
}
int main() {
    freopen("mainAlarge.in", "r", stdin);
    //freopen("mainA.in", "w", stdout);
    freopen("mainAlarge.txt", "w", stdout);
    solve();
    //fclose(stdin);
    //fclose(stdout);
}
///CTKB1997
