#include <cstdio>
#include <iostream>
#include <iomanip>
#include <vector>
#include <set>

using namespace std;

long double PI = 3.141592653589793;

bool cmp(pair<int, int> &a, pair<int,int> &b) {
    if (a.first != b.first)
        return a.first > b.first;

    if (a.second != b.second)
        return a.second > b.second;
    
    return false;
}

int main()  {
    int T; scanf("%d", &T); int test_id = 0;
    while (test_id < T) { test_id ++;
        printf("Case #%d: ", test_id);

        int n, k; scanf("%d %d", &n, &k);
        vector< pair<int, int> > cake(n);
        for(int i = 0; i < n; i++) {
            int r, h; scanf("%d %d", &r, &h);
            cake[i] = make_pair(r, h);
        }
        sort(cake.begin(), cake.end(), cmp);
        long long ans = 0;
        for(int i = 0; i <= n - k; i++) {
            long long curans = 0;

            curans += cake[i].first * 1ll * cake[i].first;
            curans += cake[i].first * 1ll * cake[i].second * 2ll;
            vector<long long> curvalues;
            for(int j = i + 1; j < n; j++) {
                curvalues.push_back(cake[j].first * 2ll * cake[j].second);
            }
            sort(curvalues.begin(), curvalues.end());
            reverse(curvalues.begin(), curvalues.end());

            for(int j = 0; j < k - 1; j++) {
                curans += curvalues[j];
            }
            if (curans > ans) ans = curans;
        }
        long double rs = ans * PI;

        cout << fixed << setprecision(12) << rs << endl;
    }
}
