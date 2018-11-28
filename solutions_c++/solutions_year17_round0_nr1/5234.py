#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

void get_next_layer(string&s, int k, unordered_set<string>& visited, vector<string>& next_layer) {
    // vector<string> res;

    // cout << "\nparent: " << s << endl;
    for (int i = 0; i + k <= s.size(); ++i) {
        string child = s;
        for (int j = 0; j < k; ++j) {
            if (child[i+j] == '+') child[i+j] = '-';
            else child[i+j] = '+';
        }
        // cout << "insert: " << child << endl;
        if (visited.find(child) != visited.end()) continue;

        visited.insert(child);
        next_layer.push_back(child);
    }


    // return res;
}

string solve(string& s, int k) {
    string target = string(s.size(), '+');
    if (s == target) {
        return "0";
    }
    // if (2*k > s.size()) {
    //     int dup = 2*k - s.size();
    //     int start = k - dup;
    //     auto subs = s.substr(start, dup);
    //     if (subs != string(subs.size(), '+') || subs != string(subs.size(), '-')) {
    //         return "IMPOSSIBLE";
    //     }
    // }
    unordered_set<string> visited;
    visited.insert(s);
    // int cnt = 0;
    vector<string> layer;
    get_next_layer(s, k, visited, layer);
    int cnt = 1;
    vector<string> next_layer;
    while (!layer.empty()) {

        auto cur = layer.back();
        // cout << "visit: " << cur << endl;
        if (cur == target) {
            return to_string(cnt);
        }
        layer.pop_back();
        get_next_layer(cur, k, visited, next_layer);
        if (layer.empty()) {
            cnt++;
            swap(layer, next_layer);
            // cout << "layer: " << cnt << endl;
        }
    }

    return "IMPOSSIBLE";
}



int main() {
    int t;
    cin >> t;
    int i = 0;
    while (i++ < t) {
        string s;
        int k;
        cin >> s >> k;
        cout << "Case #" << i << ": " << solve(s, k) << endl;
    }
}
