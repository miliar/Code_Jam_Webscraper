#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int n, c, m;
        cin >> n >> c >> m;
        vector<int> seats(n);
        vector<int> pass(n);
        for (int i = 0; i < m; ++i) {
            int a, b;
            cin >> a >> b;
            ++seats[--a];
            ++pass[--b];
        }
        int rays = 0;
        for (int i = 0; i < c; ++i) {
            rays = max(rays, pass[i]);
        }
        int max_seats = 0;
        if (seats[0] >= rays) {
            cout << "Case #" << test << ": " << seats[0] << " 0" << endl;
        } else {
            for (int i = 0; i < n; ++i) {
                max_seats = max(max_seats, seats[i]);
            }
            if (max_seats <= rays) {
                cout << "Case #" << test << ": " << rays << " 0" << endl;
            } else {
                cout << "Case #" << test << ": " << rays << " " << max_seats - rays << endl;
            }
        }
    }
    return 0;
}