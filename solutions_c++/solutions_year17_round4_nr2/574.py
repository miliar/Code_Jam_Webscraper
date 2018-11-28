#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

const int N = 1111;
int n, m, C;
int sum[N];
int cnt[N];
//int pos[N];
//bool use[N][N];

bool check(int mid) {
    //cout << mid << endl;
    for (int i = 1; i < N; i++) {
        //cout << sum[i] << "vs" << mid * i << endl;
        if (sum[i] > mid * i) return false;
    }
    return true;
}

int main() {
    int T, Case = 1;
    cin >> T;
    while (T--) {
        cin >> n >> C >> m;
        memset(cnt, 0, sizeof(cnt));
        memset(sum, 0, sizeof(sum));
        int L = 0;
        //vector<pair<int, int> > tickets;
        for (int i = 0; i < m; i++) {
            int x, y;
            cin >> x >> y;
            cnt[y]++;
            L = max(L, cnt[y]);
            sum[x]++;
            //tickets.push_back(make_pair(x, y));
        }
        //cout << L << " 12313" << endl;
        for (int i = 1; i < N; i++) {
            sum[i] += sum[i - 1];
            //cout << i << " " << sum[i] << endl;
        }
        int R = m;
        int ans1 = 0;
        while (L <= R) {
            int mid = (L + R) / 2;
            if (check(mid)) {
                ans1 = mid;
                R = mid - 1;
            } else L = mid + 1;
        }
        assert(ans1 != 0);
        //cout << "Debug " << ans1 << endl;
        //set<int> used[N];
        //sort(tickets.begin(), tickets.end());
        //for (int i = 1; i <= ans1; i++) pos[i] = C + 1;
        int ans2 = 0;
        for (int i = 1; i < N; i++) {
            //cout << sum[i] - sum[i - 1] << " " << ans1 << endl;
            if (sum[i] - sum[i - 1] > ans1) ans2 += sum[i] - sum[i - 1] - ans1;
        }
        /*
        memset(use, 0, sizeof(use));
        for (auto it = tickets.begin(); it != tickets.end(); it++) {
            int x = it->first, y = it->second;
            int idx = -1;
            for (int i = 1; i <= ans1; i++) {
                if (used[i].count(y)) continue;
                if (!use[i][x]) {
                    idx = i;
                    break;
                }
            }
            used[idx].insert(y);
            if (pos[idx] > x) pos[idx] = x;
            else {
                pos[idx]--;
                ans2++;
            }

        }
        */
        cout << "Case #" << Case++ << ": " << ans1 << " " << ans2 << endl;
    }
    return 0;
}
