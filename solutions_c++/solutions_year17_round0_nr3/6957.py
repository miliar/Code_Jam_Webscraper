#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<int> solve(int s, int p) {
    vector<bool> occupied(s, false);
    int index = (s - 1) / 2;
    occupied[index] = true; occupied[0] = true; occupied[s - 1] = true;
    set<int> indexes;
    indexes.insert(index); indexes.insert(0); indexes.insert(s - 1);
    p--;
    int start = 0;
    int max_len = -1; int max_start = -1; int max_end = -1;
    while (p > 0) {
        for (const int &end : indexes) {
            int len = end - start - 1;
            if (len > 0 && len > max_len) {
                max_len = len; max_start = start; max_end = end;
            }
            start = end;
        }
        index = (max_start + max_end) / 2;
        occupied[index] = true; indexes.insert(index);
        start = 0;
        max_len = -1;
        p--;
    }

    vector<int> ans;
    int count = 0;
    for (int i = index + 1; i < s; ++i) {
        if (!occupied[i]) {
            count++;
        } else {
            break;
        }
    }
    ans.push_back(count);
    count = 0;
    for (int i = index - 1; i >= 0; --i) {
        if (!occupied[i]) {
            count++;
        } else {
            break;
        }
    }
    ans.push_back(count);
    sort(ans.begin(), ans.end());

    return ans;
}

int main() {
    int t, stalls, people;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> stalls >> people;
        vector<int> ans = solve(stalls + 2, people);
        cout << "Case #" << i << ": " << ans[1] << " " << ans[0] << endl;
    }

    return 0;
}