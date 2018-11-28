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
        int n, p;
        cin >> n >> p;
        vector<int> v(4, 0);
        fin(i, n) {
            int x;
            cin >> x;
            v[x % p]++;
        }
        
        int sol = 0;
        sol += v[0];
        if (p == 2) {
            sol += (v[1] + 1) / 2;
        }
        if (p == 3) {
            int x = min(v[1], v[2]);
            sol += x;
            int y = max(v[1], v[2]) - x;
            sol += (y + 2) / 3;
        }
        if (p == 4) {
            int x = min(v[1], v[3]);
            sol += x;
            v[1] -= x;
            v[3] -= x;
            int y = v[2] / 2;
            sol += y;
            v[2] -= 2 * y;
            if (v[2] == 1) {
                if (v[1] >= 2) {
                    v[1] -= 2;
                    v[2] -= 1;
                    sol++;
                }
                if (v[3] >= 2) {
                    v[3] -= 2;
                    v[2] -= 1;
                    sol++;
                }
            }
            sol += v[1] / 4;
            sol += v[3] / 4;
            v[1] = v[1] % 4;
            v[3] = v[3] % 4;
            if (v[1] + v[2] + v[3] > 0) sol++;
        }

        cout << sol << endl;
        cerr << sol << endl;
    }
}
