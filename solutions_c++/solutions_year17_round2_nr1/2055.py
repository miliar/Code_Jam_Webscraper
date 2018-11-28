#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <tuple>
#include <sstream>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <queue>
#include <cstdlib>
#include <stdio.h>
using namespace std;


int main () {
    int cases;
    cin >> cases;
    for (int cc = 1; cc <= cases; ++cc) {
        cout << "Case #" << cc << ": ";
        int n;
        double d;
        double maxi = 0;
        cin >> d >> n;
        for (int i = 0; i < n; ++i) {
            double k, s;
            cin >> s >> k;
            double t = (d - s) / k;
            maxi = max(maxi, t);
        }
        printf("%.8lf\n", d / maxi);
    }
}
