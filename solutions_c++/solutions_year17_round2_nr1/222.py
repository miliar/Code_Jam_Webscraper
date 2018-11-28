#include <iostream>
#include <string.h>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;
void print(int testNum, long double answer) {
    cout << "Case #" << testNum << ": ";
    printf("%.10f\n", (double)answer);
}

int main(void) {
    freopen("/Users/glebone/Downloads/A-large.in-2.txt", "r", stdin);
    freopen("/Users/glebone/ClionProjects/bsuir/result.out", "w", stdout);
    int t;
    cin >> t;
    for (int test = 1; test <= t; test++) {
        int d, n;
        cin >> d >> n;
        vector <pair <int, int> > posAndSpeed;

        for (int j = 0; j < n; j++) {
            int x, y;
            cin >> x >> y;
            posAndSpeed.push_back({x, y});
        }

        long double mn = 0;

        for (int i = 0; i < n; i++) {
            mn = max(((long double) d - posAndSpeed[i].first) / posAndSpeed[i].second, mn);
        }

        long double v = d / mn;
        v -= 1e-11;
        print(test, v);
        //print(test, to_string(v));
    }
}