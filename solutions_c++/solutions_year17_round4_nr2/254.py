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

void solve() {
    int N, C, M;
    cin >> N >> C >> M;
    vector< vector<int> > a(N);
    for(int i=0;i<M;i++) {
        int t1, t2;
        cin >> t2 >> t1;
        t1--;t2--;
        a[t2].push_back(t1);
    }
    int ans = 0;
    vector<int> dif(C);
    int max_dif = 0;
    int entries = 0;
    for(int i=0;i<a.size();i++) {
        for(int j=0;j<a[i].size();j++) {
            dif[a[i][j]]++;
            max_dif = max(max_dif, dif[a[i][j]]);
        }
        entries += a[i].size();
        int slots = ans * (i + 1);
        int need = entries / (i + 1) + (entries % (i + 1) == 0 ? 0 : 1);
        ans = max(ans, max(need, max_dif));
    }
    int ans2 = 0;
    for(int i=0;i<a.size();i++)
        ans2 += max(0, ((int)a[i].size()) - ans);
    cout << ans << " " << ans2 << endl;
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