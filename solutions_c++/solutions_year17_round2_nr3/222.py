#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <list>
#include <limits>
#include <algorithm>
#include <utility>
#include <array>
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef long long ull;

ifstream inputStream;

int n;
int q;

array<ll, 100> e;
array<ll, 100> s;

array<array<ll, 100>, 100> d;
array<array<double, 100>, 100> t;

array<int, 100> u;
array<int, 100> v;

void solve(int tt) {
    cout << "Case #" << tt << ":";
    inputStream >> n >> q;
    for(int i=0; i<n; i++) {
        inputStream >> e[i] >> s[i];
    }
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            inputStream >> d[i][j];
        }
    }
    for(int i=0; i<q; i++) {
        inputStream >> u[i] >> v[i];
        u[i]--;
        v[i]--;
    }

    for (int k = 0; k < n; k++) {
        for(int i=0; i<n; i++) {
            for (int j = 0; j < n; j++) {
                if(d[i][k] != -1 && d[k][j] != -1 && (d[i][k] + d[k][j] < d[i][j] || d[i][j] == -1)) {
                    d[i][j] = d[i][k] + d[k][j];
                }
            }
        }
    }

    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if(d[i][j] == -1 || d[i][j] > e[i]) {
                t[i][j] = -1.0;
            } else {
                t[i][j] = (double)d[i][j] / (double)s[i];
            }
        }
    }

    for (int k = 0; k < n; k++) {
        for(int i=0; i<n; i++) {
            for (int j = 0; j < n; j++) {
                if(t[i][k] >= 0.0 && t[k][j] >= 0.0 && (t[i][k] + t[k][j] < t[i][j] || t[i][j] < 0.0)) {
                    t[i][j] = t[i][k] + t[k][j];
                }
            }
        }
    }

    for(int i=0; i<q; i++) {
        cout << " " << setprecision(10) << fixed << t[u[i]][v[i]];
    }

    cout << endl;
}

int main(int argc, char** argv) {

    inputStream = ifstream(argv[1]);
    int tt;
    inputStream >> tt;

    for(int i=0; i<tt; i++) {
        solve(i+1);
    }

}