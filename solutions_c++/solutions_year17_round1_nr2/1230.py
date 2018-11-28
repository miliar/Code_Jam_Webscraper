#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
const int NUM_PACKAGE = 55;
const int INGREDIENT_TYPE = 55;
const int INF = 1 << 30;

class Range {
public:
    int bgn, end;
    Range(){}
    Range(int bgn, int end): bgn(bgn), end(end){}
    bool operator< (const Range &opp) const {
        if (bgn != opp.bgn) return bgn < opp.bgn;
        return end < opp.bgn;
    }
};


class Event {
public:
};

int N; // the number of ingredients
int P; // the number of packages

// R[i]: the number of grams i-th ingredient needed to make one ratatouille
int R[INGREDIENT_TYPE];

// Q[i][j]:  the quantity [gram] in the j-th package of the i-th ingredient
int Q[INGREDIENT_TYPE][NUM_PACKAGE];

void read() {
    cin >> N >> P;
    for (int i = 0; i < N; ++i) {
        cin >> R[i];
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < P; ++j) {
            cin >> Q[i][j];
        }
    }
}
void add(map<int, pair<bool, bool> > &nBuy2flg, int idx, bool bgn, bool end) {
    if (nBuy2flg.count(idx) == 0) {
        nBuy2flg[idx] = make_pair(bgn, end);
    } else {
        nBuy2flg[idx].first |= bgn;
        nBuy2flg[idx].second |= end;
    }
}

void work(int cases) {
    Range numRange[INGREDIENT_TYPE][NUM_PACKAGE];
    
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < P; ++j) {
            int bgn = (Q[i][j] * 10 + R[i] * 11 - 1) / (R[i] * 11);
            int end = (Q[i][j] * 10) / (R[i] * 9);
            numRange[i][j] = Range(bgn, end);

            if (bgn > end) {
                numRange[i][j] = Range(-1, -1);
            }
        }
    }
    for (int i = 0; i < N; ++i) {
        sort(numRange[i], numRange[i] + P);
    }
    
    // nBuy2flg[nBuy] : (range bgn flag, range end flag)
    map<int, pair<bool, bool> > nBuy2flg;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < P; ++j) {
            Range &range = numRange[i][j];
            if (range.bgn == -1) continue;

            add(nBuy2flg, range.bgn - 1, false, true);
            add(nBuy2flg, range.bgn    , true, false);
            add(nBuy2flg, range.end    , false, true);
            add(nBuy2flg, range.end + 1, true, false);
            
            if (nBuy2flg.count(range.end + 1) == 0) {
                nBuy2flg[range.end + 1] = make_pair(false, true);
            } else {
                nBuy2flg[range.end + 1].second = true;
            }
        }
    }
    add(nBuy2flg, 0, true, false);
    add(nBuy2flg, INF, false, true);
    
    int ans = 0;
    
    bool used[INGREDIENT_TYPE][NUM_PACKAGE] = {};
    map<int, pair<bool, bool> >::iterator it = nBuy2flg.begin();
    while (it != nBuy2flg.end()) {
        map<int, pair<bool, bool> >::iterator next = it;
        
        while (!next->second.second) {
            ++next;
        }
        
        // eliminate range [it->first, next->first]
        int bgn = it->first;
        int end = next->first;
        vector<int> toUse;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < P; ++j) {
                if (used[i][j]) continue;
                if (max(bgn, numRange[i][j].bgn) <= min(end, numRange[i][j].end)) {
                    toUse.push_back(j);
                    break;
                }
            }
        }

        if (toUse.size() == N) {
            for (int i = 0; i < toUse.size(); ++i) {
                used[i][toUse[i]] = true;
            }
            ++ans;
        } else {
            ++next;
            while (next != nBuy2flg.end() && !next->second.first) {
                ++next;
            }
            it = next;
        }
    }
    
    cout << "Case #" << cases << ": " << ans << endl;
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
