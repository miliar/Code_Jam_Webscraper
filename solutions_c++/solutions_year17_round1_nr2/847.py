#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

pair<int,int> getK(const int &a, const int &x) {
    int sk = (10 * x) / (11 * a) + ((10 * x) % (11 * a) ? 1 : 0);
    int bk = (10 * x) / (9 * a);
    if (bk < sk) return pair<int, int>(-1, -1);
    else return pair<int, int>(sk, bk);
}

int main()
{
    int testcase;
    cin >> testcase;
    for (int tc = 1; tc <= testcase; tc++) {
        int N, P;
        cin >> N >> P;
        vector<int> R(N);
        set<int> s;
        vector<vector<pair<int, int>>> Q(N, vector<pair<int, int>>(P));
        for (int i = 0; i < N; ++i) {
            cin >> R[i];
        }
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < P; ++j) {
                int q;
                cin >> q;
                Q[i][j] = getK(R[i], q);
                if (Q[i][j].first != -1) {
                    s.insert(Q[i][j].first);
                    s.insert(Q[i][j].second);
                }
            }
        }
        int ans = 0;
        for (const int& p : s) {
            bool sw = true;
            while (sw) {
                vector<int> idx(N, -1);
                for (int i = 0; i < N && sw; ++i) {
                    pair<int, int> minv(987654321, 987654321);
                    for (int j = 0; j < P; ++j) {
                        if (Q[i][j].first <= p && p <= Q[i][j].second && Q[i][j] < minv) {
                            minv = Q[i][j];
                            idx[i] = j;
                        }
                    }
                    if (idx[i] == -1) sw = false;
                }
                if (sw) {
                    ans++;
                    for (int i = 0; i < N; ++i) {
                        Q[i][idx[i]] = pair<int, int>(-1, -1);
                    }
                }
            }
        }
        cout << "Case #" << tc << ": " << ans << endl;
    }
    return 0;
}