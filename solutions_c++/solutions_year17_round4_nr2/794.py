#include <bits/stdc++.h>

#define fin(i, n) for (int i = 0; i < n; i++)
#define fin2(i, a, b) for (int i = a; i < b; i++)
#define ll long long

using namespace std;

int main() {
    int T;
    cin >> T;
    fin(I, T) {
        cout << "Case #" << I + 1 << ": ";
        cerr << "Case #" << I + 1 << ": ";
        int n, c, m;
        cin >> n >> c >> m;

        int sol = 0;

        vector<int> a(n);
        vector<int> b(n);

        int aa = 0, bb = 0;

        fin(i, m) {
            int x, y;
            cin >> x >> y;
            if (y == 1) a[x - 1]++;
            else b[x - 1]++;
            if (y == 1) aa++;
            else bb++;
        }

        sol = max(aa, bb);
        fin2(i, 1, n) sol = max(sol, a[i] + b[i]);
        if (a[0] + b[0] > sol) {
            cout << a[0] + b[0] << " 0" << endl;
            cerr << a[0] + b[0] << " 0" << endl;
        }
        else {
            cout << max(aa, bb) << " " << sol - max(aa, bb) << endl;
            cerr << max(aa, bb) << " " << sol - max(aa, bb) << endl;
        }
    }
}
