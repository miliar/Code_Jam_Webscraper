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
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        int d, n;
        cin >> d >> n;

        double t = 0;
        for (int i = 0; i < n; ++i) {
            int x, v;
            cin >> x >> v;
            t = max(t, (double)(d - x) / (double)v);
        }
        cout << (double)d / t << endl;
    }

}