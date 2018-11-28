#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <ctime>
#include <unordered_map>
using namespace std;

clock_t begin_time, end_time;
void printtime() {
    end_time = clock();
    double elapsed_secs = double(end_time - begin_time) / CLOCKS_PER_SEC;
    cerr << "\nTime elapsed: " << elapsed_secs << endl;
}

bool ok(string s) {
    for(int i=1;i<s.size();i++) {
        if(s[i-1] > s[i])
            return false;
    }
    return true;
}

void solve() {
    int n, d;
    cin >> d >> n;
    double res = 0;
    for(int i=0;i<n;i++) {
        int k, s;
        cin >> k >> s;
        res = max(res, (0. + d - k) / s);
    }
    res = (0. + d) / res;
    printf("%.7f\n", res);
}

int main() {
    begin_time = clock();

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int tests;
    scanf("%d", &tests);
    for(int i=0;i<tests;i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }

    printtime();
    return 0;
}