#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

struct Entry {
    Entry(int mi_, int ma_, int pos_)
        : mi(mi_), ma(ma_), pos(pos_)
    {
    }
    int mi, ma, pos;
    bool operator<(const Entry& other) {
        if (mi > other.mi) {
            return true;
        } else if (mi == other.mi) {
            if (ma > other.ma) {
                return true;
            } else if (ma == other.ma) {
                if (pos < other.pos) {
                    return true;
                }
            }
        }
        return false;
    }
};

int main() {
    int nTests = 0;
    cin >> nTests;
    for (int t = 1; t <= nTests; ++t) {
        int n = 0;
        cin >> n;
        int k = 0;
        cin >> k;
        set<int> occupied;
        occupied.insert(0);
        occupied.insert(n + 1);
        int currMax = 0;
        int currMin = 0;
        for (int i = 0; i < k; ++i) {
            vector<Entry> candidates;
            for (int j = 0; j < n + 2; ++j) {
                if (occupied.find(j) == occupied.end()) {
                    auto pos = occupied.lower_bound(j);
                    auto tmp = pos;
                    int right = *pos;
                    int left = *(--tmp);
                    int leftEmpty = j + 1 - left - 1 - 1;
                    int rightEmpty = right + 1 - j - 1 - 1;
                    candidates.push_back(Entry(min(leftEmpty, rightEmpty),
                                               max(leftEmpty, rightEmpty), j));
                    // std::cout << "j" << j << "\n";
                    // std::cout << "leftEmpty" << leftEmpty << "\n";
                    // std::cout << "rightEmpty" << rightEmpty << "\n";
                    // std::cout << "left" << left << "\n";
                    // std::cout << "right" << right << "\n";
                }
            }
            sort(candidates.begin(), candidates.end());
            // std::cout << candidates.begin()->pos << "\n";
            occupied.insert(candidates.begin()->pos);
            currMax = candidates.begin()->ma;
            currMin = candidates.begin()->mi;
        }
        cout << "Case #" << t << ": " << currMax << " " << currMin << "\n";
    }

    return 0;
}
