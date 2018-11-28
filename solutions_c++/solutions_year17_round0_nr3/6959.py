#include "bits/stdc++.h"

using namespace std;

const int M = 15;

class Solution {
public:
    void solve_all() {
        int n, k;
        int T;
        cin >> T;
        for (int test = 0; test < T; ++test) {
            cin >> n >> k;
            pair<int, int> ans = solve(n, k);
            cout << "Case #" << test + 1 << ": " << ans.first << " " << ans.second << endl;
        }
    }
    
    pair<int, int> get_pair(int pos, const vector<int> myset) {
        int left_ans = 0;
        int left_pos = pos - 1;
        while(myset[left_pos--] == 0) {
            ++left_ans;
        }
        
        int right_ans = 0;
        int right_pos = pos + 1;
        while(myset[right_pos++] == 0) {
            ++right_ans;
        }
        return {left_ans, right_ans};
    }
    
    int min(const pair<int, int> &op) {
        return ::min(op.first, op.second);
    }
    
    int max(const pair<int, int> &op) {
        return ::max(op.first, op.second);
    }
    
    void print(const set<int> & vec) {
        for (auto v : vec) {
            cout << v;
        }
        cout << endl;
    }
    
    pair<int, int> find_ans(const set<int> & positions) {
//        print(positions);
        pair<int, int> best_pair = {0, 0};
        for (auto it = positions.begin(); it != positions.end(); ++it) {
            auto next_it = it;
            ++next_it;
            if (next_it == positions.end()) {
                break;
            }
            
            if (*next_it - *it > best_pair.second - best_pair.first) {
                best_pair = {*it, *next_it};
            }
        }
        int new_pos = (best_pair.second + best_pair.first) / 2;
//        cout << best_pair.first << "->" << new_pos << "->" << best_pair.second << endl;
        return {best_pair.second - new_pos - 1, new_pos - best_pair.first - 1};
    }
    
    pair<int, int> solve(int N, int K) {
        set<int> positions;
        positions.insert(1);
        positions.insert(N + 2);
        
        
        pair<int, int> best_pair = {0, 0};
        while(K > 0) {
//            print(positions);
            best_pair = {0, 0};
            for (auto it = positions.begin(); it != positions.end(); ++it) {
                auto next_it = it;
                ++next_it;
                if (next_it == positions.end()) {
                    break;
                }
                
                if (*next_it - *it > best_pair.second - best_pair.first) {
                    best_pair = {*it, *next_it};
                }
            }
            if (K == 1) {
                return find_ans(positions);
            }
            positions.insert((best_pair.second + best_pair.first) / 2);
            --K;
        }
//        print(positions);
        return {-1, -1};
    }
};

int main() {
    ios::sync_with_stdio(false);
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    Solution solution;
//    solution.read();
    solution.solve_all();
    
    return 0;
}
