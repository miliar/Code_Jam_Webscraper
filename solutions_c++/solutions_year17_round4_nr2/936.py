#include <algorithm>
#include <iostream>
#include <iomanip>
#include <utility>
#include <vector>

using namespace std;

bool try_kuhn (int v, const vector<int> &a, const vector<int> &b,
                      vector<char> &used, vector<int> &mt) {
    if (v < 0 || v >= (int)used.size()) {
        cout << v << endl;
    }
	if (used[v]) return false;
	used[v] = true;
	for (int to = 0; to < (int)b.size(); ++to) {
        if (a[v] == b[to]) {
            continue;
        }
		if (mt[to] == -1 || try_kuhn (mt[to], a, b, used, mt)) {
			mt[to] = v;
			return true;
		}
	}
	return false;
}

int max_matching(int stop_num, const vector<int> &a, const vector<int> &b) {
    if (stop_num == 0) {
        return 0;
    }
    int n = a.size();
    vector<int> mt(b.size(), -1);
    vector<char> used(a.size());
 
    int res = 0;
	for (int v=0; v<n; ++v) {
		used.assign(a.size(), false);
        if (try_kuhn(v, a, b, used, mt)) {
            res++;
            if (res >= stop_num) {
                break;
            }
        }
	}
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    for (int testCase = 0; testCase < T; ++testCase) {
        int n, c, m;
        cin >> n >> c >> m;
        vector<pair<int, int>> a(m);
        vector<int> pos[2];
        pos[0].reserve(m);
        pos[1].reserve(m);
        int cnt_fst[2] = {0};
        int cnt_nonfst[2] = {0};
        for (auto &p : a) {
            cin >> p.first >> p.second;
            p.first--;
            p.second--;
            if (p.first == 0) {
                cnt_fst[p.second]++;
            } else {
                cnt_nonfst[p.second]++;
                pos[p.second].push_back(p.first);
            }
        }
        int num = cnt_fst[0];
        cnt_nonfst[1] = max(cnt_nonfst[1] - cnt_fst[0], 0);
        num += cnt_fst[1];
        cnt_nonfst[0] = max(cnt_nonfst[0] - cnt_fst[1], 0);

        sort(begin(pos[0]), end(pos[0]));
        sort(begin(pos[1]), end(pos[1]));
        int common_rides = min(cnt_nonfst[0], cnt_nonfst[1]);
        int mmt = max_matching(common_rides, pos[0], pos[1]);
        num += max(cnt_nonfst[0], cnt_nonfst[1]);
        int proms = common_rides - mmt;

        cout << "Case #" << testCase + 1 << ": ";
        cout << num << " " << proms;
        cout << endl;
    }
    return 0;
}
