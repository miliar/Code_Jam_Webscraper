#include <bits/stdc++.h>

using namespace std;

typedef pair <long long, long long> pt;

deque<pt> dq;

int main() {
    ifstream cin ("C-large.in");
    ofstream cout ("stall.out");
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int test;
    cin >> test;
    for (int ttest = 1; ttest <= test; ttest++) {
        cout << "Case #" << ttest << ": ";

        long long n, k;
        cin >> n >> k;

        if (k == 1) {
            cout << n / 2 << " " << n - (n / 2) - 1 << "\n";
            continue;
        }

        k--;
        dq.clear();
        if (n % 2 == 0) {
            dq.push_back(make_pair(n / 2, 1));
            dq.push_back(make_pair(n - (n / 2) - 1, 1));
        } else dq.push_back(make_pair(n / 2, 2));
        while (k) {
            pt cur = dq.front();
            dq.pop_front();

            if (k <= cur.second) {
                long long m = cur.first;
                cout << m / 2 << " " << m - (m / 2) - 1 << "\n";
                break;
            } else k -= cur.second;

            if (cur.first % 2 == 1) {
                pt tmp = make_pair(cur.first / 2, 2 * cur.second);
                if (!dq.empty()) {
                    if (tmp.first == dq.front().first) {
                        pt _front = dq.front();
                        dq.pop_front();

                        _front.second += tmp.second;
                        dq.push_front(_front);
                    } else if (tmp.first == dq.back().first) {
                        pt _back = dq.back();
                        dq.pop_back();

                        _back.second += tmp.second;
                        dq.push_back(_back);
                    } else dq.push_back(tmp);
                } else dq.push_back(tmp);
            } else {
                pt tmp1 = make_pair(cur.first / 2, cur.second);
                pt tmp2 = make_pair(cur.first - tmp1.first - 1, cur.second);

                if (!dq.empty()) {
                    if (tmp1.first == dq.back().first) {
                        pt _back = dq.back();
                        dq.pop_back();

                        _back.second += tmp1.second;
                        dq.push_back(_back);
                    } else dq.push_back(tmp1);
                } else dq.push_back(tmp1);
                dq.push_back(tmp2);
            }
        }
    }
}
