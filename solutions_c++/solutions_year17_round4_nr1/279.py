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
#include <memory>
#include <memory.h>
using namespace std;

clock_t begin_time, end_time;
void printtime() {
    end_time = clock();
    double elapsed_secs = double(end_time - begin_time) / CLOCKS_PER_SEC;
    cerr << "\nTime elapsed: " << elapsed_secs << endl;
}

double get_elapsed_time() {
    return double(clock() - begin_time) / CLOCKS_PER_SEC;
}

vector<int> R;
map< pair<vector<int>, int>, int> cache;
int f(int rest) {
    if(cache.count({R, rest}))
        return cache[{R, rest}];
    int sm = 0;
    for(int i=0;i<R.size();i++)
        sm += R[i];
    if(sm == 0)
        return 0;

    int res = 0;
    for(int i=0;i<R.size();i++) {
        if(R[i] == 0)
            continue;
        R[i] --;
        int trest = (rest - i + R.size()) % R.size();
        res = max(res, f(trest));
        R[i] ++;
    }
    if(rest == 0)
        res ++;
    return cache[{R, rest}] = res;
}

void solve() {
    int n = 100, p = 4;
    cin >> n >> p;
    R.clear();
    R.resize(p, 0);
    //cache.clear();
    for(int i=0;i<n;i++) {
        int t = rand() % 100 + 1;
        scanf("%d", &t);
        R[t % p]++;
    }
    cout << f(0) << endl;
}

int main() {
    begin_time = clock();
#ifdef __APPLE__
    //freopen("in.txt", "r", stdin);
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int TEST;
    cin >> TEST;
    for(int test = 0; test < TEST; test ++) {
        printf("Case #%d: ", test + 1);
        solve();
        cerr << test << " done\n";
    }

    printtime();
    return 0;
}