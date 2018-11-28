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
private:
    int T;
    vector<Row> rows;
public:
    void read() {
        cin >> T;
        string row;
        int size;
        for (int test = 0; test < T; ++test) {
            cin >> row >> size;
            rows.emplace_back(row, size);
        }
    }
    
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
    void solve_all() {
        for (int test = 0; test < T; ++test) {
            int answer = solve(test);
            if (answer != -1) {
                cout << "Case #" << test + 1 << ": " << answer << endl;
            } else {
                cout << "Case #" << test + 1 << ": " << "IMPOSSIBLE" << endl;
            }
        }
    }
    
    int solve(int test) {
        Row start = rows[test];
        int K = start.flipper_size;
        int N = (int)start.vec.size();
        queue<Row> q;
        set<Row> visited;
        map<Row, int> distance;
        q.push(start);
        visited.insert(start);
        distance[start] = 0;
        
        while(!q.empty()) {
            Row cur = q.front(); q.pop();
            
            if (cur.is_happy()) {
                return distance[cur];
            }
            
            for (int left = 0; left < N - K + 1; ++left) {
                Row neighbour = cur;
                for (int index = left; index < left + K; ++index) {
                    neighbour.vec[index] ^= 1;
                }
                if (!visited.count(neighbour)) {
                    q.push(neighbour);
                    visited.insert(neighbour);
                    distance[neighbour] = distance[cur] + 1;
                }
            }
        }
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    Solution solution;
    solution.read();
    solution.solve_all();
    
    return 0;
}
