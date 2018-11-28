#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

/*class Tree {
private:
    const int H = 21;
    vector<vector<int>> levels;
public:
    Tree()
    {
        levels.clear();
        for (int i = 0;i < H; i++)
            levels.push_back(vector<int>(1<<i, 0));
    }

    void insert(int v, int f = 1)
    {
        for (int d = H - 1;d >= 0;d--) {
            int pos = v >> (H - 1 - d);
            levels[d][pos] += f;
        }
    }

    int get_min_ge(double v) {
        int vv = ceil(v);
        if (get_max() < vv)
            return -1;
        int d = H - 1, cur = vv;
        while (d >= 1) {
            if (levels[d - 1][cur / 2] > 0) {
            } else {
                d--;
                cur /= 2;
            }
        }
    }

    int get_max() {
        int ret = 0;
        for (int d = 1;d < H; d++) {
            if (levels[d][2 * ret + 1] > 0) {
                ret = 2 * ret + 1;
            } else {
                ret = 2 * ret;
            }
        }
        return ret;
    }
};*/

int main(int argc, char **argv)
{
    int T;
    cin >> T;
    for (int t = 1;t <= T; t++) {
        int N, P;
        cin >> N >> P;
        vector<int> ratios(N);
        for (auto& r: ratios)
            cin >> r;

        vector<multiset<long long>> packs;
        for (int i = 0;i < N; i++) {
            packs.push_back(multiset<long long>());
            multiset<long long>& tt = packs[i];
            for (int j = 0;j < P; j++) {
                int t;
                cin >> t;
                tt.insert(t);
            }
        }

        int ret = 0;
        for (long long f = 1;f <= 1000000;) {
            // f * ratios[i] for each 1 <= i <= P
begi:
            vector<long long> rem(N, -1);
            bool all = true;
            for (int i = 0;i < N; ++i) {
                long long vv =  ceil(f * 0.9 * ratios[i]);
                auto e = packs[i].lower_bound(vv);
                if (e == packs[i].end() || *e > f * 1.1 * ratios[i]) {
                    all = false;
                    goto cont;
                }
                rem[i] = *e;
            }
            ret++;
            for (int i = 0;i < N; ++i)
                packs[i].erase(packs[i].lower_bound(rem[i]));
            goto begi;
cont:;
        f++;
        }

        cout << "Case #" << t << ": " << ret << endl;
    }

    return 0;
}
