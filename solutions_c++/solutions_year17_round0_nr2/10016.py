#include "bits/stdc++.h"

using namespace std;

struct Row {
    vector<int> vec;
    int flipper_size;
    
    Row() {}
    Row(const string & row, int flipper_size) : flipper_size(flipper_size) {
        for (char ch : row) {
            if (ch == '+') {
                vec.emplace_back(1);
            } else {
                vec.emplace_back(0);
            }
        }
    }
    
    bool is_happy() {
        int sum = 0;
        for (int v : vec) {
            sum += v;
        }
        return sum == (int)vec.size();
    }
    
    bool operator==(const Row &op) const {
        return (vec == op.vec);
    }
    
    bool operator<(const Row &op) const {
        for (int index = 0; index < (int)vec.size(); ++index) {
            if (vec[index] == op.vec[index]) { continue; }
            return vec[index] < op.vec[index];
        }
        return false;
    }
};

class Solution {
//private:
//    int T;
//    vector<Row> rows;
public:
//    void read() {
//        cin >> T;
//        string row;
//        int size;
//        for (int test = 0; test < T; ++test) {
//            cin >> row >> size;
//            rows.emplace_back(row, size);
//        }
//    }
    
//    bool is_in_field(const Vertex & v) {
//        if (v.row < n && v.row >= 0 && v.column < m && v.column >= 0) {
//            if (g[v.row][v.column] != '1') {
//                return true;
//            } else {
//                cout << v.row << "->" << v.column << endl;
//                return false;
//            }
//        }
//        return false;
//    }
//    void solve_all() {
//        for (int test = 0; test < T; ++test) {
//            int answer = solve(test);
//            if (answer != -1) {
//                cout << "Case #" << test + 1 << ": " << answer << endl;
//            } else {
//                cout << "Case #" << test + 1 << ": " << "IMPOSSIBLE" << endl;
//            }
//        }
//    }
    
    long long bin_search(long long n, const vector<long long> & vec) {
        int L = -1;
        int R = (int)vec.size() + 1;
        while(R - L > 1) {
            int M = L + (R - L) / 2;
            if (vec[M] > n) {
                R = M;
            } else {
                L = M;
            }
        }
        return vec[L];
    }
    
    void solve() {
        queue<string> q;
        vector<long long> ans = { 0 };
        unordered_set<string> visited;
        for (int i = 1; i <= 9; ++i) {
            q.push(to_string(i));
            visited.insert(to_string(i));
        }
        while(!q.empty()) {
            string cur = q.front(); q.pop();
            ans.emplace_back(stoll(cur));
            if (cur.length() > 17) { continue; }
            int last_digit = cur[cur.length() - 1] - '0';
            
            for (; last_digit < 10; ++last_digit) {
                string neighbour = cur;
                neighbour.push_back('0' + last_digit);
                if (!visited.count(neighbour)) {
                    visited.insert(neighbour);
                    q.push(neighbour);
                }
            }
        }
        ans.push_back((long long)(pow(10, 18)));
        ans.push_back(((long long)(pow(10, 18))) + 1LL);
        
        int T;
        cin >> T;
        long long num;
        for (int t = 1; t <= T; ++t) {
            cin >> num;
            cout << "Case #" << t << ": " << bin_search(num, ans) << endl;
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    Solution solution;
//    solution.read();
    solution.solve();
    
    return 0;
}
