#include <stdio.h>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <ctime>
#include <cassert>
#include <unordered_map>
#include <fstream>
#include <random>
#include <cstring>
#include <complex>
#include <bitset>

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define pb push_back

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
mt19937 rr(random_device{}());


int main() {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int tests;
    cin >> tests;
    cout.precision(12);
    cout << fixed;

    vector<char> col = {'R', 'O', 'Y', 'G', 'B', 'V'};

    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        int n;
        cin >> n;
        vector<int> c(6);
        for (int i = 0; i < 6; ++i) 
            cin >> c[i];
        string u[6];

        bool printed = false;

        for (int i = 1; i < 6; i += 2) {
            int j = (i + 3) % 6;
            u[j] += col[j];
            for (; c[i] > 0; ) {
                u[j] += col[i];
                u[j] += col[j];
                --c[i]; --c[j];
            }

            if (c[j] == 0 && sz(u[j]) == n + 1) {
                u[j].pop_back();
                cout << u[j] << "\n";
                printed = true;
                break;
            }
            if (c[j] < 0) {
                cout << "IMPOSSIBLE\n";
                printed = true;
                break;
            }
        }

        if (printed) {
            continue;
        }

        string ans;
        vector<int> used(6);
        int prev = -1;
        bool f = true;

        int prior = -1;

        for (; c[0] > 0 || c[2] > 0 || c[4] > 0; ) {
            int k = -1;
            for (int i = 0; i < 6; i += 2) {
                if ((k == -1 || c[k] < c[i] || (c[k] == c[i] && i == prior)) && prev != i) 
                    k = i;
            }
            if (prev == -1) {
                prior = k;
            }

            prev = k;
            if (k == -1) {
                f = false;
                break;
            }
            --c[k];
            if (!used[k]) {
                ans += u[k];
                used[k] = true;
            } else {
                ans += col[k];
            }
        }

        // cout << ans << " " << f << endl;

        if (!f) {
            cout << "IMPOSSIBLE\n"; 
            continue;
        }

        

        if (sz(ans) != n || ans[0] == ans.back()) {
            cout << "IMPOSSIBLE\n"; 
            continue;
        }
        cout << ans << "\n";
    }

}