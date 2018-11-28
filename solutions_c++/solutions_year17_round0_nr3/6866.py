#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>

using namespace std;

vector<bool> makeEmptyStalls(int N) {
    return vector<bool>(N, false);
}

vector<int> getEmptyStallsIdx(vector<bool>& stalls) {
    vector<int> idxs;
    for (int i = 0; i < stalls.size(); ++i) {
        if (!stalls[i]) {
            idxs.push_back(i);
        }
    }
    return idxs;
}

void occupyStalls(vector<bool>& stalls, int idx) {
    stalls[idx] = true;
}

pair<int, int> getLR(vector<bool>& stalls, int idx) {
    int l = 0;
    for (int i = idx-1; i >= 0; --i) {
        if (stalls[i]) {
            break;
        }
        l++;
    }

    int r = 0;
    for (int i = idx+1; i < stalls.size(); ++i) {
        if (stalls[i]) {
            break;
        }
        r++;
    }

    return pair<int, int>(l, r);
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {
        int N, K;
        cin >> N >> K;
        auto stalls = makeEmptyStalls(N);
        for (int j = 0; j < K; ++j) {
            int choosedIdx = -1;
            map< int, vector<int> > minLRs;
            auto emptyStallIdxs = getEmptyStallsIdx(stalls);
            for (int idx : emptyStallIdxs) {
                auto lr = getLR(stalls, idx);
                int minLR = min(lr.first, lr.second);
                minLRs[minLR].push_back(idx);
            }

            vector<int>& maximalMinLrIdxs = minLRs.rbegin()->second;
            if (maximalMinLrIdxs.size() == 1) {
                choosedIdx = minLRs.rbegin()->second[0];
            } else {
                map<int, vector<int> > maxLRs;
                for (int idx : maximalMinLrIdxs) {
                    auto lr = getLR(stalls, idx);
                    int maxLR = max(lr.first, lr.second);
                    maxLRs[maxLR].push_back(idx);
                }
                choosedIdx = maxLRs.rbegin()->second[0];
            }

            if (j == K-1) {
                auto lr = getLR(stalls, choosedIdx);
                cout << "Case #" << i+1 << ": " << max(lr.first, lr.second) << " " << min(lr.first, lr.second) << endl;
            } else {
                occupyStalls(stalls, choosedIdx);
            }
        }
    }

    return 0;
}
