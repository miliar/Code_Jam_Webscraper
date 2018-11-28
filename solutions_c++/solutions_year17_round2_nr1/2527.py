#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
#include <unordered_set>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vec;
typedef vector<ll> vecll;

const int MaxN = 1000 * 1000 + 10;
const ll mod = 1000 * 1000 * 1000 + 7;

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    // freopen("in.txt", "r", stdin);
    // freopen("out.txt", "w", stdout);
    // ifstream cin("in.txt");
    // ofstream cout("out.txt");
    int cntTest;
    cin >> cntTest;
    cout.precision(30);
    for (int test = 0; test < cntTest; ++test) {

        cout << "Case #" << test + 1 << ": ";
        double d;
        int n;
        cin >> d >> n;
        vector<double> pos(n), sp(n);
        vector<double> times(n);
        double max_time = -1.0;
        for (int i = 0; i < n; ++i) {
            cin >> pos[i] >> sp[i];
            times[i] = (d - pos[i]) / sp[i];
            max_time = max(max_time, times[i]);
        }

        cout << d / max_time << endl;


    }

    return 0;
}