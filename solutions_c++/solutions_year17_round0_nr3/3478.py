#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int getLS(const vector<int> &stalls, int s) {
    int ls = 0;
    for (int i = s - 1; i >= 0; --i) {
        if (stalls[i] == 1) {
            return ls;
        }
        ++ls;
    }
    return ls;
}

int getRS(const vector<int> &stalls, int s) {
    int rs = 0;
    for (int i = s + 1; i < stalls.size(); ++i) {
        if (stalls[i] == 1) {
            return rs;
        }
        ++rs;
    }
    return rs;
}

int findStall(const vector<int> &stalls) {
    int max_min = 0;
    int max_max = 0;
    int max_stall = 0;
    for (int i = 0; i < stalls.size(); ++i) {
        if (stalls[i] == 1) {
            continue;
        }

        int ls = getLS(stalls, i);
        int rs = getRS(stalls, i);
        int mn = min(ls, rs);
        int mx = max(ls, rs);
        if (max_min < mn) {
            max_min = mn;
            max_stall = i;
        } else if (max_min == mn) {
            if (mx > max_max) {
                max_max = mn;
                max_stall = i;
            }
        }
    }
    return max_stall;
}

void printSolution2(int n, int k) {
    vector<int> stalls(n, 0);
    int last_stall = 0;

    for (int i = 0; i < k; ++i) {
        int s = findStall(stalls);
        stalls[s] = 1;
        last_stall = s;
    }
    int ls = getLS(stalls, last_stall);
    int rs = getRS(stalls, last_stall);
    cout << max(ls, rs) << " " << min(ls, rs) << endl;
}

void printSolution(int n, int k) {
    auto cmp = [](pair<int, int> l, pair<int, int> r) {
        return l.second - l.first < r.second - r.first;
    };

    priority_queue<pair<int, int>, vector<pair<int, int>>,  decltype(cmp)> pq(cmp);
    pq.push(make_pair(0, n - 1));

    int mid;
    int ls;
    int rs;

    for (int i = 0; i < k; ++i) {
        auto t = pq.top();
        pq.pop();
        
        mid = (t.first + t.second) / 2;
        ls = mid - t.first;
        rs = t.second - mid;
        if (ls > 0) {
            pq.push(make_pair(t.first, mid - 1));
        }
        if (rs > 0) {
            pq.push(make_pair(mid + 1, t.second));
        }
    }
    cout << max(ls, rs) << " " << min(ls, rs) << endl;
}

int main(int argc, char *argv[]) {
    int t;

    cin >> t;
    for (int i = 1; i <= t; ++i) {
        int n, k;
        cin >> n >> k;
        cout << "Case #" << i << ": ";
        printSolution(n, k);
    }

    return 0;
}